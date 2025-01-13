This branch contains simple server wrapper around the RemoveOverlap function

Sample request to server:
```json
{
  "dataset1_name": "DDGun-Ptmul",
  "dataset1_file": [
  {
    "_id": "63d8e6bc4b6a130dc44ac5bb",
    "hash": "0060f6fec0cdcc3d3396fb314be3b0c9",
    "mutation": "I30F/I36L",
    "ddG": "3.32",
    "organism": "Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast)",
    "protein": "Polyubiquitin",
    "pdb": "1OTR",
    "chain": "B",
    "uniprot": "P0CG63",
    "__v": 0
  },
  {
    "_id": "63d8e6bc4b6a130dc44ac647",
    "hash": "006bc2d76457ef6ad0eedc7cefc2a19f",
    "mutation": "Y8F/K13Y/K54F/Y52F",
    "ddG": "-0.07",
    "organism": "Gallus gallus (Chicken)",
    "protein": "Spectrin alpha chain, non-erythrocytic 1",
    "pdb": "1SHG",
    "chain": "A",
    "uniprot": "P07751",
    "__v": 0
  },
  ...,
  {
    "_id": "63d8e6bc4b6a130dc44ac5d7",
    "hash": "0149faef89955a7153c7914c2f1c59bd",
    "mutation": "I6E/T53R",
    "ddG": "-1.76",
    "organism": "Streptococcus sp. group G",
    "protein": "Immunoglobulin G-binding protein G",
    "pdb": "1PGA",
    "chain": "A",
    "uniprot": "P06654",
    "__v": 0
  },
],
  "dataset2_name": "PoPMuSiC-S2648",
  "pident": 30
}
```

To speed up data transfer, when sending dataset1_data_no_overlap_hashes, we send just hashes from db. We need this also to process large datasets like MegaDataset

Sample response:
```json
{
  "all_overlap": false,
  "dataset1_data_no_overlap_hashes": [
    "07537f6ede6668a0132833b9474e6713","0bce38ac07237c6e3dc02e491d9430e6", ...,"0e8ca0adff68ebc7efdb7025314e1824",
  ],
  "is_no_overlap_in_file": false,
  "no_overlap": false,
  "overlapping_proteins":
    [
      {"id1":"2TRX;A;P0AA25","id2":"2TRX;A;P0AA25"},
      {"id1":"2RN2;A;P0A7Y4","id2":"2RN2;A;P0A7Y4"},
      {"id1":"1HTI;A;P60174","id2":"1HTI;A;P60174"},
      {"id1":"1HK0;X;P07320","id2":"1HK0;X;P07320"},
      {"id1":"1HME;A;P63159","id2":"1HME;A;P63159"},
      ...,
      {"id1":"1LVE;A;P06312","id2":"1LVE;A;P06312"}
    ],
  "percent_of_overlapping": 0.8862144420131292
}
```