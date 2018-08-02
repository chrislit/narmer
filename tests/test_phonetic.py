# -*- coding: utf-8 -*-

# Copyright 2015 by Christopher C. Little.
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
# along with Narmer. If not, see <http://www.gnu.org/licenses/>.

"""narmer.tests.test_phonetic.

This module contains unit tests for narmer.phonetic
"""

from __future__ import unicode_literals

import unittest

from narmer.phonetic import german_ipa


class GermanIPATestCases(unittest.TestCase):
    """Test abydos.phonetic.german_ipa."""

    def test_german_ipa(self):
        """Test abydos.phonetic.german_ipa."""
        self.assertEqual(german_ipa(''), '')

        # https://en.wikipedia.org/wiki/German_orthography
        self.assertEqual(german_ipa('Wasser'), 'vaser')
        self.assertEqual(german_ipa('Männer'), 'menner')
        self.assertEqual(german_ipa('Bett'), 'bett')
        self.assertEqual(german_ipa('Ochse'), 'okse')
        self.assertEqual(german_ipa('Mittel'), 'mittel')
        self.assertEqual(german_ipa('kommen'), 'kommen')
        self.assertEqual(german_ipa('Göttin'), 'gøttin')
        self.assertEqual(german_ipa('Mutter'), 'mutter')
        self.assertEqual(german_ipa('Müller'), 'myller')
        self.assertEqual(german_ipa('Dystrophie'), 'dystrofi')
        self.assertEqual(german_ipa('bot'), 'bot')
        self.assertEqual(german_ipa('Wagen'), 'vagen')
        self.assertEqual(german_ipa('Boot'), 'bot')
        self.assertEqual(german_ipa('Weh'), 've')

        # etc. (for code coverage)
        self.assertEqual(german_ipa('Mädchen'), 'medçen')
        self.assertEqual(german_ipa('Achtung'), 'axtuŋ')
        self.assertEqual(german_ipa('ich'), 'iç')
        self.assertEqual(german_ipa('Backofen'), 'bakofen')
        self.assertEqual(german_ipa('cent'), 'tsent')
        self.assertEqual(german_ipa('Chemie'), 'çemi')
        self.assertEqual(german_ipa('Canada'), 'kanada')
        self.assertEqual(german_ipa('Dschungel'), 'dʒuŋel')
        self.assertEqual(german_ipa('Gerhardt'), 'gerhart')
        self.assertEqual(german_ipa('lustig'), 'lustiç')
        self.assertEqual(german_ipa('Enkelkind'), 'eŋkelkind')
        self.assertEqual(german_ipa('Potsdam'), 'potsdam')
        self.assertEqual(german_ipa('Quatsch'), 'kvatʃ')
        self.assertEqual(german_ipa('Qu\'ran'), 'kuran')
        self.assertEqual(german_ipa('Iraq'), 'irak')
        self.assertEqual(german_ipa('schon'), 'ʃon')
        self.assertEqual(german_ipa('Fisch'), 'fiʃ')
        self.assertEqual(german_ipa('Spitze'), 'ʃpitse')
        self.assertEqual(german_ipa('Stimme'), 'ʃtimme')
        self.assertEqual(german_ipa('Nietzsche'), 'nitʃe')
        self.assertEqual(german_ipa('nationelle'), 'natsionelle')
        self.assertEqual(german_ipa('exponentiell'), 'eksponentsiell')
        self.assertEqual(german_ipa('Thüringen'), 'tyriŋen')
        self.assertEqual(german_ipa('Bezsch'), 'betʃ')
        self.assertEqual(german_ipa('Zimmer'), 'tsimmer')
        self.assertEqual(german_ipa('Eichhorn'), 'aiçhorn')
        self.assertEqual(german_ipa('Löwenbräu'), 'løvenbrøy')
        self.assertEqual(german_ipa('graue'), 'graue')
        self.assertEqual(german_ipa('singen'), 'ziŋen')
        self.assertEqual(german_ipa('Volk'), 'folk')
        self.assertEqual(german_ipa('Haar'), 'har')
        self.assertEqual(german_ipa('Vieh'), 'fi')
        self.assertEqual(german_ipa('Kuh'), 'ku')
        self.assertEqual(german_ipa('Kuchen'), 'kuçen')
        self.assertEqual(german_ipa('äh'), 'e')
        self.assertEqual(german_ipa('Klöh'), 'klø')
        self.assertEqual(german_ipa('Küh-Bach'), 'kybax')
        self.assertEqual(german_ipa('Frohe'), 'froe')
        self.assertEqual(german_ipa('ohne'), 'one')


if __name__ == '__main__':
    unittest.main()
