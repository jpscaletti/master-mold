#!/usr/bin/env python
"""
COPY THIS FILE TO YOUR PROJECT.
---------
This file generates all the necessary files for packaging for the project.
Read more about it at https://github.com/jpscaletti/mastermold/
"""
from pathlib import Path


data = {
    "title": "Master Mold",
    "name": "mastermold",
    "pypi_name": "mastermold",
    "version": "1.0",
    "author": "Juan-Pablo Scaletti",
    "author_email": "juanpablo@jpscaletti.com",
    "description": "Lorem ipsum sit amet.",
    "copyright": "2019",
    "repo_name": "jpscaletti/mastermold",
    "home_url": "",
    # Displayed in the pypi project page
    "project_urls": {
        "Documentation": "",
    },

    "development_status": "4 - Beta",
    "minimal_python": 3.6,
    "install_requires": [
    ],
    "testing_requires": [
        "pytest",
        "pytest-cov",
    ],
    "development_requires": [
        "pytest-flake8",
        "flake8",
        "ipdb",
        "tox",
    ],
    "entry_points": "",

    "coverage_omit": [
    ],

    "has_docs": True,
    "google_analytics": "UA-XXXXXXXX-X",
}

exclude = [
    "copier.yml",
    "README.md",
    ".git",
    ".git/*",
    ".venv",
    ".venv/*",
]


def do_the_thing():
    import copier
    from ruamel.yaml import YAML

    def save_current_nav():
        yaml = YAML()
        mkdocs_path = Path("docs") / "mkdocs.yml"
        if not mkdocs_path.exists():
            return
        mkdocs = yaml.load(mkdocs_path)
        nav = list(filter(None, mkdocs.get("nav") or []))
        data["docs_nav"] = nav or ["index.md"]

    if data["has_docs"]:
        save_current_nav()
    else:
        data["docs_nav"] = []

    copier.copy(
        # "gh:jpscaletti/mastermold.git",
        "../mastermold",  # Path to the local copy of Master Mold
        ".",
        data=data,
        exclude=exclude,
        force=True,
        cleanup_on_error=False
    )


if __name__ == "__main__":
    do_the_thing()
