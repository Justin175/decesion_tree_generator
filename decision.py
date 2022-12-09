from typing import Dict, List, Tuple
import re
from utils import OPERATORS
from tree import DecisionNode, DecisionTree

def _get_operators_re() -> str:
    regex = ""

    for op in OPERATORS.keys():
        regex += op + "|"

    regex = regex[:-1]

    return re.compile(regex)

OPERATORS_RE = _get_operators_re()

def parse_condition(cond : str) -> DecisionTree:
    # add ' ' before and after all '(' and ')'
    n_condition = ""
    for a in cond:
        n_condition += f" {a} " if a in "()" else a 

    tree = DecisionTree()
    for a in filter(lambda x: len(x) > 0, n_condition.split(" ")):
        tree.insert(a)

    return tree

