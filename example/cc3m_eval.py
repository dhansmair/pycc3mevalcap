from os.path import dirname, abspath
import json
from pycc3mevalcap import EvalCap, load_cc3m_references


CURRENT_DIR = dirname(abspath(__file__))
candidates_file = CURRENT_DIR + '/cc3m_dummy_results.json'


def load_data(filename):
    with open(filename, 'r') as f:
        return json.load(f)
    

if __name__ == '__main__':
    annotation_data = load_cc3m_references()
    candidates_data = load_data(candidates_file)

    eval_cap = EvalCap(annotation_data)
    metrics = eval_cap.evaluate(candidates_data)
    print(metrics)