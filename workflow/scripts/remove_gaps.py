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

def get_gap_positions(fasta_file, my_id):
    """Single pass — stop as soon as query sequence is found."""
    for header, seq in iter_fasta(fasta_file):
        if header == my_id:
            return {i for i, c in enumerate(seq) if c == "-"}
    raise ValueError(f"Query ID '{my_id}' not found in alignment FASTA.")


def write_new_fasta(fasta_file, gap_indices, leaves, output_file):
    """Single pass — stream, filter, transform, write. No dict stored."""
    with open(output_file, 'w') as out:
        for header, seq in iter_fasta(fasta_file):
            if header not in leaves:
                continue
            trimmed = ''.join(seq[i] for i in range(len(seq)) if i not in gap_indices)
            cleaned = re.sub(r'[BXJZUO#$]', '-', trimmed)
            if not all(c == "-" for c in cleaned):
                out.write(f">{header}\n{cleaned}\n")


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: script.py <query_file> <fasta_file> <tree_file> <output_file>")
        sys.exit(1)

    query_file  = sys.argv[1]
    fasta_file  = sys.argv[2]
    tree_file   = sys.argv[3]
    output_file = sys.argv[4]

    my_id       = get_my_id(query_file)
    gap_indices = get_gap_positions(fasta_file, my_id)

    leaves = {leaf.name for leaf in Tree(tree_file, format=1)}

    write_new_fasta(fasta_file, gap_indices, leaves, output_file)

