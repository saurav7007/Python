#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 17:45:03 2024

@author: saurav
"""

# Defining the function to check palindrome
def is_dna_palindrome(sequence):
    # Define an empty string for storing reverse sequence
    revSeq = ''

    # Populate the reverse sequence
    for nucleotide in sequence:
        revSeq = nucleotide + revSeq
    
    # If the revSeq matcheswith Original Seq, then it is palindrome
    if revSeq == sequence:
        return print('The given sequence {} is a Palindrome'.format(sequence))
    else:
        return print('The given sequence {} is not a Palindrome'.format(sequence))

# User input
nSeq = input(str('Enter the Nucleotide Sequnce: '))

# Call the function to check Palindrome
is_dna_palindrome(nSeq)