#python remove_overlap.py DDGun-Ptmul PoPMuSiC-S2648 30

import os, sys
import pandas as pd
import numpy as np
from flask import Flask, request
import json

app = Flask(__name__)

path = './' #'~/Documents/WRK/datasets_2023.01.01' # set the path here
blast_file = os.path.join(path, 'blast.tsv')
blast = pd.read_table(blast_file)

@app.post('/')
def RemoveOverlap():
    '''
    Removes mutations from dataset1 in proteins that are similar to those in dataset2 by more than pident % of sequence identity.
    RemoveOverlap('DDGun-Ptmul', 'PoPMuSiC-S2648', 30) will produce dataset DDGun-Ptmul__PoPMuSiC-S2648__30.tsv 
    that contains mutations from the dataset DDGun-Ptmul in proteins that are similar to proteins from the dataset PoPMuSiC-S2648 
    at maximum by 30% of sequence identity.
    '''
    
    ### PARSE REQUEST DATA
    req = request.json
    dataset1 = req['dataset1_name']
    # dataset1 = "DDGun-Ptmul"
    dataset1_file = req['dataset1_file']
    # dataset2 = "Myoglobin"
    dataset2 = req['dataset2_name']
    pident=req['pident']

    print(f'Requested comparison of {dataset1} and {dataset2} at {pident} pident')

    ### LOAD DATASET ###

    # load dataset to remove overlaps from
    if dataset1 == "MegaDataset":
        dataset1_file = os.path.join(path, 'MegaDataset_overlaps_subset.tsv')
        dataset1_data = pd.read_table(dataset1_file)
    else:
        dataset1_data = pd.DataFrame.from_dict(dataset1_file)
    
    # function that generates dataset id
    def Id(lst):
        return ';'.join([i if pd.isna(i) == False else '' for i in lst])
    # create id column
    id_columns = ['pdb', 'chain', 'uniprot', 'WT_name']
    dataset1_data['id'] = dataset1_data.apply(lambda x: Id([x[i] for i in id_columns if i in dataset1_data.columns]), axis=1)

    ### LOAD OVERLAPS DATA ###

    # select data on overlaps between dataset1 and dataset2
    data = blast[(blast['dataset2'] == dataset2) & (blast['dataset1'] == dataset1)]
    data = data.sort_values("pident")[::-1]

    ### REMOVE OVERLAPS ###

    # select protein pairs with sequence identity more than threshold
    overlap = data[data['pident'] > int(pident)].loc[:, ['id1', 'id2']]
    # select names of the proteins in dataset1
    overlapping_proteins = overlap['id1'].unique()

    response = {
      "no_overlap": False,
      "all_overlap": False,
      "overlapping_proteins": [],
      "percent_of_overlapping": 0,
      "dataset1_data_no_overlap_hashes": [],
      "is_no_overlap_in_file": False
    }

    # if no overlap - print log and do nothing
    if len(overlapping_proteins) == 0:
        response['no_overlap'] = True
        # print(f'No overlap at {pident}% cutoff.')
    else: # if overlap
        # remove mutations in these proteins from dataset1
        dataset1_data_no_overlap = dataset1_data[~dataset1_data['id'].isin(overlapping_proteins)]

        overlapping_proteins_dict = json.loads(overlap.to_json(orient='records'))

        # if everything overlaps
        if len(dataset1_data_no_overlap) == 0:
            response['all_overlap'] = True
            response['overlapping_proteins'] = overlapping_proteins_dict
            response['percent_of_overlapping'] = 1
            # print(f'All data overlap at {pident}% cutoff.')
        else:
            # create a list of hashes
            if (dataset1 == "MegaDataset"):
                dataset1_data_no_overlap_hashes = dataset1_data_no_overlap.drop(columns='id')['zenodo_index'].to_list()
            else:
                dataset1_data_no_overlap_hashes = dataset1_data_no_overlap.drop(columns='id')['hash'].to_list()
            response['dataset1_data_no_overlap_hashes'] = dataset1_data_no_overlap_hashes
            n_before = len(dataset1_data)
            n_after = len(dataset1_data_no_overlap)
            response['overlapping_proteins'] = overlapping_proteins_dict
            response['percent_of_overlapping'] = (n_before-n_after)/n_before

            ### PRINT LOG ###
            # print(f'Percent of overlapping data: {(n_before-n_after)/n_before:.1%}')
    return response

if __name__ == "__main__":
    from waitress import serve
    print('Starting application')
    serve(app, host="127.0.0.1", port=5000)
