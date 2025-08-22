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
    'name': 'Biginelli Reaction',
    'description': 'Reaction of aldehyde, thio urea, and acetoacetate to pyrimidines',
    'templates' : [
        {
            'A':  [
                #Ar-CHO
                '[O;z2;x0:1]=[C;D2;x1;z2:2][C;a;M]'
            ],
            'B':  [
                #Urea
                '[N;D1;x0;z1:3][C;D3;x3;z2:4](=[O,S;M])[N;D1;x0;z1:5]',  
            ],
            'C':  [
                #β-Dicarbonyl
                '[O;z2;x0:6]=[C;D3;x1;z2:7][C;D2;x0;z1:8][C;D3;x2;z2;M](=[O;z2;x0;M])[O;D2;x0;M]',
                #Cyclohexane-1,3-dione
                '[O;x0;z2:6]=[C;D3;x1;z2:7][C;D2;x0;z1:8][C;D3;x1,x2;z2;r6;M]=[O;x0;z2;M]'
            ],
            'product': '[A:2]1[A:3][A:4][A:5][A:7]=[A:8]1',
            'alerts': [],
            'ufe': {
                'A': '[A:1][A:2]',
                'B': '[A:3][A:4][A:5]',
                'C': '[A:6][A:7][A:8]'
            }
        }
    ],
    'alerts': []
}