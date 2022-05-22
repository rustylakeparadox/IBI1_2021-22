from xml.dom.minidom import parse
import xml.dom.minidom
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
go_obo = xml.dom.minidom.parse("go_obo.xml")
collection = go_obo.documentElement
terms = collection.getElementsByTagName("term")

#Get the distribution of child nodes across terms.
number = []
for term in terms: 
    is_a = term.getElementsByTagName("is_a")
    node= len(is_a)
    number.append(node)
count = Counter(number)

value = list(count.values())
key = list(count.keys())
p1 = plt.bar(key,value)
plt.ylabel('the count of terms')
plt.xlabel('the number of childnodes of each term')
plt.title('The distribution of child nodes across all terms')
plt.show()

#Get the number of terms associated with 'translation'.
term_translation = []
for term in terms:
      defstr_text = term.getElementsByTagName("defstr")[0].childNodes[0]
      lines = defstr_text.data
      if 'translation' in lines:
          term_translation.append(term)
number2 = []
for term in term_translation:
    is_a2 =  term.getElementsByTagName("is_a")
    node2 = len(is_a2)
    number2.append(node2)

count2 = Counter(number2)
value2 = list(count2.values())
key2 = list(count2.keys())
p2 = plt.bar(key2,value2)
plt.ylabel('the count of terms')
plt.xlabel('the number of childnodes about translation')
plt.title('The distribution of child nodes across all terms about translation')
plt.show()
