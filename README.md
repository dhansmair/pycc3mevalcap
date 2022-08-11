Image Captioning Evaluation Tools
===================

Fork of salaniz/pycocoevalcap, with additional support of image captioning metrics on the Conceptual Captions (3M) dataset.


## Installation ##
To install pycc3mevalcap and all dependencies, run:
```
git clone https://github.com/dhansmair/pycc3mevalcap.git
cd pycc3mevalcap
pip install .
```

## Usage ##

Basic usage:
```python
import json
from pycc3mevalcap import EvalCap, load_cc3m_references

# file.json is expected to contain a dictionary of {image_id: caption_prediction}
with open('path/to/your/candidate/file.json', 'r') as f:
    candidates_data = json.load(f)

annotation_data = load_cc3m_references()
eval_cap = EvalCap(annotation_data)
metrics = eval_cap.evaluate(candidates_data)
print(metrics)
```
See the example scripts: [example/coco_eval.py](example/coco_eval.py), [example/cc3m_eval.py](example/cc3m_eval.py)  


## Additional Information ##
please refer to [https://github.com/salaniz/pycocoevalcap](salaniz/pycocoevalcap) for details regarding scorers, tokenizer etc.
