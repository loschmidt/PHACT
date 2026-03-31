import os
import sys
def get_fasta_dict(fasta_file):
    fasta_dict = {}
    
    with open(fasta_file,'r') as f:
        for line in f:
            if line.startswith('>'):
                line = line[0] + line[1:].replace('>', '-') 
                header = line.split(">")[1].strip()
                fasta_dict[header] = ''
            else:
                fasta_dict[header] += line.strip()
            
    f.close()

    return fasta_dict


def iter_fasta(fasta_file):
    header = None
    seq_parts = []
    with open(fasta_file) as f:
        for line in f:
            if line.startswith(">"):
                if header is not None:
                    yield header, ''.join(seq_parts)
                header = (line[0] + line[1:].replace('>', '-')).split(">")[1].strip()
                seq_parts = []
            else:
                seq_parts.append(line.strip())
    if header is not None:
        yield header, ''.join(seq_parts)


if __name__ == "__main__":
    fasta_file  = sys.argv[1]
