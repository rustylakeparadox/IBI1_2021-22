import sys
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa') as fa:
    fa_dict = {}
    for line in fa:
    # 去除末尾换行符
        line = line.replace('\n','')
        if line.startswith('>'):
            # 去除 > 号
            seq_name = line[1:]
            fa_dict[seq_name] = ''
        else:
            # 去除末尾换行符并连接多行序列
            fa_dict[seq_name] += line.replace('\n','')

filtered_dict={}
for (key,value) in zip(fa_dict.keys(), fa_dict.values()):
    if value.find('GAATTC')>=0:
        filtered_dict[key]=value

res = str(filtered_dict)
import re
name = re.findall(r'gene:(\S+)', res)
seq = re.findall(r'[A-Z]+GAATTC[A-Z]+', res)
#the output will be list


seqlen = []
# calculate the length
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
    file.write('>'+line1+' '+line2+'\n'+line3+'\n')

file.close()