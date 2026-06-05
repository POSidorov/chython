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
    'name': 'Wittig Reaction',
    'description': 'Reaction of an aldehyde or ketone with the ylide to alkene',
    'templates': [
        {
            'A': [
                # Carbonyls 
                '[O;D1;z2;x0:1]=[C;D2,D3;x1;z2:2]'
            ],
            'B': [
                # Ylide
                '[C;D1,D2;z2:3]=[P:4]([C;a:5])([C;a:6])[C;a:7]'
            ],
            'product': '[A:2]=[A:3]',
            'alerts': [],
            'ufe':{
                'A':1,
                'B': '[A:4][A:5][A:6][A:7]'
            }
        }
    ],
    'alerts': []
}
