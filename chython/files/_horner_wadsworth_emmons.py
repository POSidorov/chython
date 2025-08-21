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
    'name': 'Horner Wadsworth Emmons Reaction',
    'description': 'Olefin formation from aldehydes and phosphonates',
    'templates': [
        {
            'A': [
                #Ar-CHO
                '[O;x0;z2:1]=[C;D2;x1;z2:2][C;a;M]',
                #Alk-CHO
                '[O;x0;z2:1]=[C;D2;x1;z2:2][C;z1;M]'
            ],
            'B': [
                #Phosphonate
                '[C;x1;z1:3][O:4][P:5](=O)([O:6][C;x1;z1:7])[C;D2,D3;z1;x1:8][C;z2;x2;M]'
            ],
            'product': '[A:2]=[A:8]',
            'alerts': [],
            'ufe': {
                'A': 1,
                'B':'[A:3][A:4][A:5][A:6][A:7]'
            }
        }
    ],
    'alerts' : []
}