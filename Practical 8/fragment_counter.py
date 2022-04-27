import re
# input the sequences
seq = 'ATGCAATCGACTACGATCAATCGAGGGCC'
# count the number of the fragments that can be cut by the enzyme
fragment = seq.count("GAATC") + 1
# print out the answer
print("the number of fragments is " + str(fragment))
