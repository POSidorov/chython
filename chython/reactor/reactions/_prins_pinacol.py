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
    'name': 'Prins Pinacol Rearrangement',
    'description': 'Substituted Alkene and aldehyde in the presence of a Lewis acid to form a cyclic compound',
    'templates': [
        {
            'A': [
                # Alk-OH-C=C
                '[O;D1;x0;z1:1][C;x1;z1;M][C;x0;z1;M][C;x0;z2:2](=[C;x0;z2:3])[C;D4;x1;z1:4]([C;x0;z1:6])[O;D1;x0;z1:5]',
                # Ar-OH-C=C
                '[O;D1;x0;z1:1][C;x1;z1;M][C;x0;z1;M][C;x0;z2:2](=[C;x0;z2:3])[C;D4;x1;z1:4]([C;a:6])[O;D1;x0;z1:5]'
            ],
            'B' : [
                # Ar-CHO
                '[O;x0;z2:8]=[C;D2;x1;z2:7][C;a;M]'
            ],
            'product':'[A:1][A:7][A:3][A:2]([A:6])[A:4]=[A:5]',
            'alerts':[],
            'ufe': {
                'A': '[A:1][A:3][A:5]',
                'B': 8
            }
        }
    ],
    'alerts':[]
}
