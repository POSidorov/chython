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
    'name': 'Pictet–Spengler Reaction',
    'description': 'β-arylethylamine undergoes condensation with an aldehyde or ketone followed by ring closure',
    'templates': [
        {
            'A': [
                # β-arylethylamine
                '[N;D1,D2;x0;z1:1][C;x1;z1;M][C;x0;z1;M][C;a;M]:[C;a;D2:2]'
            ],
            'B': [
                # Carbonyl
                '[O;z2;x0:3]=[C;D1,D2,D3;x1;z2:4]'
            ],
            'product': '[A:2][A:4]-[A:1]',
            'alerts': [],
            'ufe': {
                'A': 1,
                'B': '[A:3]'
            }
        }
    ],
    'alerts': []
}
