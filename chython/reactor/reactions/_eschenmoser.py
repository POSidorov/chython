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
    'name' : 'Eschenmoser Coupling',
    'description': 'thioamide and an α-halocarbonyl compound to enaminones products',
    'templates': [
        {
            'A': [
                # S=C-N-R
                '[S;D1;x0;z2:1]=[C;D3;x2;z2:2][N;x0;z1;M]'
            ],
            'B': [
                # Br-CC(=O)-OR
                '[Br;D1:3][C;D2;x1;z1:4][C;x2;z2;M](=[O;M])[O;M]',
                # EWG-CBr-EWG
                '[O;M][C;x2;z2;M](=[O;M])[C;D3;x1;z1:4]([Br;D1:3])[C;x2;z2;M](=[O;M])[O;M]',
                # 3-bromoindolin-2-one
                '[Br;D1:3]-[C;D3;x1;z1:4]([C;a;M])[C;x2;z2;M](=[O;M])[N;M]'
            ],
            'product': '[A:2]=[A:4]',
            'alerts': [],
            'ufe':{
                'A': 1,
                'B': '[A:3]'
            }
        }
    ],
    'alerts' : []
}
