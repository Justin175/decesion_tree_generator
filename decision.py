from tree import DecisionTree, DecisionNode

def parse_condition(cond : str) -> DecisionTree:
    # after '(' following a non operator => Function call
    # add ' ' before and after all '(' and ')'
    gen = (x if x not in "()" else f" {x} " for x in cond)

    tree = DecisionTree()
    is_operator : bool = False
    last_node : DecisionNode = None
    comp_it = filter(lambda x: len(x) > 0, "".join(gen).split(" "))

    for a in comp_it:
        if a == "(" and not is_operator: # Function-Call
            cur_value = last_node.get_value() + "("
            # search for ')'
            cur_opend = 1
            while cur_opend > 0:
                b = next(comp_it)
                if b == "(":
                    cur_opend += 1
                elif b == ")":
                    cur_opend -= 1
                
                cur_value += b

            last_node.set_value(cur_value)
            continue

        last_node = tree.insert(a)
        is_operator = last_node is not None and last_node.get_priority() is not None

    return tree
