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

bedingung  = "(((x eq 1) or (x eq 2)) and ((y eq 3) or (y eq 4)))"
bedingung2 = "((x eq 1 or x eq 2) and (y eq 3 or y eq 4))"

def _search_all(cond) -> List[Tuple[int, str]]:
    ops = []
    index = 0
    while (op := re.search(OPERATORS_RE, cond)) is not None:
        ops.append((index, op))
        index += 1
        cond = cond[op.span()[1]:]
    return ops
    
def break_conditions(tokens : List[List]) -> List[List]:
    for depth, cond in tokens:
        conditions = _search_all(cond)
        if conditions is None or len(conditions) <= 1:
            continue

        # add ()
        print(conditions)



    return tokens

def parse_condition(cond : str, depth = 0) -> Dict:
    tree = {}

    tokens : List[List] = []
    last_was_block = False

    for char in cond:
        if char == '(':
            depth += 1
            last_was_block = True
        elif char == ')':
            depth -= 1
            last_was_block = True
        else:
            if last_was_block:
                tokens.append([depth, char])
            else:
                tokens[-1][1] += char
            last_was_block = False

    # break down combinted conditions
    tokens = break_conditions(tokens)

    return tokens


tree = DecisionTree()
cond = "a eq 10 and b eq 10 and k eq 10 or z eq 11"
for a in cond.split(" "):
    tree.insert(a)

tree.print_mermaid_str()

# print("-------------------------------------")
# print(parse_condition(bedingung))
# print("-------------------------------------")
# print(parse_condition(bedingung2))