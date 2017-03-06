# Guía para sincronizar un fork con el repositorio original

1. Añadir rama remota del repositorio original:

  * `git remote add upstream <ssh_repositorio>`.


*  `git fetch upstream`.


*  `git checkout master`.


* Hacer un merge de `upstream/master`a nuestra rama `master` local. Esto sincroniza nuestra rama master del fork local con el repositorio original, sin perder los cambios realizados en local.

  * `git merge upstream/master`.
