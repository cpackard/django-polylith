# Polylith Django Demo

Project demoing the Polylith architecture using the Django app system.

## Setup

### Installing Poetry

This project uses [Poetry](https://python-poetry.org/docs/) as the package manager. To install the tool on your local machine, run the command

```shell
curl -sSL https://install.python-poetry.org | python3 -
```

## Running a local project

After installing Poetry and downloading the repo, install the dependencies for the project and run the migrations. Then you're set to run the development server:

```shell
poetry install
DJANGO_SETTINGS_MODULE=api_project.settings poetry run python manage.py migrate
DJANGO_SETTINGS_MODULE=api_project.settings poetry run python manage.py runserver
```

## Development

### Adding a new component

You can create a new component using the project's command:

```shell
poetry shell
create_component <new_component_name>
```

You can also get help for any command by passing the `--help` flag:

```shell
create_component --help
```

### Create migrations

Migrations can be created for any components by running the `makemigrations` command for it from the root of the repo:

```shell
poetry run python manage.py makemigrations questions
```

Then apply the migrations as normal:

```shell
poetry run python manage.py migrate
```

#### Defining foreign-key relationships between components

From the [Django docs](https://docs.djangoproject.com/en/4.1/ref/models/fields/#foreignkey):

> To refer to models defined in another application, you can explicitly specify a model with the full application label. For example, if the `Manufacturer` model above is defined in another application called `production`, you’d need to use:

```python
class Car(models.Model):
    manufacturer = models.ForeignKey(
        'production.Manufacturer',
        on_delete=models.CASCADE,
    )
```

### Running Tests

To run tests for the entire project, run this command from the root of the repo:

```shell
poetry run pytest -v
```

Alternatively:

```shell
poetry shell
pytest -v
```

By default, this command will use the `DJANGO_SETTINGS_MODULE = "development.settings"` attribute in the root-level `pyproject.toml`. You can override this by setting a `DJANGO_SETTINGS_MODULE` environment variable or by passing the `--ds` CLI flag like `pytest --ds=api_project.settings`. See the [pytest-django docs](https://pytest-django.readthedocs.io/en/latest/configuring_django.html#) for more info.
