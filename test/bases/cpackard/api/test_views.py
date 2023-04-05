# Standard Library
import datetime
from random import randint

# Third-Party Libraries
import pytest

# Django Libraries
from django.test import Client

# Polylith Bricks
from cpackard import users


@pytest.fixture
def user_token(client: Client):
    user_num = randint(0, int(1e7))
    credentials = {"username": f"user{user_num}", "email": f"user{user_num}@nosus.com", "password": "Test123@$"}
    response = client.post("/api/auth/users/", credentials)
    assert response.status_code == 201, response.json()

    token_res = client.post("/api/auth/token/login/", credentials)
    assert token_res.status_code == 200, token_res.json()
    token = token_res.json()["auth_token"]

    return token


@pytest.mark.django_db
class TestQuestions:
    def test_create_and_find_question(self, user_token: str, client: Client) -> None:
        question = "Are ya ready?"
        post_response = client.post(
            "/api/questions/",
            {"question": question},
            headers={"Authorization": f"Token {user_token}"},
        )
        assert post_response.status_code == 201
        created_question = post_response.json()["result"]

        get_response = client.get(
            "/api/questions/",
            {"question": question},
            headers={"Authorization": f"Token {user_token}"},
        )
        assert get_response.status_code == 200
        assert get_response.json() == {"result": created_question}


@pytest.mark.django_db
class TestChoices:
    def test_create_and_find_choices(self, user_token: str, client: Client) -> None:
        question = "Are ya ready?"
        post_response = client.post(
            "/api/questions/",
            {"question": question},
            headers={"Authorization": f"Token {user_token}"},
        )
        assert post_response.status_code == 201
        created_question = post_response.json()["result"]
        qid = created_question["id"]

        first_choice = "Aye, aye!"
        first_choice_res = client.post(
            "/api/choices/",
            {"question": qid, "choice": first_choice},
            headers={"Authorization": f"Token {user_token}"},
        )
        assert first_choice_res.status_code == 201
        first_choice_data = first_choice_res.json()["result"]
        first_choice_data["question_id"] = int(first_choice_data["question"])
        del first_choice_data["question"]

        second_choice = "Raincheck?"
        second_choice_res = client.post(
            "/api/choices/",
            {"question": qid, "choice": second_choice},
            headers={"Authorization": f"Token {user_token}"},
        )
        assert second_choice_res.status_code == 201
        second_choice_data = second_choice_res.json()["result"]
        second_choice_data["question_id"] = int(second_choice_data["question"])
        del second_choice_data["question"]

        # TODO: cleanup this questionable API
        get_response = client.get(
            "/api/choices/",
            {"question": qid},
            headers={"Authorization": f"Token {user_token}"},
        )
        assert get_response.status_code == 200
        assert get_response.json() == {"result": [first_choice_data, second_choice_data]}


@pytest.mark.django_db
class TestSurveys:
    def test_create_and_find_surveys(self, user_token: str, client: Client) -> None:
        satisfaction = 5
        response_text = "Not bad!"

        post_response = client.post(
            "/api/surveys/",
            {"satisfaction": satisfaction, "response_text": response_text},
            headers={"Authorization": f"Token {user_token}"},
        )
        assert post_response.status_code == 201

        get_response = client.get(
            "/api/surveys/",
            {"satisfaction": satisfaction},
            headers={"Authorization": f"Token {user_token}"},
        )
        assert get_response.status_code == 200
        assert get_response.json() == {
            "result": [{"id": 1, "satisfaction": satisfaction, "response_text": response_text}]
        }
