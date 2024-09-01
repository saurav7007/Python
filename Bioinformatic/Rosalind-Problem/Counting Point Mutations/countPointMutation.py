def hammarDistance(file):
    file = open(file, 'r')

    seq1 = file.readline().strip()
    seq2 = file.readline().strip()

    dH = 0

    for base in range(0, len(seq1)):
        if seq1[base] != seq2[base]:
            dH += 1

    print(dH)

hammarDistance('rosalind_hamm.txt')