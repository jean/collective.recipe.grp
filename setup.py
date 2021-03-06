# -*- coding: utf-8 -*-
"""
This module contains the tool of collective.recipe.grp
"""
import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '1.0'
long_description = (read('README.rst') + '\n' + read('docs/HISTORY.txt'))
entry_point = 'collective.recipe.grp:Recipe'
entry_points = {"zc.buildout": ["default = %s" % entry_point]}
tests_require=['zope.testing', 'zc.buildout']

setup(name='collective.recipe.grp',
      version=version,
      description="A window unto Python's Standard Library grp function",
      long_description=long_description,
      classifiers=[
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: Zope Public License',
        ],
      keywords='',
      author='Alex Clark',
      author_email='aclark@aclark.net',
      url='http://svn.plone.org/svn/collective/buildout/collective.recipe.grp',
      license='ZPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.recipe'],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'zc.buildout'
                        # -*- Extra requirements: -*-
                        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite = 'collective.recipe.grp.tests.test_docs.test_suite',
      entry_points=entry_points,
      )
