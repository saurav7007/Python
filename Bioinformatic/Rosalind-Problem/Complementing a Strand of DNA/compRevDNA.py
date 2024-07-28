seqFile = open('rosalind_revc.txt', 'r')

inputSeq = seqFile.read().strip()

complement = ''

for nucleotide in inputSeq:
    if nucleotide == 'A':
        complement += 'T'
    elif nucleotide == 'T':
        complement += 'A'
    elif nucleotide == 'G':
        complement += 'C'
    else:
        complement += 'G'

revComplement = complement[::-1]

print('The reverse Compliment of the input string is:\n{}'.format(revComplement))
