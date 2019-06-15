#!/usr/bin/env python
"""
COPY THIS FILE TO YOUR PROJECT.
---------
This file generates all the necessary files for packaging for the project.
Read more about it at https://github.com/jpscaletti/mastermold/
"""
from pathlib import Path

import copier
from ruamel.yaml import YAML


data = {
    "title": "Master Mold",
    "name": "mastermold",
    "pypi_name": "mastermold",
    "version": "1.0",
    "author": "Juan-Pablo Scaletti",
    "author_email": "juanpablo@jpscaletti.com",
    "description": "Lorem ipsum sit amet.",
    "repo_name": "jpscaletti/mastermold",
    "home_url": "",
    "docs_url": "",
    "install_requires": [
        "foo",
        "bar",
    ],
    "entry_points": "",
    "coverage_omit": [
        "foo",
    ],
    "google_analytics": "UA-XXXXXXXX-X",
    "docs_nav": [],  # Overwritten by `save_current_nav`.
}


def save_current_nav():
    yaml = YAML()
    mkdocs_path = Path("docs") / "mkdocs.yml"
    if not mkdocs_path.exists():
        return
    mkdocs = yaml.load(mkdocs_path)
    data["docs_nav"] = mkdocs.get("nav")


def do_the_thing():
    save_current_nav()
    copier.copy(
        "gh:jpscaletti/mastermold.git",
        ".",
        data=data,
        exclude=[
            "README.md",
            ".git",
            ".git/*",
            ".venv",
            ".venv/*",
        ],
        force=True,
        cleanup_on_error=False
    )


if __name__ == "__main__":
    do_the_thing()
