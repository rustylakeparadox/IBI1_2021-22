import re
#read the 3 given .fa files
with open("DLX5_human.fa") as fa:
    human = fa.read()
with open("DLX5_mouse.fa") as fa:
    mouse = fa.read()
with open("RandomSeq(1).fa") as fa:
    random = fa.read()

# extract the amino acid sequence
human_re = re.findall(r'\n(\S+)', human)
human_re = str(human_re)
seq_human=[]
for line in human_re:
    line= line.replace('[','')
    if not line.startswith(']'):
        seq_human += line

# delete useless punctuation
del seq_human[0]
del seq_human[-1]

# the same operation for the mouse and the random sequences
mouse_re = re.findall(r'\n(\S+)', mouse)
mouse_re = str(mouse_re)

seq_mouse=[]
for line in mouse_re:
    line= line.replace('[','')
    if not line.startswith(']'):
        seq_mouse += line

del seq_mouse[0]
del seq_mouse[-1]

random_re = re.findall(r'\n(\S+)', random)
random_re = str(random_re)

seq_random=[]
for line in random_re:
    line= line.replace('[','')
    if not line.startswith(']'):
        seq_random += line

del seq_random[0]
del seq_random[-1]

# set the initial value of edit_distance to be zero
edit_distance_1 = 0
for i in range(len(seq_mouse)):  #compare each amino acid
    if seq_mouse[i]!=seq_human[i]:
      edit_distance_1 += 1     #add a score 1 if amino acids are different
    
#culcalate the percentage of identical amino acid in the comparison
pc1= edit_distance_1/len(seq_mouse)    
pc1= (1-pc1)*100

# print out the answer
print ('The number of different amino acids between human and mouse is',edit_distance_1)
print("the percentage of identical amino acids between human and mouse is " + str(pc1) + "%")

# reset the value of edit)distance to be zero
edit_distance_2 = 0
# repeat the distance calculation the same as before
for i in range(len(seq_human)): 
    if seq_human[i]!=seq_random[i]:
      edit_distance_2 += 1
#culcalate the percentage of identical amino acid in the comparison
pc2= edit_distance_2/len(seq_human)    
pc2= (1-pc2)*100

# print out the answer
print ('The number of different amino acids between human and random is',edit_distance_2)
print("the percentage of identical amino acids between human and random is " + str(pc2) + "%")


# reset the value of edit)distance to be zero
edit_distance_3 = 0
# repeat the distance calculation the same as before
for i in range(len(seq_random)): 
    if seq_random[i]!=seq_mouse[i]:
      edit_distance_3 += 1
    
#culcalate the percentage of identical amino acid in the comparison
pc3= edit_distance_3/len(seq_random)    
pc3= (1-pc3)*100

# print out the answer
print ('The number of different amino acids between mouse and random is',edit_distance_3)
print("the percentage of identical amino acids between mouse and random is " + str(pc3) + "%")
