#'---
#' title: RNA Variant Calling
#' author: mumichae
#' wb:
#'  log:
#'    - snakemake: '`sm str(tmp_dir / "RVC" / "overview.Rds")`'
#'  params:
#'    - groups: 'sm cfg.RVC.groups'
#' output:
#'  html_document
#'---

saveRDS(snakemake, snakemake@log$snakemake)

# Obtain the annotations and datasets
datasets <- snakemake@params$groups

#' datasets: `r datasets`
