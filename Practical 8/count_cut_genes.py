filename=input()

#Now input the file name.
# I used the file 'cut_genes.txt' in the working directory to test

#First, open the file and store the data.
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa') as fa:
#The data will be stored in the dict "fa_dict".
    fa_dict = {}
    for line in fa:
        # Remove end line breaks "\n".
        line = line.replace('\n','')
        if line.startswith('>'):
            # Remove ">" at the beginning.
            seq_name = line[1:]
            fa_dict[seq_name] = ''
        else:
            # Remove end newline and join multiline sequences
            fa_dict[seq_name] += line.replace('\n','')


#Find out sequence in the fa_dict and put the sequence and relative information into another dictionary.
filtered_dict={}
for (key,value) in zip(fa_dict.keys(), fa_dict.values()):
    if value.find('GAATTC')>=0:
        filtered_dict[key]=value


#Turn the dictionary into strings.
res = str(filtered_dict)
import re
#Use re to process.
#Filter the name and sequence in the string. 
#The criteria is based on the text features.
name = re.findall(r'gene:(\S+)', res)
seq = re.findall(r'[A-Z]+GAATTC[A-Z]+', res)
#The output will be lists.


# Calculate fragment number and store it in a list.
frag=[]
for x in seq:
    ment=x.count('GAATTC')+1
    frag.append(ment)

#Create the file.
file = open(filename,'w')
for i in range(0,len(seq)):
# Store information in an 'int' first.
    line1=name[i]
# Variable 'int' must be turned into a 'str' to be written in the file.
    line1=str(line1)
    line2=frag[i]
    line2=str(line2)
    line3=seq[i]
    line3=str(line3)
    file.write('>'+line1+' '+line2+'\n'+line3+'\n')

file.close()
