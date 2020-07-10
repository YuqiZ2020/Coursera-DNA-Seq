seq = "ATCGCCTGA"
len(seq)
print(seq[-2: ])
print(seq[2:5])
print(seq[ :5])

letters = ['T', 'C', 'A', 'G']
print("joined letters = " + ''.join(letters))

import random
seq2 = ""
for _ in range(10):
    seq2 += random.choice("ATCG")
print("seq2 = " + seq2)
seq3 = ''.join([random.choice("ATCG") for _ in range(10)])
print("seq3 = " + seq3)