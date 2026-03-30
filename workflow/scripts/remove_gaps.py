import os
import sys
from fasta_dict import *
import re
import ete3
from ete3 import Tree

def get_my_id(query_file):
    query_dict = get_fasta_dict(query_file)
    for k,v in query_dict.items():
        print(k)
        return k

def get_gap_positions(seqDict,my_id):
    for key, value in seqDict.items():
        if my_id == key:
            #print(value)
            return [i for i, x in enumerate(value) if x == "-"]
            #print(indices)

def get_sequences_without_gap(seqDict,indices):
    new_seqDict = {}
    for k,v in seqDict.items():
        #print(v)
        #print(new_seqDict)
        #print(indices)
        #print( [v[i] for i in range(len(v)) if i not in indices])       
        new_seqDict[k] = ''.join([v[i] for i in range(len(v)) if i not in indices])
        #print(new_seqDict)  
    return new_seqDict


def write_new_fasta(new_seqDict,fasta_file,tree_file,output_file):
    t = Tree(tree_file,format=1)
    leaves = []
    for leaf in t:
        leaves.append(leaf.name)
    with open (output_file,'w') as new_file:
        #print(new_file)
        for newheader,value in  new_seqDict.items():
            if newheader in leaves:
                new_value = re.sub(r'[BXJZUO#$]', '-',value)
                if not all([c=="-" for c in new_value]):
                    new_file.write(">" +newheader+"\n" + new_value+ "\n")
    new_file.close()



if __name__ == "__main__":
    query_file = sys.argv[1]
    fasta_file= sys.argv[2]
    tree_file= sys.argv[3]
    output_file= sys.argv[4]
    my_id= get_my_id(query_file)
    seqDict = get_fasta_dict(fasta_file)
    gap_indices = get_gap_positions(seqDict,my_id)
    new_seqDict = get_sequences_without_gap(seqDict,gap_indices)
    write_new_fasta(new_seqDict,fasta_file,tree_file,output_file)
