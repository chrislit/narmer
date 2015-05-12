#!/bin/sh

sudo rm -rf ./build
python setup.py build
sudo python setup.py install

sudo rm -rf ./build
python3 setup.py build
sudo python3 setup.py install

sudo python setup.py install
sudo python3 setup.py install

nosetests -v --with-coverage --cover-erase --cover-html --cover-branches --cover-package=narmer .
nosetests3 -v --with-coverage --cover-erase --cover-html --cover-branches --cover-package=narmer .

pylint --rcfile=pylint.rc narmer > pylint.log
pep8 -v --statistics --exclude=.git,__pycache__,build . > pep8.log

./badge_update.py
