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
    'name': 'Heck Reaction',
    'description': 'C-C coupling between aryl halides or vinyl halides and activated alkenes',
    'templates': [
        {
            'A': [
                #Hal-Ar
                '[Cl,Br,I;D1:1]-[C;a:2]'
            ],
            'B': [
                #C=C-Alk
                '[C;D1;x0;z2:3]=[C;D2;x0;z2;M][C;x0;z1;M]',
                #C=C-Ar
                '[C;D1;x0;z2:3]=[C;D2;x0;z2;M][C;a;M]',
                #C=C-Acid
                '[C;D1;x0;z2:3]=[C;x0,x1;z2;M][C;x2;z2;M]',
                #Olefines
                '[C;D2;x0;z2:3]=[C;D3;x0;z2;M]'
                ],
                'product': '[A:2]-[A:3]',
                'alerts': [],
                'ufe': {
                'A': 1,
                'B': 3
            }
        }
    ],
    'alerts': []
}