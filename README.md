# Decesion-Tree-Builder

A small algorithm to build a decision tree out of c++-conditions.

Use this as follows:

````python
# write a condition
condition = "a eq 10 and b eq 10 and k eq 10 or z eq 11"

# split the condition into the seperate parts and add
# every part to the tree

tree = DecisionTree()
for part in condition.split(" "):
    tree.insert(part)

# print the output => This could be used to generate a mermaid flow-chart
tree.print_mermaid_str()
```

From this condition the following chart is generated from mermaid:
![Exmample Diagramm](res/mermaid-example.png)
