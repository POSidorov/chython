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
    'name' : 'Knorr Quinoline Synthesis',
    'description': 'Anilines and β-keto esters to 2-hydroxyquinoline',
    'templates' : [
        {
            'A': [
                # Ar-NH2
                '[N;D1;x0;z1:1][C;a;M]:[C;a;D2:2]'
            ],
            'B': [
                # ß-ketoester
                '[O;z2;x0:8]=[C;D3;x1;z2:7][C;x0;z1:6][C;D3;x2;z2:4](=[O:3])[O;D2;x0:5]'
            ],
            'product': '[A:1]=[A:4]([A:3])[A:6]=[A:7][A:2]',
            'alerts': [],
            'ufe': {
                'A': '[A:1][A:2]',
                'B': '[A:5][A:8]'
            }
        }
    ],
    'alerts': []
}
