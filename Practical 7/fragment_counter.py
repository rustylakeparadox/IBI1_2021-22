import re
seq = 'ATGCAATCGACTACGATCAATCGAGGGCC'
fragment = seq.count("GAATC") + 1
print("the number of fragments is " + str(fragment))
