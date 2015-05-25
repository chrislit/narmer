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

"""narmer.tests.test_stats

This module contains unit tests for narmer.stats
"""

from __future__ import unicode_literals
import unittest
from narmer.stats import weissman
import math


class WeissmanTestCases(unittest.TestCase):
    """test cases for abydos.stats.weissman
    """
    def test_weissman(self):
        """test abydos.stats.weissman
        """
        self.assertRaises(ValueError, weissman, 0, 1, 1, 1)
        self.assertRaises(ValueError, weissman, 1, 0, 1, 1)
        self.assertRaises(ValueError, weissman, 1, 1, 0, 1)
        self.assertRaises(ValueError, weissman, 1, 1, 1, 0)

        self.assertEqual(weissman(1, math.e, 1, math.e), 1.0)
        self.assertEqual(weissman(1, 5, 1, 5), 1.0)

        self.assertEqual(weissman(1, 1, 1, 1), 1.0)
        self.assertEqual(weissman(1, 1, 1, 1, 2), 2.0)

        self.assertAlmostEqual(weissman(1, 1, 1, math.e), 4503599627370497)

        self.assertAlmostEqual(weissman(2.53, 57.06, 1.23, 23),
                               1.5947740798552632)


if __name__ == '__main__':
    unittest.main()
