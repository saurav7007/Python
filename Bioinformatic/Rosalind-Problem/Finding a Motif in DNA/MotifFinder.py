import re

def motifCount(file):
    file = open(file, "r")

    dnaSeq = file.readline().strip()
    motif = file.readline().strip()

    match = re.search(motif, dnaSeq).start()

    continueSearch = True

    motifStart = []

    while continueSearch:
        match = re.search(motif, dnaSeq)     

        if match is not None:    
            if motifStart == []:
                lastIndex = match.start()+1
                motifStart.append(lastIndex)
            else:
                lastIndex = match.start()+1
                motifStart.append(motifStart[-1] + lastIndex)
            
            dnaSeq = dnaSeq[lastIndex:]
            continueSearch = True
        else:
            continueSearch = False
    
    return motifStart

print(' '.join(map(str, motifCount('rosalind_subs.txt'))))