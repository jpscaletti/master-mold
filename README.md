
# Master Mold

A master mold for all Python packages.

The idea is to reduce the tedious work necessary to keep all (of my) packages up-to-date
with the features and/or best practices for packaging.

---
**NOTE:** I'm not happy. I don't think this approach works very well for existing projects (my main concern).
I'm going to try something using [Copier](https://github.com/jpscaletti/copier).

---

## New projects

To use this master mold for a new project, simply pull it into a new project:

```bash
$ git init my-new-project
$ cd my-new-project
$ git pull git@github.com:jpscaletti/mastermold.git
```

Now customize the project to suit your individual project needs.


## Update existing projects

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
