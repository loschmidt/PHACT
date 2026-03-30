import re
import sys
from fasta_dict import *

def get_human_id(fasta_file):
    query_dict = get_fasta_dict(fasta_file)
    for k,v in query_dict.items():
        print(k)
        return k

get_human_id(sys.argv[1])
