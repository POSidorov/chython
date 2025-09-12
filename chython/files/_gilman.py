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
    'name': 'Gilman Reaction',
    'description': 'Acid chlorides and α,β-unsaturated carbonyl compounds reaction with Gilman reagents',
    'templates': [
        {
            'A': [
                #α,β-unsaturated ketones
                '[O;x0;z2;M]=[C;x1;z2;M]([C;x0;z1;M])[C;x0;z2:1]=[C;x0;z2:2]'
            ],
            'B':[
                #Gilman Reagent
                '[C;x1;z1,z2:3][Cu-;x0:4].[Li+:5]',
                '[C;a:3][Cu-;x0:4].[Li+:5]'
             ],
            'product': '[A:1][A:2]-[A:3]',
            'alerts': [],
            'ufe': {
                'A': '[A:1][A:2]',
                'B': '[A:3]'
            }
        },
        {
            'A': [
                #Acid Chloride-Alk
                '[Cl;D1:1][C;D3;x2;z2:2]([C;x0;z1;M])=[O;M]',
                #Acid Chloride-Ar
                '[Cl;D1:1][C;D3;x2;z2:2]([C;a;M])=[O;M]',
            ],
            'B':[
                #Gilman Reagent
                '[C;x1;z1,z2:3][Cu-;x0:4][C;x1;z1,z2:5].[Li+:6]',
                '[C;a:3][Cu-;x0:4][C;a:5].[Li+:6]'
             ],
            'product': '[A:2]-[A:3]',
            'alerts': [],
            'ufe': {
                'A': '[A:1][A:2]',
                'B': '[A:3]'
            }
        },
    ],
    'alerts' : []
}