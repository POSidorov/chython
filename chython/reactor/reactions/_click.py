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
    'name': 'Click Reaction',
    'description' : 'Azide-alkyne cycloaddition reaction',
    'templates' : [
        {
            'A':  [
                # N=N=N-Ar
                '[N-;D1;x1;z2:1]=[N+;D2;x2;z3:2]=[N;D2;x1;z2:3][C;a;M]',
                # N=N=N-Alk
                '[N-;D1;x1;z2:1]=[N+;D2;x2;z3:2]=[N;D2;x1;z2:3][C;x1;z1;M]'
            ],
            'B':  [
                # C#C-Ar
                '[C;x0;z3:5]#[C;x0:4][C;a;M]',
                # C#C-Alk
                '[C;x0;z3:5]#[C;x0:4][C;x0;z1;M]'
            ],
            'product': '[A:1]1=[A:2]-[A:3]-[A:5]=[A:4]1',
            'alerts' : [],
                'ufe' : {
                    'A': '[A:1][A:2][A:3][At;M]',
                    'B': '[A:4][A:5][At;M]'
                }
            }
        ],
        'alerts' : []
}
