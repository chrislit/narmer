# -*- coding: utf-8 -*-
"""narmer.phonetic

The phonetic module implements phonetic algorithms including:
    german_ipa


Copyright 2015 by Christopher C. Little.
This file is part of Narmer.

Narmer is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Narmer is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Narmer. If not, see <http://www.gnu.org/licenses/>.
"""

from __future__ import unicode_literals
from __future__ import division
from abydos._compat import _unicode, _range
import unicodedata


def german_ipa(word):
    """Return the IPA transcription of a German word

    Arguments:
    word -- the German word to transcribe to IPA

    Description:
    This is based largely on the orthographic mapping described at:
    https://en.wikipedia.org/wiki/German_orthography

    No significant attempt is made to accomodate loanwords.
    """
    # pylint: disable=too-many-branches
    _vowels = frozenset('AEIOUYÄÖÜ')

    word = unicodedata.normalize('NFKC', _unicode(word.upper()))
    word = word.replace('ß', 'SS')

    # word = ''.join([c for c in word if c in
    #                 frozenset('ABCDEFGIKLMNOPQRSTUVXYZ')])

    ipa = ''
    last = len(word)-1
    skip = 0
    for i in _range(len(word)):
        if skip:
            skip -= 1
            continue

        # Consonants
        if word[i] in frozenset('BFJKLMR'):
            ipa += word[i].lower()
        elif word[i] == 'C':
            if word[i:i+2] == 'CH':
                if word[i:i+3] == 'CHS':
                    ipa += 'ks'
                    skip = 2
                elif word[i:i+4] == 'CHEN':
                    ipa += 'ç'
                    skip = 1
                elif i-1 >= 0 and word[i-1] in frozenset('AOU'):
                    ipa += 'x'
                    skip = 1
                else:
                    ipa += 'ç'
                    skip = 1
            elif word[i:i+2] == 'CK':
                ipa += 'k'
                skip = 1
            elif i != last and word[i+1] in frozenset('ÄEI'):
                ipa += 'ts'
            else:
                ipa += 'k'
        elif word[i] == 'D':
            if word[i:i+4] == 'DSCH':
                ipa += 'dʒ'
                skip = 3
            elif word[i:i+2] == 'DT':
                ipa += 't'
                skip = 1
            else:
                ipa += 'd'
        elif word[i] == 'G':
            if i-1 >= 0 and word[i-1] == 'I':
                ipa += 'ç'
            else:
                ipa += 'g'
        elif word[i] == 'H':
            # H after vowels should already be covered by the vowel rules
            ipa += 'h'
        elif word[i] == 'N':
            if word[i:i+2] == 'NG':
                ipa += 'ŋ'
                skip = 1
            elif word[i:i+2] == 'NK':
                ipa += 'ŋk'
                skip = 1
            else:
                ipa += 'n'
        elif word[i] == 'P':
            if word[i:i+2] == 'PH':
                ipa += 'f'
                skip = 1
            else:
                ipa += 'p'
        elif word[i] == 'Q':
            if word[i:i+2] == 'QU' and i+1 != last and word[i+2] in _vowels:
                ipa += 'kv'
                skip = 1
            else:
                ipa += 'k'
        elif word[i] == 'S':
            if word[i:i+2] == 'SS':
                ipa += 's'
                skip = 1
            elif word[i:i+3] == 'SCH':
                ipa += 'ʃ'
                skip = 2
            elif i == 0 and i != last and word[i+1] in frozenset('PT'):
                ipa += 'ʃ'
            elif i != last and word[i+1] in _vowels:
                ipa += 'z'
            else:
                ipa += 's'
        elif word[i] == 'T':
            if word[i:i+4] == 'TSCH':
                ipa += 'tʃ'
                skip = 3
            elif word[i:i+5] == 'TZSCH':
                ipa += 'tʃ'
                skip = 4
            elif (word[i:i+4] == 'TION' or word[i:i+4] == 'TIÄR' or
                  word[i:i+4] == 'TIAL' or word[i:i+5] == 'TIELL'):
                ipa += 'tsi'
                skip = 1
            elif word[i:i+2] == 'TZ':
                ipa += 'ts'
                skip = 1
            elif word[i:i+2] == 'TH':
                ipa += 't'
                skip = 1
            else:
                ipa += 't'
        elif word[i] == 'V':
            ipa += 'f'
        elif word[i] == 'W':
            ipa += 'v'
        elif word[i] == 'X':
            ipa += 'ks'
        elif word[i] == 'Z':
            if word[i:i+4] == 'ZSCH':
                ipa += 'tʃ'
                skip = 3
            else:
                ipa += 'ts'

        # Vowels -- little attention is paid to length or tenseness
        # -Diphthongs first
        elif word[i:i+2] in frozenset(['EI', 'AI', 'EY', 'AY']):
            ipa += 'ai'
            skip = 1
        elif word[i:i+2] in frozenset(['EU', 'ÄU']):
            ipa += 'oy'
            skip = 1
        elif word[i:i+2] == 'AU':
            ipa += 'au'
            skip = 1

        # -Monophthongs following
        elif word[i] == 'A':
            if word[i:i+2] in frozenset(['AA', 'AH']):
                skip = 1
            ipa += 'a'
        elif word[i] == 'E':
            if word[i:i+2] in frozenset(['EE', 'EH']):
                skip = 1
            ipa += 'e'
        elif word[i] == 'I':
            if word[i:i+2] in frozenset(['IE', 'IH']):
                skip = 1
            if word[i:i+3] == 'IEH':
                skip = 2
            ipa += 'i'
        elif word[i] == 'O':
            if word[i:i+2] in frozenset(['OO', 'OH']):
                skip = 1
            ipa += 'o'
        elif word[i] == 'U':
            if word[i:i+2] == 'UH':
                skip = 1
            ipa += 'u'
        elif word[i] == 'Y':
            ipa += 'y'
        elif word[i] == 'Ä':
            if word[i:i+2] == 'ÄH':
                skip = 1
            ipa += 'e'
        elif word[i] == 'Ö':
            if word[i:i+2] == 'ÖH':
                skip = 1
            ipa += 'ø'
        elif word[i] == 'Ü':
            if word[i:i+2] == 'ÜH':
                skip = 1
            ipa += 'y'

    return ipa
