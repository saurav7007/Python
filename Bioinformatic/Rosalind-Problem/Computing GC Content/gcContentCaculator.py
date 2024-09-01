def gcCalculator(file):
    import re

    file = open(file, "r")

    seqDic = {}
    key = '' 

    while True:
        line = file.readline().strip()

        if line == '':
            break

        seqName = re.match(">", line)

        if seqName is not None:
            key = line.strip('^>')
            
            if key not in seqDic:
                seqDic[key] = ''
        else:
            seqDic[key] += line

    seqGC = {}

    for name,seq in seqDic.items():
        seqGC[name]= round((((seq.count('G') + seq.count('C')) / len(seq))* 100), 6)

    maxGCSeqName = max(seqDic, key=seqGC.get)

    # Print the key and the highest value
    print(maxGCSeqName)
    print(seqGC[maxGCSeqName])

# Call the GC Calculator
gcCalculator("rosalind_gc.txt")