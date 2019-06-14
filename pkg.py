#!/usr/bin/env python
import copier


data = {
    "title": "[[ title ]]",
    "name": "[[ name ]]",
    "version": "[[ version ]]",
    "author": "[[ author ]]",
    "author_email": "[[ author_email ]]",
    "description": "[[ description ]]",
    "repo_name": "[[ repo_name ]]",
    "home_url": "[[ home_url ]]",
    "docs_url": "[[ docs_url ]]",
    "install_requires": "[[ install_requires ]]",
    "entry_points": "[[ entry_points ]]",
    "coverage_omit": "[[ coverage_omit ]]",
    "google_analytics": "[[ google_analytics ]]",
    "docs_nav": "[[ docs_nav ]]",
}


def do_the_thing():
    copier.copy(
        "gh:jpscaletti/mastermold.git",
        ".",
        data=data,
        force=True,
        cleanup_on_error=False
    )


if __name__ == "__main__":
    do_the_thing()
