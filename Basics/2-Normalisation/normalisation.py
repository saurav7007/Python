#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 19:54:20 2024

@author: krishagni
"""

def normalizer(inputFile, outputFile):
    data = {}
    with open(inputFile, 'r') as infile:
        line = infile.readline().strip()                                # Ignore the first line
        line = infile.readline().strip()                                # Read second line
        
        while line != '':
            values = line.split(',')                                    # Split data into 3 parts, Patient, Field, Value
            if values[0] in data:                                       # Check if the pateint is already parent in dictionary
                data[values[0]][values[1]] = values[2]                  # Add new fields value to the existing patient
            else:
                if data:                                                # If a new patient is found,
                    with open(outputFile, 'a', newline='') as outFile:  # push all the data of existing patient to the output file
                        outFile.write(str(data) + '\n')

                data = {}                                               # Empty the dictinary to release the memory
                data[values[0]] = {values[1]: values[2]}                # Push the data of new patient to the dictionary
                
            line = infile.readline().strip()                            # Read the next line      

        if data:                                                        # Write the last record outside the loop  
            with open(outputFile, 'a', newline='') as outFile:
                outFile.write(str(data) + '\n')

# Specify the paths to your input and output files
input_file_path = '/media/krishagni/aa4d9ed7-87ae-4d03-8fa2-9af1a94c8d2c/home/krishagni/Desktop/pythonPractice/9-Normalization/denormalizedData.csv'
output_file_path = '/media/krishagni/aa4d9ed7-87ae-4d03-8fa2-9af1a94c8d2c/home/krishagni/Desktop/pythonPractice/9-Normalization/normalizedData.csv'

normalizer(input_file_path, output_file_path)
