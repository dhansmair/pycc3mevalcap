from typing import Dict, List, Union
from pycocoevalcap.tokenizer.ptbtokenizer import PTBTokenizer
from pycocoevalcap.bleu.bleu import Bleu
from pycocoevalcap.meteor.meteor import Meteor
from pycocoevalcap.rouge.rouge import Rouge
from pycocoevalcap.cider.cider import Cider
from pycocoevalcap.spice.spice import Spice


class EvalCap:
    """ evaluator class for common image captioning metrics. 

    Uses metric implementations from the pycocoevalcap package.
    Available metrics: BLEU, METEOR, ROUGE_L, CIDEr, SPICE
    Expected references format:
        dictionary where keys are image ids and values are lists of captions
    Expected candidates format:
        dictionary where keys are image ids and values are your predicted candidates
    
    """
    def __init__(self, references: Dict[str, List[str]]):
        """ constructor.
        
        Args:
            references: dictionary {image_id : [caption]}
                keys are the image_ids, value a list of one or more reference captions
            
        Raises:
            AssertionError: raised if references parameter fails sanity check
        """
        
        # sanity check
        for k, v in references.items():
            assert isinstance(k, str) or isinstance(k, int), 'image ids must be strings or ints'
            assert isinstance(v, list), 'references must be a list'
            assert all(isinstance(caption, str) for caption in v)

        refs = {}
        for k, ref_list in references.items():
            refs[k] = [{'caption':cap} for cap in ref_list]

        self.tokenizer = PTBTokenizer()
        self.tokenized_references = self.tokenizer.tokenize(refs)

        self.scorers = {
            'BLEU': Bleu(4),
            'METEOR': Meteor(),
            'ROUGE_L': Rouge(),
            'CIDEr': Cider(),
            'SPICE': Spice(),
        }
    
    def evaluate(
        self, 
        candidates: Dict[str, str], 
        metrics=('BLEU', 'METEOR', 'ROUGE_L', 'CIDEr', 'SPICE')
    ) -> Dict[str, Union[float, List[float]]]:
        """ evaluate various metrics on the candidate captions.
        
        This function will only consider those reference strings for which a candidate caption is given.
        Available metrics: 'BLEU', 'METEOR', 'ROUGE_L', 'CIDEr', 'SPICE'
        
        Args:
            candidates: dictionary {image_id : caption} 
            metrics: tuple of metrics you want to have evaluated.
            
        Returns:
            dictionary {metric_name : result} 
            Will contain a score of -1.0 if evaluation of the respective metric fails.
        """

        # sanity check
        assert isinstance(candidates, dict), "candidates must be a Dict[str, str]"
        for k, v in candidates.items():
            assert isinstance(k, str) or isinstance(k, int), 'image ids must be strings or ints'
            assert isinstance(v, str), 'candidates must be a string'

        # this is the format the tokenizer requires
        # for references, only filter the ones that appear in the candidate list.
        cands, refs = {}, {}
        for k, v in candidates.items():
            cands[k] = [{'caption':v}]
            refs[k] = self.tokenized_references[k]

        tokenized_candidates = self.tokenizer.tokenize(cands)
        result = {}

        for metric in metrics:
            if metric not in self.scorers:
                print(f'warning: unknown metric {metric}, cannot evaluate. Possible metrics: {self.scorers.keys()}')
                result[metric] = None
            else:
                try:
                    scorer = self.scorers[metric]
                    score, scores = scorer.compute_score(refs, tokenized_candidates)
                    result[metric] = score
                except Exception as e:
                    print(f'info: failed to evaluate {metric}. There was the following exception:')
                    print(e)
                    result[metric] = -1.0
            
        print('scoring done.')
            
        return result
