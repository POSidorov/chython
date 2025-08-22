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
    'name': 'Bucherer–Bergs Reaction',
    'description': 'Reaction between carbonyl, potassium cyanide and ammonium carbonate to form hydantoins',
    'templates': [
        {
            'A': [
                #O=CR2
                '[O;x0;z2:2]=[C;x1;z2:1]'
            ],
            'B': [
                #KCN
                '[N;D1:3]#[C-;D1:4].[K+:5]'
            ],
            'C': [
                #(NH4)2CO3
                '[O-:6][C;x3;z2:7](=[O;M])[O-:8].[N+:9].[N+:10]'
            ],
            'product': '[A:1]1[A:4](=[A:6])[A:3][A:7][A:9]1',
            'alerts': [],
            'ufe': {
                'A': 2,
                'B': 5,
                'C': '[A:8][A:10]'
            }
        }
    ],
    'alerts': []
}