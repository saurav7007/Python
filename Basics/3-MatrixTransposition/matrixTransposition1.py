#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 16:05:24 2024

@author: saurav
"""

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

transposed = []


for rowNum, row in enumerate(matrix):
    for colNum, item in enumerate(row):
        # Check if transposed matrix needs a new row
        if len(transposed) <= colNum:
            transposed.append([item])
        else:
            transposed[colNum].append(item)
            
print('The transposed matrix is: ', transposed)