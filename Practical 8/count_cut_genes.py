# input the file name.
filename=input()

# I used the file 'cut_genes.txt' in the working directory to test

# open the file and store the data.
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa') as fa:
# The data will be stored in the dictionary "fa_dict".
    fa_dict = {}
    for line in fa:
        # Remove line breaks "\n" at the end 
        line = line.replace('\n','')
        if line.startswith('>'):
            # Remove ">" at the beginning
            seq_name = line[1:]
            fa_dict[seq_name] = ''
        else:
            # Remove the line break at the end and join multiline sequences together
            fa_dict[seq_name] += line.replace('\n','')


# find out the sequence that can be cut by the enzyme and put the it with its relative information into another dictionary.
filtered_dict={}
for (key,value) in zip(fa_dict.keys(), fa_dict.values()):
    if value.find('GAATTC')>=0:
        filtered_dict[key]=value


# swift the dictionary to strings
res = str(filtered_dict)
import re
# use re to process.
# filter the name and sequence in the string 
# the criteria is based on the text features
name = re.findall(r'gene:(\S+)', res)
seq = re.findall(r'[A-Z]+GAATTC[A-Z]+', res)
# the output will be lists


# calculate the number of fragments and store it in a list.
frag=[]
for x in seq:
    ment=x.count('GAATTC')+1
    frag.append(ment)

# create the file
file = open(filename,'w')
for i in range(0,len(seq)):
# store the information in an 'int' first.
    line1=name[i]
# 'int' must be turned into a 'str' to be written in the file.
    line1=str(line1)
    line2=frag[i]
    line2=str(line2)
    line3=seq[i]
    line3=str(line3)
    file.write('>'+line1+' '+line2+'\n'+line3+'\n')

file.close()
