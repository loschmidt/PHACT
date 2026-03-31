rule get_blasthits:
    input:
        query_fasta = "{workdir}/{query_id}.fasta",
        blastp_out = "{workdir}/results/{query_id}/1_psiblast/{query_id}_blasthits.out",
    output:
        blast_fasta = "{workdir}/results/{query_id}/1_psiblast/{query_id}_blasthits.fasta",
    params:
        blastdb = expand("{mount_dir}/{blastdb_folder}/{blastdb}",mount_dir=config["mount_dir"],blastdb_folder=config["blastdb_folder"],blastdb=config["blastdb_file"])
    resources:
        time_min=300
    conda:
        "../envs/python.yml"
    log:
        "{workdir}/logs/rules/{query_id}_get_blasthits.err"
    benchmark:
        "{workdir}/logs/benchmarks/{query_id}_get_blasthits.out"
    shell:
        "blastdbcmd -db {params.blastdb} -entry_batch {blastp_out} -out {blast_fasta} 2> {log}"