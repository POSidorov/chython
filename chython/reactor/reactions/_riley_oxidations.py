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
    'name': 'Riley Oxidations',
    'description': 'Oxidation of allylic C-H bonds with selenium oxide',
    'templates': [
        # Template 1: Alkene group(R-C=C-R)
        {
            'A':[
                # R-C(R)=C
                '[C;D1;z1;x0:1][C;D3;z2;x0;M]=[C;z2;M]',
                # R-C=C
                '[C;D1;z1;x0:1][C;D2;z2;M]=[C,O;z2;M]',
                # C-Ar
                '[C;D1;z1;x0:1]-[C;a;M]'
            ],
            'B': [
                # SeO2
                '[O;D1;z2;x1:2]=[Se;z3;x2:3]=[O;D1;z2;x1:4]'
            ],
            'product': '[A:1]=[A:2]',
            'alerts': [],
            'ufe':{
                'A': '[A:1][At;M]',
                'B': '[A:2][A:3][A:4]'
            }
        },
        # Template 2: Alkyne group(R-C#C-R)
        {
            'A':[
                # RC#CR
                '[C;D2;z3;x0:1]#[C;D2;z3;x0:2]'  
            ],
            'B': [
                # SeO2
                '[O;D1;z2;x1:3]=[Se;z3;x2:4]=[O;D1;z2;x1:5]'
            ],
            'product': '[A:3]=[A:1][A:2]=[A:5]',
            'alerts': [],
            'ufe':{
                'A': '[A:1][At;M]',
                'B': '[A:2][A:3][A:4]'
            }
        },
        # Template 3: Alkyne group(R-C#C-H)
        {
            'A':[
                # RC#CH
                '[C;D2;z3;x0:1]#[C;D1;z3;x0:2]'
                
            ],
            'B': [
                # SeO2
                '[O;D1;z2;x1:3]=[Se;z3;x2:4]=[O;D1;z2;x1:5]'
            ],
            'product': '[A:3]=[A:1][A:2]([O])=[A:5]',
            'alerts': [],
            'ufe':{
                'A': '[A:1][At;M]',
                'B': '[A:2][A:3][A:4]'
            }
        }
    ],
    'alerts':[]
}
