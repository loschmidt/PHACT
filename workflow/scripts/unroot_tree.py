from ete3 import Tree
import os
import sys
from fasta_dict import *
import re
import ete3
from ete3 import Tree

def iter_fasta_headers(fasta_file):
    return map(lambda x: x[0], iter_fasta(fasta_file))


def unroot_tree(tree_file, no_gap_msa_file):
    t = Tree(tree_file, format=1)
    seq_headers = set(iter_fasta_headers(no_gap_msa_file))

    prune_list = filter(seq_headers.__contains__, t.get_leaf_names())

    t.prune(prune_list)
    t.unroot()
    t.write(outfile=tree_file + "_unrooted", format=1)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: script.py <tree_file> <no_gap_msa_file>")
        sys.exit(1)

    tree_file       = sys.argv[1]
    no_gap_msa_file = sys.argv[2]

    unroot_tree(tree_file, no_gap_msa_file)