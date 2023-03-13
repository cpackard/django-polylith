# Polylith Django Demo

Project demoing the Polylith architecture using the Django app system.

## Setup

### Installing Poetry

This project uses [Poetry]() as the package manager. To install the tool on your local machine, run the command

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

- Create the directory: `mkdir -p components/polls/src`
- Generate Django boilerplate: `poetry run python manage.py startapp polls components/src/polls`
- `cd` into the new directory and run `poetry config virtualenvs.create false --local` so you don't create sub-venvs.

### Create migrations

Migrations can be created for any components by running the `makemigrations` command for it from the root of the repo:

```shell
poetry run python manage.py makemigrations polls
```

Then apply the migrations as normal:

```shell
poetry run python manage.py migrate
```
