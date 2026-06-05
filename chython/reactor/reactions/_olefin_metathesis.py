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


smarts_A = ['[C;D1;z2;x0:1]=[C;z2;x0:2]' + '[A;M]'*x + '[C;z2;x0:3]=[C;D1;z2;x0:4]' for x in range(2,20)]     
smarts_B = ['[C;D1;z2;x0:1]=[C;z2;x0:2][C;z1;x0;M][C;a;M]:[C;a;M]' + '[A;M]'*x + '[C;z2;x0:3]=[C;D1;z2;x0:4]' for x in range(0,20)]
smarts_all = smarts_A + smarts_B 
template = {
    'name': 'Olefin Metathesis',
    'description': 'Rearranges the fragments of alkenes and reforming carbon-carbon double bonds',
    'templates': [
        # Intramolecular olefin metathesis (ring-closing metathesis)
        {
            'A': smarts_all,
                                     
            'product': '[A:2]=[A:3]',
            'alerts' : [],
            'ufe': {
                'A': '[A:1][A:4]'   
            }
        },
        # Interamolecular olefin metathesis (cross-metathesis)
        {
            'A':[
                # C=C
                '[C;D1;z2;x0:1]=[C;D2,D3;z2;x0:2]'
            ],
            'B': [
                # C=C
                '[C;D1;z2;x0:3]=[C;D2,D3;z2;x0:4]'
            ],
            'product': '[A:2]=[A:4]',
            'alerts' : [],
            'ufe': {
                'A': 1,
                'B': 3
            }
        } 
    ],
    'alerts': []
}
