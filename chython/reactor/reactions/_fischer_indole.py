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
    'name': 'Fischer Indole Synthesis',
    'description': 'Cyclization of arylhydrazones woth aldehyde or ketone to indoles',
    'templates': [
        {
            'A': [
                # Phenylhydrazine
                '[C;a:1]:[C;a;M][N;x1;z1:2][N;D1;x1;z1:3]'
                             
            ],
            'B': [
                # Alk-C=O
                '[O;D1;z2;x0:4]=[C;D3;x1;z2:5]([C;z1;x0;M])[C;D2,D3;z1;x0:6]',
                # Alk-CHO
                '[O;D1;z2;x0:4]=[C;D2;x1;z2:5][C;D2,D3;z1;x0:6]',
                # Alk-OH
                '[O;D1;x0;z1:4][C;D3;x1;z1:5]([C;z1;x0;M])[C;D2;z1;x0:6]'
            ],
            'product': '[A:2][A:5]=[A:6][A:1]',
            'alerts': [],
            'ufe':{
                'A': '[A:1][A:2][A:3]',
                'B': '[A:4][A:5][A:6]'
            }
        }
    ],
    'alerts': []
}
