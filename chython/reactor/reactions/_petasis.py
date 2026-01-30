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
    'name': 'Petasis Reaction',
    'description': 'Combines a carbonyl derivative, an amine, and a boronic acid to produce substituted amines',
    'templates': [
            {
            'A': [
                # Ar-NH2
                '[N;D1;x0;z1:1][C;a;M]',
                # Alk-NH2
                '[N;D1;x0;z1:1][C;z1,z2;x1,x2;M]',
                # Ar-NH-Ar
                '[N;D2;x0;z1:1]([C;a;M])[C;a;M]',
                # Alk-NH-Ar
                '[N;D2;x0;z1:1]([C;a;M])[C;z1;x1;M]',
                # Alk2NH
                '[N;D2;x0;z1:1]([C;z1;x1;M])[C;z1;x1;M]'
            ],
            'B': [
                #Ar-CHO
                '[O;z2;x0:2]=[C;D2,D3;x1;z2:3][C;a;M]',
                #Alk-CHO
                '[O;z2;x0:2]=[C;D2,D3;x1;z2:3][C;z1,z2;M]'
            ],
            'C': [
                # Ar-B
                '[B;D3;x2;z1:4]([O:5])([O:6])-[C;a:7]',
                # C=C-B, [N,O]C=C-B, C=C([N,O])-B
                '[B;D3;x2;z1:4]([O:5])([O:6])-[C;x1,x2;z2:7]=[C;x0,x1;z2;M]',
                # B-C#C
                '[B;D3;x2;z1:4]([O:5])([O:6])-[C;D2;x1;z3:7]',
                # B-C(alk)
                '[B;D3;x2;z1:4]([O:5])([O:6])-[C;x1,x2;z1:7]'
            ],
            'product': '[A:1][A:3]-[A:7]',
            'alerts': [],
            'ufe': {
                'A': '[A:1]',
                'B': '[A:2]',
                'C': '[A:4][At;M]'
            }
        }
    ],
    'alerts': []
}
