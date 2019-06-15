
# Master Mold

A master mold for all Python packages.

![MASTER MOLD](https://repository-images.githubusercontent.com/186540545/4b451280-762b-11e9-8013-2464b596792c) 

The idea is to reduce the tedious work necessary to keep all (of my) packages up-to-date
with the features and/or best practices for packaging.

To do so, it uses [Copier](https://github.com/jpscaletti/copier).


## Usage

To use this master mold for a new or an existing project:

1. Copy the `mm.py` to the project folder.
2. Edit the file and customized with the individual project data.
3. When it's ready, install [Copier](https://github.com/jpscaletti/copier); and
4. Run `python mm.py` to auto-generate the packaging files.

When you want to change the package data, change them in the `mm.py` file, **not** in the auto-generated files, and then run `python mm.py` to update them.

I repeat: **do not edit the auto-generated files, just the data in the `mm.py` file**, or you'll loose those changes.


## FIN
