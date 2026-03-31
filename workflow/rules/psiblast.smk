rule psiblastp:
    input:
        query_fasta = "{workdir}/{query_id}.fasta"
    output:
        outfile = "{workdir}/results/{query_id}/1_psiblast/{query_id}_blasthits.out"
    params:
        blastdb = expand("{mount_dir}/{blastdb_folder}/{blastdb}", mount_dir=config["mount_dir"], blastdb_folder=config["blastdb_folder"], blastdb=config["blastdb_file"]),
    log:
        "{workdir}/logs/rules/{query_id}_psiblastp.err"
    benchmark:
        "{workdir}/logs/benchmarks/{query_id}_psiblastp.out"
    conda:
        "../envs/blastp.yml"
    shell:
        "psiblast -query {input.query_fasta} -db {params.blastdb} -outfmt {config[outfmt]} -out {output.outfile} -max_target_seqs {config[max_target_seqs]} -num_iterations {config[num_iterations]} -evalue {config[max_e_value]} 2> {log}"
