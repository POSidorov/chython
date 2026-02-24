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
    'name': 'Chan-Lam Reaction',
    'description': 'Cross-coupling reaction between an aryl or alkyl boronic acid and an amine or alcohol',
    'templates': [
        {
            'A': [
                # Ar-NH2
                '[N;D1;x0;z1:1][C;a;M]',
                # Alk2NH
                '[N;D2;x0;z1:1]([C;z1;x1;M])[C;z1;x1;M]',
                # Pyrrole
                '[N;h1;a;r5:1]:[C;a;r6;M]',
                # Lactom Ring-NH,
                '[N;D2;x0;z1:1]([C;z2;x2;M])[C;z1;x1;M]',
                # O=C-NH2
                '[N;D1;x0;z1:1][C;z2;x2;M]=[O;x0;z2;M]',
                # RCOOH
                '[O;x0;z2;M]=[C;x2;M][O;D1:1]'
            ],
            'B': [
                # Ar-B
                '[B;D3;x2;z1:3]([O:4])([O:5])-[C;a:2]',
                # C=C-B, [N,O]C=C-B, C=C([N,O])-B
                '[B;D3;x2;z1:3]([O:4])([O:5])-[C;x1,x2;z2:2]=[C;x0,x1;z2;M]',
                # B-C#C
                '[B;D3;x2;z1:3]([O:4])([O:5])-[C;D2;x1;z3:2]',
                # B-C(alk)
                '[B;D3;x2;z1:3]([O:4])([O:5])-[C;x1,x2;z1:2]'
                
            ],
            'product': '[A:1]-[A:2]',
            'alerts': [],
            'ufe': {
                'A': 1,
                'B': '[A:3][At;M]'
            }
        }
    ],
    'alerts': []
}
