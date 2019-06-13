
# Master Mold

A master mold for all Python packages.

The idea is to reduce the tedious work necessary to keep all (of my) packages up-to-date
with the features and/or best practices for packaging.


## Usage (new)

To use this master mold for a new project, simply pull it into a new project:

```bash
$ git init my-new-project
$ cd my-new-project
$ git pull git@github.com:jpscaletti/mastermold.git
```

Now customize the project to suit your individual project needs.


## Usage (existing)

For existing projects, you can still incorporate the master mold by adding its repo as a remote and then merging the branch it into the codebase.

```bash
$ git remote add mastermold git@github.com:jpscaletti/mastermold.git
$ git remote update
$ git merge --allow-unrelated-histories mastermold/master
```

The `--allow-unrelated-histories` is necessary because the history from the master mold is unrelated to the existing codebase.

Resolve any merge conflicts and commit to the master, and now the project is based on the shared skeleton.


## Updating

Now, whenever a change is needed or desired for the general technique for packaging, it can be made in the master mold project and then merged into the each of the derived projects as needed.


## FIN

**NOTE:** I shamelessly stole this idea from Jason Coombs https://github.com/jaraco/skeleton . And I would do it again!
