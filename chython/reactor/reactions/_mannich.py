# -*- coding: utf-8 -*-
#
#  Copyright 2022-2024 Ramil Nugmanov <nougmanoff@protonmail.com>
#  Copyright 2023 Timur Gimadiev <timur.gimadiev@gmail.com>
#  Copyright 2025 Balasubramaniyan Sakthivel <sakthivelbala.s@gmail.com>
#  This file is part of chython.
#
#  chython is free software; you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program; if not, see <https://www.gnu.org/licenses/>.
#

template = {
    'name': 'Mannich Reaction',
    'description': 'Three-component aminomethylation from amine, aldehyde and acidic methylene moiety',
    'templates': [
        {
            'A': [
                # Acidic methylene
                '[O;z2;x0;M]=[C;D3;x1;z2;M][C;x0;z1:1]'
            ],
            'B': [
                 # Ar-CHO
                '[O;z2;x0:2]=[C;D2;x1;z2:3][C;a;M]',
                # Alkyl-CHO
                '[O;z2;x0:2]=[C;D2;x1;z2:3][C;z1;M]',
                # CH2O
                '[O;z2;x0:2]=[C;D1,D2;x1;z2:3]'
            ],
            'C': [
                # Ar-NH2
                '[N;D1;x0;z1:4][C;a;M]',
                # Alk-NH2
                '[N;D1;x0;z1:4][C;z1;x1;M]',
                # Ar-NH-Ar
                '[N;D2;x0;z1:4]([C;a;M])[C;a;M]',
                # Alk-NH-Ar
                '[N;D2;x0;z1:4]([C;a;M])[C;z1;x1;M]',
                # Alk2NH
                '[N;D2;x0;z1:4]([C;z1;x1;M])[C;z1;x1;M]'
            ],
            'product': '[A:1][A:3][A:4]',
                'alerts': [],
                'ufe': {
                    'A': 1,
                    'B': '[A:2][At;M]',
                    'C': '[A:3][At;M]'
            }
        },
    ],
    'alerts': []
}
