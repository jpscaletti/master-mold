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
    "development_status": "4 - Beta",
    "minimal_python": 3.6,
    "install_requires": [
        "foo",
        "bar",
    ],
    "test_requires": [
        "pytest",
        "pytest-cov",
        "pytest-flake8",
        "flake8",
        "ipdb",
        "tox",
    ],
    "entry_points": "",

    "coverage_omit": [
        "foo",
    ],

    "copyright": "2019",
    "has_docs": True,
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
    if data["has_docs"]:
        save_current_nav()

    copier.copy(
        "gh:jpscaletti/mastermold.git",
        ".",
        data=data,
        exclude=[
            "copier.yml",
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
