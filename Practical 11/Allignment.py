#read the 3 given .fa files
with open("DLX5_human.fa") as fa:
    human = fa.read()
with open("DLX5_mouse.fa") as fa:
    mouse = fa.read()
with open("RandomSeq(1).fa") as fa:
    random = fa.read()
    
# set the initial value of edit_distance to be zero
edit_distance = 0
for i in range(len(human)):  #compare each amino acid
    if human[i]!=mouse[i]:
      edit_distance += 1     #add a score 1 if amino acids are different
    
# print out the answer
print("the edit distance between human and mouse sequences is " + str(edit_distance))

# reset the value of edit)distance to be zero
edit_distance = 0
# repeat the distance calculation the same as before
for i in range(len(random)): 
    if random[i]!=human[i]:
      edit_distance += 1
# print out the answer
print("the edit distance between human and random sequences is " + str(edit_distance))

# reset the value of edit)distance to be zero
edit_distance = 0
# repeat the distance calculation the same as before
for i in range(len(random)): 
    if random[i]!=mouse[i]:
      edit_distance += 1
# print out the answer
print("the edit distance between mouse and random sequences is " + str(edit_distance))
