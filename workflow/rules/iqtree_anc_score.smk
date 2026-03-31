rule iqtree_anc_score:
    input:
        tree_file = "{workdir}/results/{query_id}/7_iqtree_ancestral/{query_id}_nogap_msa.fasta.treefile",
        probabilities = "{workdir}/results/{query_id}/7_iqtree_ancestral/{query_id}_nogap_msa.fasta.state",
    output:
        "{workdir}/results/{query_id}/8_iqtree_ancestral_scores/{query_id}_wol_param_{pattern}.csv",
        "{workdir}/results/{query_id}/8_iqtree_ancestral_scores/{query_id}_wl_param_{pattern}.csv",
    params:
        out = "{workdir}/results/{query_id}/8_iqtree_ancestral_scores/{query_id}",
        fasta = "{workdir}/results/{query_id}/2_msa/{query_id}_nogap_msa_fasttree.fasta",
        query_fasta = "{workdir}/results/{query_id}/1_psiblast/{query_id}.fasta",
        query_id = "{query_id}"
    log:
        "{workdir}/logs/rules/{query_id}_iqtreeanc_{pattern}_compute_score.err"
    benchmark:
        "{workdir}/logs/benchmarks/{query_id}_iqtreeanc_{pattern}_compute_score.out"
    conda:
        "../envs/r-base.yml"
    shell:
        "Rscript {config[install_dir]}/workflow/scripts/ComputeScore_Nonnormal_withDiversity_0411.R {input.tree_file} {input.probabilities} {params.fasta} {params.out} {params.query_id} {config[weights]} 2>{log}"

