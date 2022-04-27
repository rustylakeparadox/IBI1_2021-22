import sys
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa') as fa:     # open the file
    fa_dict = {}     # create a dictionary
    for line in fa:    
    # remove the line break at the beginning of the file
        line = line.replace('\n','')
        if line.startswith('>'):
         # remove the ">"
            seq_name = line[1:]
            fa_dict[seq_name] = ''
        else:
            # remove the line break at last and integrate all the fragments
            fa_dict[seq_name] += line.replace('\n','')

# create another dictionary
filtered_dict={}
# find the sequences that can be cut by the enzyme and store them
for (key,value) in zip(fa_dict.keys(), fa_dict.values()):
    if value.find('GAATTC')>=0:
        filtered_dict[key]=value

# change the list to strings
res = str(filtered_dict)
import re
name = re.findall(r'gene:(\S+)', res)    # store the gene names 
seq = re.findall(r'[A-Z]+GAATTC[A-Z]+', res)    # store the sequences
#the output will be lists

# create a new list
seqlen = []
# calculate the length and store it in the list
for x in seq:
    length = len(x)
    seqlen.append(length)

# create the file
file = open('cut_genes.fa','w')
for i in range(0,len(seq)):
#Store information in an int first.
    line1=name[i]
# variable 'int' must be turned into a 'str' to be written in the file.
    line1=str(line1)
    line2=seqlen[i]
    line2=str(line2)
    line3=seq[i]
    line3=str(line3)
# integrate the contents
    file.write('>'+line1+' '+line2+'\n'+line3+'\n')

file.close()
