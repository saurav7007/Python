#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 09:58:45 2024

@author: saurav
"""

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

# Transpose the matrix using list comprehension and zip
transposed = [list(row) for row in zip(*matrix)]

print('The transposed matrix is: ', transposed)