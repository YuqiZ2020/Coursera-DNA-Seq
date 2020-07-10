def longestCommonPrefix(s1, s2):
    i = 0
    while (i < len(s1) and i < len(s2) and s1[i] == s2[i]):
        i = i + 1
    return s1[:i]

seq1 = "ATTCGATCGT"
seq2 = "ATTCACGTCGGT"
print(longestCommonPrefix(seq1, seq2))

def reverseComplement(s):
    complement = {'A':'T', 'C':'G', 'T':'A', 'G':'C'}
    ans = ''
    for base in s:
        ans = complement[base] + ans
    return ans

seq3 = "ACCTATCAGCGGC"
print(reverseComplement(seq3))

# import wget
# url = 'http://d28rh4a8wq0iu5.cloudfront.net/ads1/data/lambda_virus.fa'
# wget.download(url)

def readGenome(filename):
    genome = ""
    with open(filename, 'r') as genFile:
        for line in genFile:
            if not line[0] == '>':
                genome = genome + line.strip()
    return genome

genomeLambda = readGenome('lambda_virus.fa')
print(genomeLambda[:100])
print(len(genomeLambda))

import collections
print(collections.Counter(genomeLambda))
