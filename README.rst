narmer
======

To build/install/unittest in Python 2:
sudo python setup.py install; nosetests -v --with-coverage --cover-erase --cover-html --cover-branches --cover-package=narmer .

To build/install/unittest in Python 3:
sudo python3 setup.py install; nosetests3 -v --with-coverage --cover-erase --cover-html --cover-branches --cover-package=narmer .


For pylint testing, run:
pylint --rcfile=pylint.rc narmer > pylint.log


