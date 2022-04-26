with open("DLX5_human.fa") as fa:
    human = fa.read()
with open("DLX5_mouse.fa") as fa:
    mouse = fa.read()
with open("RandomSeq(1).fa") as fa:
    random = fa.read()
edit_distance = 0
for i in range(len(human)): 
    if human[i]!=mouse[i]:
      edit_distance += 1 
print("the edit distance between human and mouse sequences is " + str(edit_distance))
edit_distance = 0
for i in range(len(random)): 
    if random[i]!=human[i]:
      edit_distance += 1
print("the edit distance between human and random sequences is " + str(edit_distance))
edit_distance = 0
for i in range(len(random)): 
    if random[i]!=mouse[i]:
      edit_distance += 1
print("the edit distance between mouse and random sequences is " + str(edit_distance))
