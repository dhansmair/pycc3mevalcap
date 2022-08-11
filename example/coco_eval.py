"""
using pycc3mevalcap to evaluate captions on MS COCO.
We use a different data format. load_coco_annotations() and load_coco_fakecaps()
are used to reformat the original coco data files.
"""
from os.path import dirname, abspath
import json
from pycc3mevalcap import EvalCap, load_coco_references


CURRENT_DIR = dirname(abspath(__file__))
candidates_file = CURRENT_DIR + '/captions_val2014_fakecap_results.json'


def load_coco_fakecaps(filename: str):
    with open(filename, 'r') as f:
        data = json.load(f)
    result = {}
    for inst in data:
        image_id = inst['image_id']
        caption = inst['caption']
        result[image_id] = caption
    return result


if __name__ == '__main__':
    annotation_data = load_coco_references()
    candidates_data = load_coco_fakecaps(candidates_file)
    
    eval_cap = EvalCap(annotation_data)
    metrics = eval_cap.evaluate(candidates_data)
    print(metrics)
    