#!/usr/bin/env python
"""
COPY THIS FILE TO YOUR PROJECT.
---------
This file generates all the necessary files for packaging for the project.
Read more about it at https://github.com/jpscaletti/mastermold/
"""
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

    copier.copy(
        # "gh:jpscaletti/mastermold.git",
        "../mastermold",  # Path to the local copy of Master Mold
        ".",
        data=data,
        exclude=exclude,
        force=False,
        cleanup_on_error=False
    )


if __name__ == "__main__":
    do_the_thing()
