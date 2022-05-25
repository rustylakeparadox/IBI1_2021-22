# import
from xml.dom.minidom import parse
import xml.dom.minidom
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

# input the file and extract its elements
go_obo = xml.dom.minidom.parse("go_obo.xml")
collection = go_obo.documentElement
# extract all the terms
terms = collection.getElementsByTagName("term")

# create new dictionaries
nodes = {}
result_all = {}

# create a function to find all the childNodes of a node
# this function will run continuously until it finds all the childnodes
def find_parents(node_id, parent_id):
    mediate_ids = nodes[node_id]
    for mediate_id in mediate_ids: 
        parent_id.add(mediate_id)  # get the ids of parentNodes
        find_parents(mediate_id, parent_id)

# find all the nodes of every term
for term in terms:  
    node_id = term.getElementsByTagName("id")[0].childNodes[0].data       
    mediate_ids = []              # create a new dictionary to store mediate info.  
    for is_a in term.getElementsByTagName("is_a"): 
        mediate_ids.append(is_a.childNodes[0].data) 
    nodes[node_id] = mediate_ids   # store the info. in "nodes"
    result_all[node_id] = 0      # let "result_all" have the length of nodes but all the values set to be 0

# calculate the number of parentNodes for every childNode 
for key in nodes.keys():
  parent_ids = set()
  find_parents(key, parent_ids)    # use the function created before to find parentNodes
  for parent_id in parent_ids:
    result_all[parent_id] += 1      # store the numbers

# draw the boxplot to show the distribution of child nodes in all terms
plt.boxplot(result_all.values(), vert=True, showbox=True, showcaps=True, showfliers=True)
plt.title('The distribution of child nodes in all terms')
plt.xlabel("All terms")
plt.ylabel("The number of childnodes of all terms")
plt.show()

# get the list of terms about 'translation'.
term_list = []   # create a new dictionary
for term in terms:
      text = term.getElementsByTagName("defstr")[0].childNodes[0]
      if 'translation' in text.data:
          term_list.append(term)   # store the "translation" terms in "term_list"

# find the nodes about 'translation' in all the nodes
node_list = []    # create a new dictionary
for term in term_list:  
    node_id = term.getElementsByTagName("id")[0].childNodes[0].data 
    node_list.append(node_id)      # store the "translation" nodes in "node_list"

# create a new dictionary
term_translation = []
for node in node_list:
      term_translation.append(result_all[node])  # store the number of 'translation' nodes

# draw the boxplot plot of the distribution of child nodes throughout the terms about translation
plt.boxplot(term_translation, vert=True, showbox=True, showcaps=True, showfliers=True)
plt.title('The distribution of child nodes throughout the terms about translation ')
plt.xlabel("Terms about translation")
plt.ylabel("number of childnodes of terms about translation")
plt.show()


# calculate the average number of overall terms and 'translation' terms
average_all= sum(result_all.values())/len(result_all.values())
average_translation= sum(term_translation)/len(term_translation)

# print out the answers
print("The overall terms have", average_all, "child nodes on average.")
print("The 'translation' terms have", average_translation, "child nodes on average.")
# judge which number is bigger and print out the answer
if average_all > average_translation:
   print("The 'translation' terms have a greater number of child nodes than the overall terms.")
else:
   print("The overall terms have a greater number of child nodes than the 'translation' terms.")
