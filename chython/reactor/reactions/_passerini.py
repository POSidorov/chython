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
    'name': 'Passerini Reaction',
    'description': 'Reaction of carboxylic acid, carbonyl compound and isocyanide to α-hydroxy carboxamides',
    'templates': [
        {
            'A': [
                #R-COOH
                '[O;D1;x0;z1:2][C;D3;x2;z2:1]=[O;x0;z2:3]'
            ],
            'B': [
                #Aldehyde
                '[O;z2;x0:4]=[C;D2;x1;z2:5]'
            ],
            'C': [
                #Isocyanides
                '[C-;D1;x1;z3:6]#[N+;D2;x0;z3:7]'
            ],
            'product': '[A:1](=[A:2])[A:4][A:5][A:6](=[A:3])[A:7]',
            'alerts': [],
            'ufe': {
                'A': '[A:1][A:3]',
                'B': '[A:4][A:5]',
                'C': '[A:6][A:7]'
            }
        }
    ],
    'alerts':[]
}
