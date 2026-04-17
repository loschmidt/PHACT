def iter_fasta(fasta_file):
    with open(fasta_file) as f:
        header, seq_parts = None, []
        for line in f:
            line = line.rstrip()
            if line.startswith(">"):
                if header:
                    yield header, "".join(seq_parts)
                header, seq_parts = line[1:], []
            elif line:
                seq_parts.append(line)
        if header:
            yield header, "".join(seq_parts)
