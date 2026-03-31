rule remove_gaps_fasttree:
    input:
        query_file = "{workdir}/{query_id}.fasta",
        msa_file = "{workdir}/{query_id}_msa.fasta",
        tree_file = "{workdir}/results/{query_id}/6_fasttree/{query_id}.nwk",
    output:
        no_gap_file = "{workdir}/results/{query_id}/2_msa/{query_id}_nogap_msa_fasttree.fasta",
    conda:
        "../envs/prune.yml"
    log:
        "{workdir}/logs/rules/{query_id}_remove_gaps.err"
    benchmark:
        "{workdir}/logs/benchmarks/{query_id}_remove_gaps.out"
    shell:
        "python3 {config[install_dir]}/workflow/scripts/remove_gaps.py {input.query_file} {input.msa_file} {input.tree_file}  {output.no_gap_file} 2> {log}"
