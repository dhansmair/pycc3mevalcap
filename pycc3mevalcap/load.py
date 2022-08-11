""" 
utilities to load reference captions for coco and cc3m
"""
from typing import Dict, List
from os.path import dirname, abspath
import csv
import json


CURRENT_DIR = dirname(abspath(__file__))
COCO_REFERENCES = CURRENT_DIR + '/captions_val2014.json'
CC3M_REFERENCES = CURRENT_DIR + '/Validation_GCC-1.1.0-Validation.tsv'


def load_coco_references(path=COCO_REFERENCES) -> Dict[str, List[str]]:
    """ load references for ms coco 2014 validation split """
    result = {}
    with open(path, 'r') as f:
        data = json.load(f)

    for ann in data['annotations']:
        image_id = ann['image_id']
        caption = ann['caption']
        if image_id not in result:
            result[image_id] = []
        result[image_id].append(caption)
    return result


def load_cc3m_references(path=CC3M_REFERENCES) -> Dict[str, List[str]]:
    """ load references for conceptual captions 3M validation split.
    
    image_id is the index of the row in the csv file in this case.
    """
    result = {}
    with open(path) as f:
        read_tsv = csv.reader(f, delimiter="\t")
        for i, row in enumerate(read_tsv):
            caption = row[0]
            result[f'{i:08d}'] = [caption]
    return result