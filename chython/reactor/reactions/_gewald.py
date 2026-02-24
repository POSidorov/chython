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
    'name':'Gewald Aminothiophene Synthesis',
    'description': 'Synthesis of 2-aminothiophenes using sulfur, an α-methylene carbonyl and α-cyanoester',
    'templates': [
        {
            'A': [
                # α-Methylene carbonyl
                '[O;D1;z2:1]=[C;z2:2][C;D2;x0;z1:3]'
            ],
            'B': [
                # α-Cyanoester
                '[C;D2;x0;z1:4]([C;x2;z2;M](=[O;M])[O;M])[C;x1;z3:5]#[N;x0;z3:6]'
            ],
            'C': [
                # Sulfur-S8
                '[S;D2;x2;z1;r8:7]([S;D2;x2;z1:8])[S;D2;x2;z1:9]'
            ],
            'product': '[A:3]1=[A:2][A:4]=[A:5]([A:6])[A:7]1',
            'alerts': [],
            'ufe': {
                'A': 1,
                'B': '[A:6][At;M]',
                'C': 8
            }
        }
    ],
    'alerts': []
}
