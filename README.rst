Narmer
======

.. image:: https://travis-ci.org/chrislit/narmer.svg
    :target: https://travis-ci.org/chrislit/narmer

.. image:: https://coveralls.io/repos/chrislit/narmer/badge.svg
    :target: https://coveralls.io/r/chrislit/narmer
    :alt: Coverage Status

.. image:: https://codeclimate.com/github/chrislit/narmer/badges/gpa.svg
   :target: https://codeclimate.com/github/chrislit/narmer
   :alt: Code Climate

.. image:: https://img.shields.io/badge/Pylint-9.71/10-green.svg
    :alt: Pylint Score

.. image:: https://img.shields.io/badge/PEP8-0-brightgreen.svg
    :alt: PEP8 Errors

.. image:: https://readthedocs.org/projects/narmer/badge/?version=latest
    :target: https://readthedocs.org/projects/narmer/?badge=latest
    :alt: Documentation Status

Narmer NLP/IR library
Copyright 2015 by Christopher C. Little

This library contains code I'm using for research, in particular dissertation research & experimentation.

Suggested for testing & QA

- Nose        (for unit testing)
- coverage.py (for code coverage checking)
- Pylint      (for code quality checking)
- PEP8        (for code quality checking)

-----

To build/install/unittest in Python 2:

::

    sudo python setup.py install
    nosetests -v --with-coverage --cover-erase --cover-html --cover-branches --cover-package=abydos .

To build/install/unittest in Python 3:

::

    sudo python3 setup.py install
    nosetests3 -v --with-coverage --cover-erase --cover-html --cover-branches --cover-package=abydos .

For pylint testing, run:

::

    pylint --rcfile=pylint.rc abydos > pylint.log
