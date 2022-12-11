# All Operators...
# SEE https://cplusplus.com/doc/tutorial/operators/
OPERATORS = {
    "not": 3,   "!": 3,
    "<" : 5,
    "<=": 5,
    ">": 5,
    ">=": 5,
    "eq": 6,    "==": 6,
    "neq": 6,   "!=": 6,
    "and": 10,  "&&": 10,
    "or": 11,   "||": 11
}

# not listeted operators are LR (Left-Right) Operators
RL_OPERATORS = [
    "not", "!"
]