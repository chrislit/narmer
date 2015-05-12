# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))


def readfile(fn):
    """Read fn and return the contents."""
    with open(path.join(here, fn), 'r', encoding='utf-8') as f:
        return f.read()

setup(
      name='narmer',
      packages=['narmer'],
      version='0.1.0',
      description='Narmer Experimental NLP/IR library for Python',
      author='Christopher C. Little',
      author_email='chrisclittle@gmail.com',
      url='https://github.com/chrislit/narmer',
      keywords=['nlp', 'ai', 'ir', 'language', 'linguistics',
                'phonetic algorithms'],
      classifiers=[
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 3',
                   'Development Status :: 2 - Pre-Alpha',
                   'Environment :: Other Environment',
                   'Intended Audience :: Developers',
                   'Operating System :: OS Independent',
                   'Topic :: Scientific/Engineering :: Artificial Intelligence',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: Text Processing :: Indexing',
                   'Topic :: Text Processing :: Linguistic',
                   ],
      long_description='\n\n'.join([readfile(f) for f in ('README.rst',
                                                          'HISTORY.rst',
                                                          'AUTHORS.rst')]),
      install_requires=['abydos'],
      )
