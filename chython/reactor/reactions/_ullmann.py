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
    'name': 'Ullmann Reactions',
    'description': 'Synthesis of symmetric biaryls C–C, C–O and C-S coupling reaction',
    'templates': [
        # Template 1: Ullmann C–C Coupling
        {
            'A': [
                # Hal-Ar
                '[Cl,Br,I;D1:1][C;a:2]'
            ], 
            'B': [
                # Hal-Ar
                '[Cl,Br,I;D1:3][C;a:4]'
            ],
            'product': '[A:2]-[A:4]',
            'alerts': [],
            'ufe': {
                'A': 1,
                'B': 3
            }
        },
        # Template 2: Ullmann Ether (C–O) Coupling
        {
            'A': [
                # Hal-Ar
                '[Cl,Br,I;D1:1][C;a:2]'
            ], 
            'B': [
                # Ar-OH, Ar-SH
                '[O,S;D1;x0;z1:3][C;a;M]'
            ],  
            'product': '[A:2]-[A:3]',
            'alerts': [],
            'ufe': {
                'A': 1,
                'B': '[A:3][At:M]'
            }
        }
    ],
    'alerts': []
}
