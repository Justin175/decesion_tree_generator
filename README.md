# Decesion-Tree-Builder

A small algorithm to build a decision tree out of c++-conditions.

Use this as follows:

```python
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
[![](https://mermaid.ink/img/pako:eNpNkE1uwkAMha8y8spIIGXyQ0gWXXEDuvTGZYaCIA4Nk0WLuHs9mShi589-z37yE46989DC98D3s_nck1iL_bAiKZDFrSKbzebDFFqh_4mDiS1JhhznE2YkOdps4ZyknhckfU1SJX89cUWyTYZq4i1JiV8LliTNu7zRxVnSN-m-XtzhdeGdCorkmBPbGLlEa2NrDq1rbY5_b50c1tD5oeOL0zc8SYwhCGffeYJWS-dPPN4CAclLpTyG_vArR2jDMPo1jHfHwe8vrA_soD3x7eFf_6TIXiE?type=png)](https://mermaid.live/edit#pako:eNpNkE1uwkAMha8y8spIIGXyQ0gWXXEDuvTGZYaCIA4Nk0WLuHs9mShi589-z37yE46989DC98D3s_nck1iL_bAiKZDFrSKbzebDFFqh_4mDiS1JhhznE2YkOdps4ZyknhckfU1SJX89cUWyTYZq4i1JiV8LliTNu7zRxVnSN-m-XtzhdeGdCorkmBPbGLlEa2NrDq1rbY5_b50c1tD5oeOL0zc8SYwhCGffeYJWS-dPPN4CAclLpTyG_vArR2jDMPo1jHfHwe8vrA_soD3x7eFf_6TIXiE)
