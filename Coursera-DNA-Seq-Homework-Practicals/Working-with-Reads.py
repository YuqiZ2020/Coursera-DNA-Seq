# import wget
# url = 'http://d28rh4a8wq0iu5.cloudfront.net/ads1/data/SRR835775_1.first1000.fastq'
# wget.download(url)

def readFastq(filename):
    sequences = []
    qualities = []
    with open(filename) as fh:
        while True:
            fh.readline()
            seq = fh.readline().rstrip()
            fh.readline()
            qua = fh.readline().rstrip()
            if len(seq) == 0:
                break
            sequences.append(seq)
            qualities.append(qua)
    return sequences, qualities

sequences, qualities = readFastq("Wk1-Data/SRR835775_1.first1000.fastq")

print(sequences[:5])
print(qualities[:5])

def phred33toQ(qua):
    return ord(qua) - 33

def createHist(qualitiesList):
    hist = [0] * 50
    for qua in qualitiesList:
        for phred in qua:
            qScore = phred33toQ(phred)
            hist[qScore] += 1
    return hist

qualitiesHistogram = createHist(qualities)
print(qualitiesHistogram)

import matplotlib.pyplot as plt
plt.plot(range(len(qualitiesHistogram)), qualitiesHistogram )
plt.show()

def findGCbyPos(sequencesList):
    gc = [0] * 100
    total = [0] * 100
    for read in sequencesList:
        for i in range(len(read)):
            if read[i] == 'C' or read[i] == 'G':
                gc[i] += 1
            total[i] += 1
    for i in range(len(gc)):
        if (total[i] > 0):
            gc[i] /= float(total[i])
    return gc

gcInPos = findGCbyPos(sequences)

plt.plot(range(len(gcInPos)), gcInPos)
plt.show()

import collections
count = collections.Counter()
for seq in sequences:
    count.update(seq)
print(count)

