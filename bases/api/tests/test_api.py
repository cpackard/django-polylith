# Standard Library
import datetime

# Django Libraries
from django.test import Client, TestCase


class TestQuestions(TestCase):
    def test_create_and_find_question(self) -> None:
        c = Client()
        question = "Are ya ready?"
        post_response = c.post("/api/questions/", {"question": question})
        assert post_response.status_code == 201
        created_question = post_response.json()["result"]

        get_response = c.get("/api/questions/", {"question": question})
        assert get_response.status_code == 200
        assert get_response.json() == {"result": created_question}


class TestChoices(TestCase):
    def test_create_and_find_choices(self) -> None:
        c = Client()
        question = "Are ya ready?"
        post_response = c.post("/api/questions/", {"question": question})
        assert post_response.status_code == 201
        created_question = post_response.json()["result"]
        qid = created_question["id"]

        first_choice = "Aye, aye!"
        first_choice_res = c.post(
            "/api/choices/", {"question": qid, "choice": first_choice}
        )
        assert first_choice_res.status_code == 201
        first_choice_data = first_choice_res.json()["result"]
        first_choice_data["question_id"] = int(first_choice_data["question"])
        del first_choice_data["question"]

        second_choice = "Raincheck?"
        second_choice_res = c.post(
            "/api/choices/", {"question": qid, "choice": second_choice}
        )
        assert second_choice_res.status_code == 201
        second_choice_data = second_choice_res.json()["result"]
        second_choice_data["question_id"] = int(second_choice_data["question"])
        del second_choice_data["question"]

        # TODO: cleanup this questionable API
        get_response = c.get("/api/choices/", {"question": qid})
        assert get_response.status_code == 200
        assert get_response.json() == {
            "result": [first_choice_data, second_choice_data]
        }
