
# Master Mold

A master mold for all Python packages.

![MASTER MOLD](https://repository-images.githubusercontent.com/186540545/4b451280-762b-11e9-8013-2464b596792c) 

The idea is to reduce the tedious work necessary to keep all (of my) packages up-to-date
with the features and/or best practices for packaging.

To do so, it uses [Copier](https://github.com/jpscaletti/copier).

---

## New projects

To use this master mold for a new project, simply install copier globally and call it with this repo url:

```bash
copier git@github.com:jpscaletti/mastermold.git my-new-project
```

Answer the cuestions (like its name, a description, the repo URL, etc.) to customize it to your individual project needs.

Among the auto-generated files, you'll find one named `pkg.py`, with your answers to the questions and code to regenerate the packaging files.

When you want to change those values, change them in this file, **not** in the auto-generated files, and then run `python pkg.py` to update them.

I repeat: **do not edit the auto-generated files, just the data in the `pkg.py` file**, or you'll loose those changes.


## Updating existing projects

To update existing projects, just run `python pkg.py`. If the project folder wasn't created originally with this template, just make a new empty project somewhere, copy the `pkg.py` file from there, and update the data.

## FIN
