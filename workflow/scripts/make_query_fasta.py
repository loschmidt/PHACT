import os
import sys
import shutil

def make_query_fasta(acc_no,all_eu_file,output_path):

    protein_dict = {}

    with open(all_eu_file,'r') as f:
        for line in f:
            if line.startswith('>'):
                line = line[0] + line[1:].replace('>', '-') 
                header = line.split(">")[1].strip()
                if acc_no in header:
                    line = next(f).strip()
                    protein_dict[header] = ''
                    while not line.startswith('>'):
                        protein_dict[header] += line
                        try:
                            line = next(f).strip()
                        except:
                            break
    f.close()

    with open(output_path,'w') as f:
        for header,sequence in protein_dict.items():
            f.write(">"+header+"\n" + sequence + "\n")
    f.close()


if __name__ == "__main__":
#    print(sys.argv, file=sys.stderr)
    acc_no = sys.argv[1]
    all_eu_file = sys.argv[2]
    output_path = sys.argv[3]
    input_path = sys.argv[4]
    #make_query_fasta(acc_no,all_eu_file,output_path)
    shutil.copyfile(sys.argv[4] + "/" + acc_no + ".fasta", output_path) 


