# Polylith Django Demo

Project demoing the [Polylith architecture](https://polylith.gitbook.io/polylith/) using the Django [app system](https://docs.djangoproject.com/en/4.1/ref/applications/) and the [Python Polylith](https://davidvujic.github.io/python-polylith-docs/) tool.

## Setup

### Installing Poetry

This project uses [Poetry](https://python-poetry.org/docs/) as the package manager. To install the tool on your local machine, run the command

```shell
curl -sSL https://install.python-poetry.org | python3 -
```

### Running a local project

After installing Poetry and downloading the repo, install the dependencies for the project and run the migrations. Then you're set to run the development server:

```shell
poetry install
poetry shell
python manage.py migrate
python manage.py runserver
```

You can run any command in this doc as an ad-hoc command in your root shell by prefixing it with `poetry run`. The rest of this doc assumes you're in an active `poetry shell` for brevity.

## Structure and Organization

Since this is a Django variant of the Polylith architecture it uses most of the key terms from the [Polylith overview docs](https://polylith.gitbook.io/polylith/introduction/polylith-in-a-nutshell).

To summarize the table below: *libraries* are used by *components*, which represent app entities through an `interface` module. *Bases* expose functionality of *components* publicly through endpoints. *Projects* assemble each of these into an artifact like a service.

<details><summary>Polylith concepts</summary>
<p>

| Name | Icon | Description |
| ---- | ---- | ----------- |
| Library | ![library](https://505824696-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LAhrWK1psIWk5h5zNLV%2F-MLRFm_9NfJLsJpcXde8%2F-MLRaXuk9NequZe8_Cuz%2Flibrary-small.png?alt=media&token=7d801a59-0377-4cc7-bad7-1bea43015f90) | A library is anything installed from PyPI or other package repositories. |
| Component | ![component](https://505824696-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LAhrWK1psIWk5h5zNLV%2F-MLRFm_9NfJLsJpcXde8%2F-MLR_67CCSuxxg6f-2Ir%2Fcomponent.png?alt=media&token=017e856d-67db-48cd-8852-bbf9d1549bb6) | Components are modules representing part of our domain, infrastructure, or third-party integration. They each have an interface of functions for other components or bases to use. |
| Base | ![base](https://505824696-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LAhrWK1psIWk5h5zNLV%2F-MLRFm_9NfJLsJpcXde8%2F-MLRdJ4sVNRI3e5Gwai0%2Fbase.png?alt=media&token=decbf922-06c6-4f35-95a8-41ec7891f869) | A base is a module that exposes component interfaces via endpoints, command-line, etc. |
| Brick | ![brick](https://505824696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LAhrWK1psIWk5h5zNLV%2Fuploads%2FRZMej4nrNznJMsZ6FGAW%2Fbrick.png?alt=media&token=83f1a352-9d82-4781-906d-af299b642381) | Brick is the common name for a component or base, which are our building blocks (together with libraries). |
| Project | ![project](https://505824696-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LAhrWK1psIWk5h5zNLV%2F-MLvr0aBnP0LO8jSq-lj%2F-MM-RiGnhRbPwxftgFvn%2Fproject.png?alt=media&token=74c5a034-92ed-49b8-81ec-7a1e26f7e60d) | A project specifies which libraries and bricks should be included in an artifact (service, command line tool, etc.) which allows reuse of components across multiple projects. |
| Development Project | ![dev-project](https://505824696-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LAhrWK1psIWk5h5zNLV%2F-MLvr0aBnP0LO8jSq-lj%2F-MM-Ro-4oXj9cBv5zswX%2Fdevelopment.png?alt=media&token=903d437b-781c-4aff-83c7-5a2767e13e4c) | A development project is the place we use to work with all our libraries, components, and bases, giving a “monolithic development experience”. |

</p>
</details>

Below are the Django-specific details of each term.

<details><summary>Component</summary>
<p>

Each component lives in a separate directory in the `components` folder and namespace.

The `interface.py` module is a set of functions using native data structures (e.g. lists and maps) for inputs and outputs. Each function in the interface module "passes-through" to an equivalent function in `core.py`, which enables encapsulation and allows for any private implementation (like using the ORM).

- The constraint of native data structures for input/output is necessary both as a “protocol” between components and to ensure encapsulation. For example: if the `questions` module returned `Question` ORM objects, that would expose the implementation details of using the ORM, and allow callers to use methods on the object for functionality instead of those from `questions.interface`.

`apps.py` is the module for [Django app configuration](https://docs.djangoproject.com/en/4.1/ref/applications/#configuring-applications), `types.py` is for shared types within the app, and `models.py` is the standard module for data models.

```
▾ workspace
  ▾ components
    ▾ cpackard
      ▾ questions
        ▸ migrations
        __init__.py
        apps.py
        core.py
        interface.py
        models.py
        types.py
```

</p>
</details>

<details><summary>Base</summary>
<p>

Like components, each base lives in a separate directory in the `bases` folder and namespace.

Bases expose component interfaces through endpoint functions defined in the conventional Django `views.py` module, which have their routes defined in `urls.py`. They also hold the common top-level Django configuration modules like `settings.py` and `wsgi.py`.

```
▾ workspace
  ▾ bases
    ▾ cpackard
      ▾ api
        __init__.py
        asgi.py
        manage.py
        settings.py
        urls.py
        views.py
        wsgi.py
```

</p>
</details>

<details><summary>Project</summary>
<p>

A project is the result of combining one base (or in rare cases several bases) with multiple components and libraries.

Unlike bases and components, projects have no `src` or `tests` directories because they contain no logic of their own. Instead, they have the `pyproject.toml` includes the components, bases, and required libs as dependencies for the final artifact.

```
▾ workspace
  ▾ projects
    ▾ monolith-api
      __init__.py
      pyproject.toml
      poetry.lock
```

</p>
</details>

<details><summary>Development Project</summary>
<p>

The development folder is where you can put code that you write to experiment or try out features. Here, you add all dependencies and bricks. This will make it possible to have the entire code-base available in one and the same virtual environment.

In this folder, it is quite common that developers keep their scratch-style Python modules. It is perfectly fine to version control them.

```
▾ workspace
  ▾ development
    __init__.py
    cpackard.py
  pyproject.toml
```

</p>
</details>

<details><summary>Tests</summary>
<p>

Tests are kept in a separate `test` folder in the top-level of the repo. Tests are organized by brick type and namespace:

```
▾ workspace
  ▾ test
    ▾ bases
      ▾ cpackard
        ▾ api
          __init__.py
          test_views.py
    ▾ components
      ▾ cpackard
        ▸ choices
        ▾ questions
          __init__.py
          test_core.py
```

</p>
</details>

## Development

### Adding a new component

You can create a new component using the project's command:

```shell
poetry poly create component --name questions
```

For more info on other commands, see the [Python Polylith docs](https://davidvujic.github.io/python-polylith-docs/commands/).

### Create migrations

Migrations can be created for any components by running the `makemigrations` command for it from the root of the repo:

```shell
python manage.py makemigrations questions
```

Then apply the migrations as normal:

```shell
python manage.py migrate
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
pytest -v
```

By default, this command will use the `DJANGO_SETTINGS_MODULE = "cpackard.api.settings"` attribute in the root-level `pyproject.toml`. You can override this by setting a `DJANGO_SETTINGS_MODULE` environment variable or by passing the `--ds` CLI flag like `pytest --ds=cpackard.api.settings`. See the [pytest-django docs](https://pytest-django.readthedocs.io/en/latest/configuring_django.html#) for more info.
