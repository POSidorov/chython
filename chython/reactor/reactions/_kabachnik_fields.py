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
    'name' : 'Kabachnik Fields Reaction',
    'description': 'Coupling of a aldehyde, primary amine and a hydrophosphoryl to aminophosphonates',
    'templates': [
        {
            'A': [
                # Ar-NH2
                '[N;D1;x0;z1:1][C;a;M]',
                # Alk-NH2
                '[N;D1;x0;z1:1][C;x1;z1;M]'
            ],
            'B': [
                # Ar-CHO
                '[O;x0;z2:2]=[C;D2;x1;z2:3][C;a;M]',
                # Alk-CHO
                '[O;x0;z2:2]=[C;D2;x1;z2:3][C;z1;M]'
            ],
            'C': [
                # Hydrophosphoryl
                '[O;z2;x1;M]=[P;D3:4]([O;z1;x1;M])[O;z1;x1;M]'
            ],
            'product': '[A:1][A:3][A:4]',
            'alerts': [],
            'ufe': {
                'A': '[A:1]',
                'B': '[A:2]',
                'C': '[A:4][At;M]'
            }
        }
    ],
    'alerts':[]
}
