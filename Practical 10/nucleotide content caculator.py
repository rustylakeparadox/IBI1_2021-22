def Nucleotide_ontent_calculator():     # create a function
    genes = input("the single strand is ")     # imput the viriable "genes"
    genes = genes.swapcase()                   # swift all the strings into capital letters
    total = len(genes)                         # count the number of the nucleotides
    # caculate the percentage of each kind of nucleotide seperately
    pc_A = genes.count("A")/total               
    pc_G = genes.count("G")/total
    pc_C = genes.count("C")/total
    pc_T = genes.count("T")/total
    return pc_A, pc_G, pc_C, pc_T               # return the outcomes

# give an example
Nucleotide_ontent_calculator()      # call the function
#input 'acGTAgT'
##(0.14285714285714285, 0.14285714285714285, 0.14285714285714285, 0.0)
