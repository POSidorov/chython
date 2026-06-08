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
    'name': 'Pfitzinger-Borsche Reaction',
    'description': 'Isatin with base and a carbonyl compound to quinoline-4-carboxylic acids',
    'templates': [
        {
            'A': [
                # Isatin
                '[N;D2;x0;z1;r5:1]([C;a;M])[C;D3;x2;z2:2](=[O;M])[C;D3;x1;z2:3]=[O:4]'
            ],
            'B': [
                # α-Methylene carbonyl
                '[O;D1;z2;x0:5]=[C;x1;z2:6][C;D2;x0,x1;z1:7]'
            ],
            'C': [
                # Alk-OH
                '[O;D1;x0;z1:8][C;x1;z1;M]',
                # Base KOH
                '[O-:8].[K+:9]'
                ],
                'product': '[A:1]=[A:6][A:7]=[A:3][A:2][A:8]',
                'alerts': [],
                'ufe': {
                    'A': 4,
                    'B': '[A:5]',
                    'C': '[A:8]'
                }
        }
    ],
    'alerts': []
}
