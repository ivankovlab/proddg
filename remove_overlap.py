#python remove_overlap.py DDGun-Ptmul PoPMuSiC-S2648 30

import os, sys
import pandas as pd
import numpy as np

path = '~/Documents/WRK/datasets_2023.01.01' # set the path here
blast_file = os.path.join(path, 'blast.tsv')
blast = pd.read_table(blast_file)

def RemoveOverlap(dataset1, dataset2, pident=25):
    
    '''
    Removes mutations from dataset1 in proteins that are similar to those in dataset2 by more than pident % of sequence identity.
    RemoveOverlap('DDGun-Ptmul', 'PoPMuSiC-S2648', 30) will produce dataset DDGun-Ptmul__PoPMuSiC-S2648__30.tsv 
    that contains mutations from the dataset DDGun-Ptmul in proteins that are similar to proteins from the dataset PoPMuSiC-S2648 
    at maximum by 30% of sequence identity.
    '''
    
    dataset1_file = os.path.join(path, dataset1 + '.tsv')
    dataset1_data = pd.read_table(dataset1_file)
    dataset1_data['id'] = dataset1_data['pdb'] + '_' + dataset1_data['chain']

    data = blast[(blast['dataset2'] == dataset2) & (blast['dataset1'] == dataset1)]

    overlap = data.sort_values("pident")[::-1]
    overlap = overlap[overlap['pident'] > int(pident)].loc[:, ['pdbid1', 'pdbid2', 'pident']]
    overlapping_proteins = overlap.pdbid1.unique()

    if len(overlapping_proteins) == 0:
        print(f'No overlap at {pident}% cutoff.')
    else:
        overlap.to_csv('overlapping_proteins.tsv', sep='\t', index=False, header=False)
        overlapping_proteins = overlap.pdbid1.unique()

        dataset1_data_no_overlap = dataset1_data[~dataset1_data['id'].isin(overlapping_proteins)]
        if len(dataset1_data_no_overlap) == 0:
            print(f'All data overlap at {pident}% cutoff.')
        else:
            file_name = '__'.join([dataset1, dataset2, str(pident)])
            dataset1_data_no_overlap.drop(columns='id').to_csv(os.path.join(path, file_name+'.tsv'), sep='\t', index=False)

            n_before = len(dataset1_data)
            n_after = len(dataset1_data_no_overlap)
            print(f'Percent of overlapping data: {n_after/n_before:.1%}')

dataset1 = str(sys.argv[1])
dataset2 = str(sys.argv[2])
pident = str(sys.argv[3])

RemoveOverlap(dataset1, dataset2, pident)
