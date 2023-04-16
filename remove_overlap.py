#python remove_overlap.py DDGun-Ptmul PoPMuSiC-S2648 30

import os, sys
import pandas as pd
import numpy as np

path = '~/Documents/WRK/datasets_2023.03.06/PROCESSED' # set the path here
blast_file = os.path.join(path, 'blast.tsv')
blast = pd.read_table(blast_file)

def RemoveOverlap(dataset1, dataset2, pident=25):
    
    '''
    Removes mutations from dataset1 in proteins that are similar to those in dataset2 by more than pident % of sequence identity.
    RemoveOverlap('DDGun-Ptmul', 'PoPMuSiC-S2648', 30) will produce dataset DDGun-Ptmul__PoPMuSiC-S2648__30.tsv 
    that contains mutations from the dataset DDGun-Ptmul in proteins that are similar to proteins from the dataset PoPMuSiC-S2648 
    at maximum by 30% of sequence identity.
    '''
    
    ### LOAD DATASET ###
    
    # function that generates dataset id
    def Id(lst):
        return ';'.join([i if pd.isna(i) == False else '' for i in lst])
    # load dataset to remove overlaps from
    dataset1_file = os.path.join(path, dataset1 + '.tsv')
    dataset1_data = pd.read_table(dataset1_file)
    # create id column
    id_columns = [i for i in dataset1_data.columns if i in ['pdb', 'chain', 'uniprot', 'WT_name']]
    dataset1_data['id'] = dataset1_data.apply(lambda x: Id([x[i] for i in id_columns]), axis=1)

    ### LOAD OVERLAPS DATA ###
    
    # load blast 
    blast_file = os.path.join(path, 'blast.tsv')
    blast = pd.read_table(blast_file)
    # select data on overlaps between dataset1 and dataset2
    data = blast[(blast['dataset2'] == dataset2) & (blast['dataset1'] == dataset1)]
    data = data.sort_values("pident")[::-1]

    ### REMOVE OVERLAPS ###
    
    # select protein pairs with sequence identity more than threshold
    overlap = data[data['pident'] > int(pident)].loc[:, ['id1', 'id2']]
    # select names of the proteins in dataset1
    overlaping_proteins = overlap['id1'].unique()
    # save the list of overlaping proteins
    overlap.to_csv('overlap_proteins.tsv', sep='\t', index=False, header=None)
    # if no overlap - print log and do nothing
    if len(overlaping_proteins) == 0:
        print(f'No overlap at {pident}% cutoff.')
    else: # if overlap
        # remove mutations in these proteins from dataset1
        dataset1_data_no_overlap = dataset1_data[~dataset1_data['id'].isin(overlaping_proteins)]
        # if everything overlaps - print log and do nothing
        if len(dataset1_data_no_overlap) == 0:
            print(f'All data overlap at {pident}% cutoff.')
        else:
            # save dataset1 without overlaps with dataset2
            file_name = '__'.join([dataset1, dataset2, str(pident)])
            dataset1_data_no_overlap.drop(columns='id').to_csv(file_name+'.tsv', sep='\t', index=False)

            ### PRINT LOG ###

            n_before = len(dataset1_data)
            n_after = len(dataset1_data_no_overlap)
            print(f'Percent of overlapping data: {(n_before-n_after)/n_before:.1%}')

dataset1 = str(sys.argv[1])
dataset2 = str(sys.argv[2])
pident = str(sys.argv[3])

RemoveOverlap(dataset1, dataset2, pident)
