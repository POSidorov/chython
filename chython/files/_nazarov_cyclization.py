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
    'name': 'Nazarov Cyclization',
    'description': 'Formation of cyclopentenone from di-vinyl ketone',
    'templates': [
        {
            'A': [
                #Divinyl Ketone
                '[C;x0,x1;z2:1]=[C;x0,x1;z2:2][C;x1;z2;M]([C;x0,x1;z2;M]=[C;x0,x1;z2:4])=[O;M]',
                #Divinyl Dione
                '[C;z2;x0,x1:1]=[C;z2;x0,x1:2][C;z2;x1;M]([C;z2;x0,x1;M]=[O;z2;x0:4])=[O;M]',
                #Divinyl-Ar
                '[C;z2;x0,x1:1]=[C;z2;x0,x1:2][C;z2;x1;M](=[O;M])[C;a;M]:[C;a:4]'
            ],
            'product': '[A:4][A:1][A:2]',
            'alerts': [],
            'ufe': {
                'A': '[A:1][A:4]'
                
            }
        },
    ],
    'alerts': []
}