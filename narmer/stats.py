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

"""narmer.stats

The stats module defines functions for calculating various statistical data
about linguistic objects, including:

    - Weissman score calculation
"""

from __future__ import unicode_literals
from __future__ import division
import math
import sys


def weissman(r_tar, t_tar, r_src, t_src, alpha=1.0):
    """Weissman score based on entered statistics

    The score is:
    :math:`W = α \\cdot \\frac{r_{tar}}{r_{src}} \\cdot
    \\frac{log t_{src}}{log t_{tar}}`

    In practice, the score can be used to rate time-intensive tasks on the
    basis of other metrics, also, e.g. :math:`F_1` score.

    Sources:
    http://spectrum.ieee.org/view-from-the-valley/computing/software/a-madefortv-compression-metric-moves-to-the-real-world

    :param float r_tar: the target algorithm's compression ratio
    :param float t_tar: the target algorithm's compression time
    :param float r_src: a standard algorithm's compression ratio
    :param float t_src: a standard algorithm's compression time
    :param float alpha: a scaling constant (1.0 by default)
    :returns: the Weissman score
    :rtype: float
    """
    if t_tar <= 0 or t_src <= 0:
        raise ValueError("Compression times must be positive values.")
    elif r_tar <= 0 or r_src <= 0:
        raise ValueError("Compression ratios must be positive values.")
    elif t_src == t_tar:
        return alpha * (r_tar / r_src)
    elif t_tar == 1:
        # if t_tar == 1, add epsilon to avoid division by log(1) = 0
        t_tar += sys.float_info.epsilon

    if r_src == r_tar:
        return alpha * (math.log(t_src) / math.log(t_tar))
    else:
        return alpha * (r_tar / r_src) * (math.log(t_src) / math.log(t_tar))
