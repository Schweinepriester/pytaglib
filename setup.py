#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2011-2012 Michael Helmling
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation
#
"""Setup file for pytaglib. Type <python setup.py install> to install this package."""
 
import os.path
from setuptools import setup
from Cython.Build import cythonize

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Cython',
    'Topic :: Software Development :: Libraries :: Python Modules',
]


def readme():
    with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as rm:
        return rm.read()


setup(
  name='pytaglib',
  description='TagLib bindings for python 2.x/3.x, written using cython',
  long_description=readme(),
  version='0.2.4',
  license='GPLv3+',
  author='Michael Helmling',
  author_email='helmling@mathematik.uni-kl.de',
  url='http://github.com/supermihi/pytaglib',
  install_requires=['cython>=0.16'],
  ext_modules=cythonize("src/taglib.pyx"),
  scripts=['src/pyprinttags.py'],
  package_dir={'': 'src'},
  test_suite='tests',
)
