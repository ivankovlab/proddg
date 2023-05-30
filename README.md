# ProDDG - database of ∆∆G datasets and predictors


Access ProDDG: [ivankovlab.ru/proddg](https://ivankovlab.ru/proddg)

## About ProDDG

ProDDG is a web-service for developers, assessors and users of tools for predicting the effect of protein mutations. ProDDG provides all datasets on protein stability changes upon mutations (∆∆G) that were used for training, testing, and assessment of popular ∆∆G predictors.

ProDDG allows you to access and analyze ∆∆G data, compile leakage-free datasets for evaluating predictors, and discover the latest and most accurate ∆∆G predictors.

## Datasets

All ΔΔG datasets in ProDDG were processed to have a unified format. 

ΔΔG values are the folding free energy change of folding (negative values denote stabilization). 

All datasets obligatorily contain the following data: PDB, Chain, Protein, Gene, Uniprot ID, Uniprot, Organism, Mutation, ΔΔG, Wild-type sequence, Mutant sequence. Wild-type sequence is always provided, there is not a single entry without it, while other protein data may be absent (e.g. if there is no experimental structure available, PDB and Chain will be missing or if the protein is designed de novo, there will be no Uniprot data). If not provided in the original dataset, the wild-type sequence was retrieved from the SEQRES record of PDB structure. 

Additionally, some datasets may contain information about mutant structures, experimental conditions (pH, T), references, notes, and other information specific to the given dataset. Notes contain comments that were provided with the original dataset. If the entry in the original dataset contains erroneous data it will be stated in the Notes. 

Mutations have a standard format: < original amino acid >< position >< new amino acid >. Position numbering matches that in the wild-type sequence. If applicable, Mutation PDB is provided with the numbering corresponding to the stated PDB structure.

Check detailed description of columns and how data was derived: [Datasets](https://github.com/ivankovlab/proddg/blob/main/Datasets.md).

## Cite

If you used ProDDG in your work, please, cite us:

Marina A. Pak, Evgeny V. Kniazev, Igor D. Abramkin, Dmitry N. Ivankov. (2023). ProDDG - database of ∆∆G datasets and predictors. Available at: https://ivankovlab.ru/proddg.

