#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 17:45:03 2024

@author: saurav
"""

# Defining the function to check palindrome
def is_dna_palindrome(sequence):    
    # Get the length half length of the sequence
    halfSeqLen = len(sequence) // 2
    
    # Iterate through the first half of the sequence and its reverse
    for forNuc, revNuc in zip(sequence[0:halfSeqLen + 1], sequence[::-1][0:halfSeqLen + 1]):
        # Compare characters from the beginning and end
        if forNuc != revNuc:
            return print('The given sequence {} is not a Palindrome'.format(sequence))
    
    # If the loop completes without returning, it's a palindrome
    return print('The given sequence {} is a Palindrome'.format(sequence))

# User input
nSeq = input(str('Enter the Nucleotide Sequence: '))

# Call the function to check Palindrome
is_dna_palindrome(nSeq)