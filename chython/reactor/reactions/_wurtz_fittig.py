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
    'name': 'Wurtz Reaction',
    'description': 'Coupling of two alkyl halides to form symmetrical alkanes',
    'templates' : [
        {
            'A': [
                # X-Alk
                '[Cl,Br,I;D1:1]-[C;D1,D2;x1;z1:2]' 
                ],
            'B': [
                # X-Alk
                '[Cl,Br,I;D1:3]-[C;D1,D2;x1;z1:4]'
            ],
            'product': '[A:2]-[A:4]',
            'alerts': [],
            'ufe': {
                'A': 1,
                'B': 3
            }
        }
    ],
    'alerts':[]
}
