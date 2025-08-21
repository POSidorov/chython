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
    'name': 'Diels Alder Reaction',
    'description': 'Conjugated diene and a dienophile reaction to form the cyclohexene ring',
    'templates':  [
        #Alkene Template
        {
            'A':  [
                #Conjugated diene-EDG
                #Conjugated diene-Hetero
                '[C;D1,D2;x0;z2:1]=[C;x0;z2:2][C;x0;z2:3]=[C;D2;x1;z2:4][O,N,Cl,Br,I;M]',
                #Conjugated diene-Alk
                '[C;D1,D2;x0;z2:1]=[C;x0;z2:2][C;x0;z2:3]=[C;D2;x0;z2:4][C;x0;z1,z2;M]',
                #Conjugated diene-Ar
                '[C;D1,D2;x0;z2:1]=[C;x0;z2:2][C;x0;z2:3]=[C;D2;x0;z2:4][C;a;M]',
                #Conjugated diene C=O-Hetero
                '[O;D1,D2;x0;z2:1]=[C;x1;z2:2][C;x0;z2:3]=[C;D2;x1;z2:4][O,N,Cl,Br,I;M]',
                #Conjugated diene C=O-Alk
                '[O;D1,D2;x0;z2:1]=[C;x1;z2:2][C;x0;z2:3]=[C;D2;x0;z2:4][C;x0;z1,z2;M]',
                #Conjugated diene-Ar
                '[O;D1,D2;x0;z2:1]=[C;x1;z2:2][C;x0;z2:3]=[C;D2;x0;z2:4][C;a;M]',
                #Cyclopentadiene
                '[C;D2;x0;z2:1]1=[C;x0;z2:2][C;x0;z2:3]=[C;D2;x0;z2:4][C;x0;z1;M]1'
                
               ],
            'B':  [
                #Dienophile-EWG
                #Dienophile-CHO
                '[C;D1,D2;x0;z2:5]=[C;D2;x0,x1;z2:6][C;x1,x2;z2;M]=[O;M]',
                #Dienophile-CO-Alk
                '[C;D1,D2;x0;z2:5]=[C;D2;x0;z2:6][C;x1;z2;M]-[O;M]',
                #Dienophile-CF3
                '[C;D1,D2;x0;z2:5]=[C;D2;x0;z2:6][C;x3;z2;M]-[F;M]',
                #Dienophile-C#N
                '[C;D1,D2;x0;z2:5]=[C;D2;x0;z2:6][C;x1;z3;M]#[N;M]',
                #Dienophile-NO2
                '[C;D1,D2;x0;z2:5]=[C;D2;x1;z2:6][N+;D3;x2;M][O-;M]',
                #Dienophile-SO3H
                '[C;D1,D2;x0;z2:5]=[C;D2;x1;z2:6][S;D3;x3;M][O;M]'                
            ],
          
            'product': '[A:1]1[A:5][A:6][A:4][A:3]=[A:2]1',   
            'alerts': [],
            'ufe': {
                'A': '[A:1][A:2]',
                'B': '[A:3][A:6]'
            }
            
        },
        #Alkyne Template
        {
            'A':  [
                #Conjugated diene-EDG
                #Conjugated diene-Hetero
                '[C;D1,D2;x0;z2:1]=[C;x0;z2:2][C;x0;z2:3]=[C;D2;x1;z2:4][O,N,Cl,Br,I;M]',
                #Conjugated diene-Alk
                '[C;D1,D2;x0;z2:1]=[C;x0;z2:2][C;x0;z2:3]=[C;D2;x0;z2:4][C;x0;z1,z2;M]',
                #Conjugated diene-Ar
                '[C;D1,D2;x0;z2:1]=[C;x0;z2:2][C;x0;z2:3]=[C;D2;x0;z2:4][C;a;M]',
                #Conjugated diene C=O-Hetero
                '[O;D1,D2;x0;z2:1]=[C;x1;z2:2][C;x0;z2:3]=[C;D2;x1;z2:4][O,N,Cl,Br,I;M]',
                #Conjugated diene C=O-Alk
                '[O;D1,D2;x0;z2:1]=[C;x1;z2:2][C;x0;z2:3]=[C;D2;x0;z2:4][C;x0;z1,z2;M]',
                #Conjugated diene-Ar
                '[O;D1,D2;x0;z2:1]=[C;x1;z2:2][C;x0;z2:3]=[C;D2;x0;z2:4][C;a;M]',
                #Cyclopentadiene
                '[C;D2;x0;z2:1]1=[C;x0;z2:2][C;x0;z2:3]=[C;D2;x0;z2:4][C;x0;z1;M]1'
                
               ],
            'B':  [
                #Dienophile#EWG
                #Dienophile#CHO
                '[C;D1,D2;x0;z3:5]#[C;D2;x0,x1;z3:6][C;x1,x2;z2;M]=[O;M]',
                #Dienophile#CO-Alk
                '[C;D1,D2;x0;z3:5]#[C;D2;x0;z3:6][C;x1;z2;M]-[O;M]',
                #Dienophile#CO-Hetere
                '[C;D1,D2;x0;z3:5]#[C;D2;x0;z3:6][C;x2;z2;M]=[O;M]',
                #Dienophile#CF3
                '[C;D1,D2;x0;z3:5]#[C;D2;x0;z3:6][C;x3;z2;M]-[F;M]',
                #Dienophile-C#N
                '[C;D1,D2;x0;z3:5]#[C;D2;x0;z3:6][C;x1;z3;M]#[N;M]',
                #Dienophile-NO2
                '[C;D1,D2;x0;z3:5]#[C;D2;x1;z3:6][N+;D3;x2;M][O-;M]',
                #Dienophile-SO3H
                '[C;D1,D2;x0;z3:5]#[C;D2;x1;z3:6][S;D3;x3;M][O;M]'                
            ],
          
            'product': '[A:1]1[A:5]=[A:6][A:4][A:3]=[A:2]1',   
            'alerts': [],
            'ufe': {
                'A': '[A:1][A:2]',
                'B': '[A:3][A:6]'
            }
            
        }
        
    ],

    'alerts': []
}