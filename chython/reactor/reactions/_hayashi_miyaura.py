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
    'name': 'Hayashi-Miyaura_Reaction',
    'description': 'Aryl- or Alkenyl-boronic acids to α,β-unsaturated ketones',
    'templates': [
        {
            'A': [
                # α,β-unsaturated ketone
                '[O;z2;x0;M]=[C;D3;z2;x1,x2;M][C;z2;x0:1]=[C;D2;z2;x0,x1:2]'
            ],
            'B': [
                # Ar-B
                '[B;D3;x2;z1:4]([O:5])([O:6])-[C;a:3]',
                # C=C-B, [N,O]C=C-B, C=C([N,O])-B
                '[B;D3;x2;z1:4]([O:5])([O:6])-[C;x1,x2;z2:3]=[C;x0,x1;z2;M]'
            ],
            'product': '[A:1][A:2]-[A:3]',
            'alerts': [],
            'ufe': {
                'A': '[A:1][A:2]',
                'B': '[A:3][At;M]'
            }
        }
    ],
    'alerts' : []
}
