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
    'name': 'Perkin Reaction',
    'description': 'Condensation of an aromatic aldehyde and an acid anhydride to α,β-unsaturated aromatic acid',
    'templates': [
            {
            'A': [
                # Ar-CHO
                '[O;z2;x0:1]=[C;D2;x1;z2:2][C;a;M]'
            ],
            'B': [
                # Acid anhydride
                '[C;D1;x0;z1:3][C;x2;z2:4](=[O;M])[O;x0;z1:5][C;x2;z2:6](=[O:7])[C;x0;z1:8]'
            ],
            'product': '[A:2]=[A:3][A:4][A:5]',
            'alerts': [],
            'ufe': {
                'A': '[A:1]',
                'B': '[A:6][A:7]'
            }
        }
    ],
    'alerts': []
}
