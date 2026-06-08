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
    'name': 'Beckmann Rearrangement',
    'description': 'Aldehyde or Ketone convert to amide',
    'templates': [
        # Ketone
        {
            'A': [
                # Alk-C(=O)-Ar
                '[O;z2;x0;M]=[C;D3;x1;z2:1]([C;z1;M])[C;a:2]',
                # Ar-C(=O)-Ar
                '[O;z2;x0;M]=[C;D3;x1;z2:1]([C;a;M])[C;a:2]',
                # Alk-C(=O)-Subs-Alk
                '[O;z2;x0;M]=[C;D3;x1;z2:1]([C;z1;M])[C;D3;z1:2]',
                # Alk-C(=O)-Alk
                '[O;z2;x0;M]=[C;D3;x1;z2:1]([C;z1;M])[C;z1:2]'
                
            ],
            'B': [
                # NH4OH
                '[N+;z1:3].[O-:4]'
            ],
            'product': '[A:1][A:3][A:2]',
            'alerts': [],
            'ufe':{
                'A': 2,
                'B': 4
            }
        },
        # Aldehyde
        {
            'A': [
                # R-CHO
                '[O;z2;x0;M]=[C;D2;x1;z2:1]'
                
            ],
            'B': [
                # NH4OH
                '[N+;z1:3].[O-:4]'
            ],
            'product': '[A:1][A:3]',
            'alerts': [],
            'ufe':{
                'A': 2,
                'B': 4
            }
        },
    ],
    'alerts':[]
}
