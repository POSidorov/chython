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
    'name' : 'Wolff Rearrangement',
    'description': 'Diazoketone in to a ketene and ring constraction',
    'templates': [
        {
            'A': [
                  # H-Diazoketone
                  '[N-;z2;x1:1]=[N+;x1;z3:2]=[C;x1;z2:3][C;x1;z2:4](=[O;M])[H:5]',
                  # Ar-Diazoketone
                  '[N-;z2;x1:1]=[N+;x1;z3:2]=[C;x1;z2:3][C;x1;z2:4](=[O;M])[C;a:5]',
                  # Alk-Diazoketone
                  '[N-;z2;x1:1]=[N+;x1;z3:2]=[C;x1;z2:3][C;x1;z2:4](=[O;M])[C;z1:5]',
                 ],
            'B': [
                  # CH2OH
                '[C;x1;z1;M][O;D1;z1:6]'
            ],
            'product': '[A:5][A:3][A:4][A:6]',
            'alerts': [],
            'ufe': {
                'A': 1,
                'B': '[A:6]'
            }
        }
    ],
    'alerts':[]
}
