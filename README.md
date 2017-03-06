# Guía para sincronizar un fork con el repositorio original

1. Añadir rama remota del repositorio original:

  * `git remote add upstream <ssh_repositorio>`.

2. `git fetch upstream`.

3. `git checkout master`.

4. Hacer un merge de `upstream/master`a nuestra rama `master` local. Esto sincroniza nuestra rama master del fork local con el repositorio original, sin perder los cambios realizados en local.

  * `git merge upstream/master`.

#### Script.py
[@Chinegua](https://github.com/Chinegua) ha desarrollado un script que automatiza los pasos anteriores, usando el lenguaje Python3.
