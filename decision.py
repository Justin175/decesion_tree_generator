from tree import DecisionTree

def parse_condition(cond : str) -> DecisionTree:
    # add ' ' before and after all '(' and ')'
    gen = (x if x not in "()" else f" {x} " for x in cond)

    tree = DecisionTree()
    for a in filter(lambda x: len(x) > 0, "".join(gen).split(" ")):
        tree.insert(a)

    return tree

cond = "not ((a and b) or not (c and d)) neq (e < f)"
parse_condition(cond).print_mermaid_str()

