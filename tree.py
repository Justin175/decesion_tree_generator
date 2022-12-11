from typing import Any
from utils import OPERATORS, RL_OPERATORS

class DecisionNode:
    _value : Any
    _id : int
    _depth : int

    _parent : Any = None # Node
    _left : Any = None # Node
    _right : Any = None # Node
    _priority : int # None if variable
    _is_rl_operator : bool
    _tree : Any

    def __init__(self, value, tree, depth = 0, id = 0) -> None:
        self._value = value
        self._priority = OPERATORS.get(value, None)
        self._id = id
        self._depth = depth
        if self._priority is not None:
            self._priority -= (depth * 100)
        self._is_rl_operator = value in RL_OPERATORS
        self._tree = tree

    def get_value(self) -> Any:
        return self._value

    def is_rl_operator(self) -> bool:
        return self._is_rl_operator

    def get_left(self) -> Any:
        return self._left

    def get_right(self) -> Any:
        return self._right

    def get_parent(self) -> Any:
        return self._parent

    def get_id(self) -> int:
        return self._id

    def get_priority(self) -> int:
        return self._priority

    def set_right(self, right : Any):
        self._right = right
        right.set_parent(self)

    def set_left(self, left : Any):
        self._left = left
        left.set_parent(self)

    def set_parent(self, parent : Any):
        self._parent = parent

    def _rot_left(self, node):
        if self._parent is None:
            self._tree.set_root(node)
        else:
            self._parent.set_right(node)
        node.set_left(self)

    def _switch_root(self, node):
        if self._parent is None:
            self._tree.set_root(node)
        else:
            self._parent.set_right(node)
        node.set_left(self)

    def insert(self, node):
        if self._priority is None: # node is an OPERATOR
            self._switch_root(node)
        elif node.get_priority() is None: # node is a VAR, therefor self is a OPERATOR
            if self._right is None:
                self.set_right(node) # set in right leaf
            else: # right is a OPERATOR, insert it
                self._right.insert(node)
        else: # node is a OPERATOR
            # check the precedence...
            if node.get_priority() >= self._priority: # set as new parent
                self._switch_root(node)
            else: # insert right
                if self._right is None: # if right is None, then set it
                    self.set_right(node)
                else:
                    self._right.insert(node)

    def __repr__(self) -> str:
        return f"[value={self._value}, left={self._left}, right={self._right}]"

    def print_mermaid_str(self) -> str:
        print(f"{self._id}({self._value})")

        if self._parent is not None:
            print(f"{self._parent.get_id()} --> {self._id}")
        
        if self._left is not None:
            self._left.print_mermaid_str()

        if self._right is not None:
            self._right.print_mermaid_str()


class DecisionTree:
    _root : DecisionNode = None
    _right : DecisionNode = None
    _next_id : int = 0
    _depth = 0

    def __init__(self) -> None:
        pass

    def insert(self, value : str):
        if value == "(":
            self._depth += 1
            return
        if value == ")":
            self._depth -= 1
            return
        
        node = DecisionNode(value, self, self._depth, self._next_id)
        self._next_id += 1

        if self._root is None: # if tree is empty
            self._root = node
            return

        self._root.insert(node)

    def set_root(self, root : DecisionNode):
        self._root = root

    def print_mermaid_str(self):
        print("graph TD")
        if self._root is not None:
            self._root.print_mermaid_str()

    def __repr__(self) -> str:
        return f"Tree [{self._root}]"


        
        

