# Standard Library
import argparse
import subprocess

# Third-Party Libraries
import toml


def _create_parent_directories(src_folder: str, test_folder: str) -> None:
    subprocess.run(["mkdir", "-p", src_folder])
    subprocess.run(["mkdir", "-p", test_folder])


def _generate_readme(component_name: str) -> None:
    readme_text = """
# {component_name} Component

    """
    with open(f"components/{component_name}/README.md", "w") as f:
        f.write(readme_text)


def _create_component_toml(component_name: str) -> None:
    component_toml = f"""
[tool.poetry]
name = "{component_name}"
version = "0.1.0"
description = "{component_name} component."
authors = ["Example Author <author@example.com>"]
readme = "README.md"
packages = [ {{ include = "{component_name}", from = "./src" }} ]

[tool.poetry.dependencies]
python = "^3.11"
    """
    parsed_toml = toml.loads(component_toml)
    with open(f"components/{component_name}/pyproject.toml", "w") as comp_f:
        toml.dump(parsed_toml, comp_f)

    config_toml = """
[virtualenvs]
create = false
    """
    config_parsed = toml.loads(config_toml)
    with open(f"components/{component_name}/poetry.toml", "w") as config_f:
        toml.dump(config_parsed, config_f)


def _update_development_toml(component_name: str) -> None:
    dev_toml = toml.load("pyproject.toml")
    dev_toml["tool"]["poetry"]["dependencies"][component_name] = {
        "path": f"components/{component_name}",
        "develop": True,
    }
    with open("pyproject.toml", "w") as f:
        toml.dump(dev_toml, f)


def create_component() -> None:
    """Create a new component."""
    parser = argparse.ArgumentParser(description="Create a new component.")
    parser.add_argument("name", type=str, help="the name of the new component")

    comp_name = parser.parse_args().name
    comp_src = f"components/{comp_name}/src/{comp_name}"
    comp_tests = f"components/{comp_name}/tests"

    _create_parent_directories(comp_src, comp_tests)

    # create placeholder test files
    subprocess.run(["touch", f"{comp_tests}/__init__.py", f"{comp_tests}/test_{comp_name}.py"])
    # Django command to generate boilerplate
    subprocess.run(["poetry", "run", "python", "manage.py", "startapp", comp_name, comp_src])
    # Cleanup unnecessary modules
    subprocess.run(["rm", f"{comp_src}/admin.py", f"{comp_src}/tests.py", f"{comp_src}/views.py"])

    _generate_readme(comp_name)
    _create_component_toml(comp_name)
    _update_development_toml(comp_name)

    print(f"\nSuccessfully created new component `{comp_name}` in components/{comp_name}.")
    print(
        "\n To add as a dependency in another brick, add the following in the relevant pyproject.toml file dependencies:"
    )
    print(f'\n\t{comp_name} = {{ path = "components/{comp_name}," develop = true }}\n')
    print(
        f"Finally, add the new component `{comp_name}` to the INSTALLED_APPS of development/settings.py and any relevant project's settings.py"
    )
    print("\n")
