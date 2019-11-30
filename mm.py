#!/usr/bin/env python
"""
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
    "extra_classifiers": [],

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


def do_the_thing():
    import hecto

    hecto.copy(
        # "gh:jpscaletti/mastermold.git",
        "../mastermold",  # Path to the local copy of Master Mold
        ".",
        data=data,
        force=False,
        exclude=[
            ".*"
            ".*/*"
            ".*/**/*"
            "README.md"
        ],
    )


if __name__ == "__main__":
    do_the_thing()
