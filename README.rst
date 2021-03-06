Introduction
*************

This is a one line recipe to allow buildout users to 
refer to ``${grp:GROUP}`` to get the current user's group.
In other words, the results of ``id -g -n`` on UNIX systems
for the person executing the buildout.
This can be handy in combination with the `gocept.recipe.env`_ recipe,
when setting ownership on the contents of a buildout,
e.g. ``chown -R  ${env:USER}:${grp:GROUP} ${buildout:directory}``.

- Code repository: https://github.com/collective/collective.recipe.grp
- Questions and comments to aclark@aclark.net
- Report bugs to aclark@aclark.net

.. _gocept.recipe.env: http://pypi.python.org/pypi/gocept.recipe.env
