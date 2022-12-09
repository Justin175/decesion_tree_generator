from typing import Any
from utils import OPERATORS

class DecisionNode:
    _value : Any
    _id : int

    _parent : Any = None # Node
    _left : Any = None # Node
    _right : Any = None # Node
    _priority : int # None if variable

    def __init__(self, value, id = 0) -> None:
        self._value = value
        self._priority = OPERATORS.get(value, None)
        self._id = id

    def get_value(self) -> Any:
        return self._value

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

    def insert_right(self, node):
        if self._left is None:
            if self._priority is None:
                # set new parent
                self._parent.set_right(node)
                node.set_right(self)
            else:
                self.set_left(node)
        elif self._right is None:
            self.set_right(node)
        else:
            if self._right.get_left() is None and self._parent is not None and node.get_priority() is not None and self._priority < node.get_priority(): # check for rotation
                self._parent.set_right(node)
                node.set_left(self)
            else:
                self._right.insert_right(node)

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

    def __init__(self) -> None:
        pass

    def insert(self, value, depth = 0):
        node = DecisionNode(value, self._next_id)
        self._next_id += 1

        print("---", value)
        if self._root is None: # if tree is empty
            self._root = node
            return

        if self._root.get_priority() is None: # added node must be an OPERATOR ==> new root
            node.set_left(self._root)
            self._root = node
        else: # add to right
            if node.get_priority() is not None and node.get_priority() > self._root.get_priority(): # also new root
                node.set_left(self._root)
                self._root = node
            else:
                self._root.insert_right(node)

    def print_mermaid_str(self):
        print("graph TD")
        if self._root is not None:
            self._root.print_mermaid_str()

    def __repr__(self) -> str:
        return f"Tree [{self._root}]"


        
        

