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
    'name': 'Evans Aldol Reaction',
    'description': 'Aldehyde to aldol using chiral acyl oxazolidinone',
    'templates': [
        {
            'A': [
                #Ar-CHO
                '[O;x0;z2:1]=[C;D2;x1;z2:2][C;a;M]',
                #Alk-CHO
                '[O;z2;x0:1]=[C;D2;x1;z2:2][C;z1;M]'
            ],
            'B': [
                #Acylated oxazolidinones
                '[C;D1,D2;x0;z1:3][C;x2;z2;M](=[O;M])[N;D3;x0;z1;M][C;x3;z2;M;r5]=[O,S;M]'
                
            ],
            'product':'[A:1][A:2]-[A:3]',
            'alerts': [],
            'ufe': {
                'A': 1,
                'B':'[A:3][At;M]'
            }
        },
    ],
    'alerts': []
}