# -*- coding: utf-8 -*-

# Copyright 2015-2018 by Christopher C. Little.
# This file is part of Narmer.
#
# Narmer is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Narmer is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Abydos. If not, see <http://www.gnu.org/licenses/>.

"""setup.py.

setuptools configuration file for Narmer
"""

from codecs import open
from os import path

from setuptools import find_packages, setup

HERE = path.abspath(path.dirname(__file__))


def readfile(fn):
    """Read fn and return the contents."""
    with open(path.join(HERE, fn), 'r', encoding='utf-8') as f:
        return f.read()


setup(
      name='narmer',
      packages=find_packages(exclude=['tests*']),
      version='0.1.2',
      description='Narmer Experimental NLP/IR library for Python',
      author='Christopher C. Little',
      author_email='chrisclittle+narmer@gmail.com',
      url='https://github.com/chrislit/narmer',
      download_url='https://github.com/chrislit/narmer/archive/master.zip',
      keywords=['nlp', 'ai', 'ir', 'language', 'linguistics',
                'phonetic algorithms'],
      license='GPLv3+',
      classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Development Status :: 3 - Alpha',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU General Public License v3 or later \
(GPLv3+)',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Indexing',
        'Topic :: Text Processing :: Linguistic',
        ],
      long_description='\n\n'.join([readfile(f) for f in ('README.rst',
                                                          'HISTORY.rst',
                                                          'AUTHORS.rst')]),
      install_requires=['six'],
      )
