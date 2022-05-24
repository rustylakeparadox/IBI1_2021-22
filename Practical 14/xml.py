from xml.dom.minidom import parse
import xml.dom.minidom
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
go_obo = xml.dom.minidom.parse("go_obo.xml")
collection = go_obo.documentElement
terms = collection.getElementsByTagName("term")

nodes = {}
result_all = {}

def find_parents(node_id, parent_id):
    mediate_ids = nodes[node_id]
    for mediate_id in mediate_ids:
        parent_id.add(mediate_id) 
        find_parents(mediate_id, parent_id)

for term in terms:  
    node_id = term.getElementsByTagName("id")[0].childNodes[0].data 
    mediate_ids = [] #对于父节点
    for is_a in term.getElementsByTagName("is_a"): 
        mediate_ids.append(is_a.childNodes[0].data) 
    nodes[node_id] = mediate_ids 
    result_all[node_id] = 0

for key in nodes.keys():
  parent_ids = set()
  find_parents(key, parent_ids)
  for parent_id in parent_ids:
    result_all[parent_id] += 1

plt.boxplot(result_all.values(), vert=True, showbox=True, showcaps=True, showfliers=True)
plt.title('The distribution of child nodes in all terms')
plt.xlabel("All terms")
plt.ylabel("The number of childnodes of all terms")
plt.show()

#Get the list of terms associated with 'translation'.
term_list = []
for term in terms:
      text = term.getElementsByTagName("defstr")[0].childNodes[0]
      if 'translation' in text.data:
          term_list.append(term)

#Find the nodes with translation in the nodefamily
node_list = []
for term in term_list:  
    node_id = term.getElementsByTagName("id")[0].childNodes[0].data 
    node_list.append(node_id)

term_translation = []
for node in node_list:
      term_translation.append(result_all[node])

#Draw the boxplot plot
plt.boxplot(term_translation, vert=True, whis=1.5, patch_artist=True, showbox=True, showcaps=True, showfliers=True)
plt.title('The distribution of child nodes across terms associated with translation ')
plt.xlabel("Terms associated with translation")
plt.ylabel("number of childnodes of terms with translation")
plt.show()


#Calculate the average number
average_all= sum(result_all.values())/len(result_all.values())
average_translation= sum(result_translation)/len(term_translation)
print("The overall terms have", average_all, "child nodes on average.")
print("The 'translation' terms have", average_translation, "child nodes on average.")

if average_all > average_translation:
   print("The 'translation' terms contain a greater number of child nodes than the overall terms.")
else:
   print("The overall terms contain a greater number of child nodes than the 'translation' terms.")
