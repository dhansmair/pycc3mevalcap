from pycc3mevalcap import EvalCap
from pycc3mevalcap import load_cc3m_references
from os.path import dirname, abspath
import json
import csv


# CURRENT_DIR = dirname(abspath(__file__))


# load reference captions from .tsv file
# annotation_file = CURRENT_DIR + '/Validation_GCC-1.1.0-Validation.tsv'
candidates_file = '/home/stud/hansmair/ma_flamingo/training/caption_predictions/candidates_baseline_run0.json'

# load results and annotations
def load_tsv(path: str) -> dict:
    data = {}
    
    with open(path) as f:
        read_tsv = csv.reader(f, delimiter="\t")
        for i, row in enumerate(read_tsv):
            caption = row[0]
            # url = row[1]
            data[f'{i:08d}'] = [caption]

    return data


def load_data(filename):
    with open(filename, 'r') as f:
        return json.load(f)
    
    
    
# cc3m example
# annotation_file = '/home/stud/hansmair/ma_flamingo/training/caption_predictions/val_references.json'

# annotation_data = load_tsv(annotation_file)
annotation_data = load_cc3m_references()
candidates_data = load_data(candidates_file)

eval_cap = EvalCap(annotation_data)
metrics = eval_cap.evaluate(candidates_data)
print(metrics)