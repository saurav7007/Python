def findCommonAncestor(file):
    with open(file, 'r') as file:
        sequences = {}
        current_seq = None
        
        # Read the FASTA file and store sequences
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                current_seq = line[1:]
                sequences[current_seq] = ''
            else:
                sequences[current_seq] += line
    # Initialize matrix for nucleotide counts
    matrix = {}

    # Loop through all sequences and populate the matrix
    for sequence in sequences.values():
        for index in range(0, len(sequence)):
            # Initialize the matrix dictionary for each position
            if index not in matrix:
                matrix[index] = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
            # Increment the nucleotide count at the current position
            matrix[index][sequence[index]] += 1
            
    # Build the consensus string from the matrix
    consensusString = ''
    for position in matrix:
        consensusString += max(matrix[position], key=matrix[position].get)

    print("Consensus String:")
    print(consensusString)

    # Create matrix view for nucleotide counts
    print("\nNucleotide Count Matrix:")
    matrixView = ''
    for nucleotide in ['A', 'C', 'G', 'T']:
        for index in range(0, len(matrix)):
            if index == 0:
                matrixView += nucleotide + ': ' + str(matrix[index].get(nucleotide, 0))
            else:
                matrixView += ' ' + str(matrix[index].get(nucleotide, 0))
        matrixView += '\n'

    print(matrixView)

# Call the function with your FASTA file
findCommonAncestor('rosalind_cons.txt')