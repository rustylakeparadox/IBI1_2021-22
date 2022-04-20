def Nucleotide_ontent_calculator():
    genes = input("the single strand is ")
    genes = genes.swapcase()
    total = len(genes)
    pc_A = genes.count("A")/total
    pc_G = genes.count("G")/total
    pc_C = genes.count("C")/total
    pc_T = genes.count("T")/total
    return pc_A, pc_G, pc_C, pc_T

Nucleotide_ontent_calculator()
#input 'acGTAgT'
##(0.14285714285714285, 0.14285714285714285, 0.14285714285714285, 0.0)
