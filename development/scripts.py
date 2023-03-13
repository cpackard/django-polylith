# Standard Library
import argparse
import subprocess


def create_component() -> None:
    """Create a new component."""
    parser = argparse.ArgumentParser(description="Create a new component.")
    parser.add_argument("name", type=str, help="the name of the new component")

    comp_name = parser.parse_args().name
    comp_src = f"components/{comp_name}/src"

    subprocess.run(["mkdir", "-p", comp_src])
    subprocess.run(["poetry", "run", "python", "manage.py", "startapp", comp_name, comp_src])
    subprocess.run(
        ["cd", f"components/{comp_name}", "&&", "poetry", "config", "virtualenvs.create", "false", "--local"],
        shell=True,
    )

    print(f"\nSuccessfully created new component `{comp_name}` in components/{comp_name}.")
    print("\n Be sure to add the following lines to the root pyproject.toml file:")
    print("\nIn the `packages` attribute of [tool.poetry]:")
    print(f'\n\t{{ include = "{comp_name}", from = "./components/{comp_name}/src/" }}')
    print("\nIn the [tool.poetry.dependencies] section:")
    print(f'\n\t{comp_name} = {{ path = "components/{comp_name}," develop = true }}')
    print("\n")
