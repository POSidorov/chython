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
    'name': 'Baeyer-Villiger Oxidation',
    'description': 'Ketones into esters using mCPBA or H2O2',
    'templates': [
        {
            'A': [
                # Ar-Ketone
                '[O;z2;x0;M]=[C;D3;x1;z2:1]([C;z1;M])[C;a:2]',
                '[O;z2;x0;M]=[C;D3;x1;z2:1]([C;a;M])[C;z1:2]',
                # Alk-Ketone
                '[O;z2;x0;M]=[C;D3;x1;z2:1]([C;z1;M])[C;D3,D2;z1,z2:2]',
                # Alk-CHO
                '[O;z2;x0;M]=[C;D2;x1;z2:1][C;D3,D2;x0,x1,x2;z1,z2:2]',
                # Ar-CHO
                '[O;z2;x0;M]=[C;D2;x1;z2:1][C;a:2]',
                # Cyclic-Ketone
                '[O;z2;x0;M]=[C;D3;x1;z2:1]([C;D2;x0,x1;z1;r4,r5,r6,r7,r8;M])[C;D2,D3;x0;z1;r4,r5,r6,r7,r8:2]'
            ],
            'B': [
                # mCPBA
                '[O;D1;x1;z1:3][O;D2;x1;z1:4][C;x2;z2:5](=[O;z2;x0:6])[C;a:7]',
                # H2O2
                '[O;D1:3][O;D1:4]'
            ],
            'product': '[A:2][A:3][A:1]',
            'alerts': [],
            'ufe': {
                'A': 1,
                'B': '[A:5][A:5][A:6]'
            }
        }
    ],
    'alerts':[]
}
