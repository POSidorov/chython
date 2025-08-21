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
    'name': 'DIBAL_Reduction',
    'description': 'Reducing esters and nitriles to aldehydes using DIBAL-H',
    'templates': [
        # Template 1: Ester and DIBAL-H to CHO
        {
            'A': [
                #Ester
                '[O;x0;z2;M]=[C;D3;x2;z2:1][O;D2;x0;z1:2]'
            ],
            'product': '[A:1]',
            'alerts': [],
            'ufe': {
                'A': 2
            }
        },
        # Template 2: Nitriles and DIBAL-H to CHO
       {
            'A': [
                #Nitrile
                '[N;D1;z3;x0:2]#[C;D2;x1;z3:1]'
            ],        
            'product': '[A:1]=[O]',
            'alerts': [],
            'ufe': {
                'A': 2
            }
        },  
    ],
    'alerts': []
}