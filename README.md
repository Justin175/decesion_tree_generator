# Decesion-Tree-Builder

A small algorithm to build a decision tree out of c++-conditions.

Use this as follows:

```python
from decision import parse_condition
# write a condition
condition1 = "not ((a and b) or not (c and d)) or (e < f)"
condition2 = "a = (1 + 2) * 3"

# split the condition into the seperate parts and add
# every part to the tree

tree1 = parse_condition(condition1)
tree2 = parse_condition(condition2)

# print the output => This could be used to generate a mermaid flow-chart
tree1.print_mermaid_str()
tree2.print_mermaid_str()
```

From condition1 the following chart is generated from mermaid:
[![](https://mermaid.ink/img/pako:eNpNkMFuwjAMhl8l8slIIDWhpVChnXgDdvTFa9yBRF3UpQeEePd5oap2ir9Pzi_bT2iHKNDA98j3i_s8kR5wGFekBeqQ7D24zebDFaTl7DOXpAFZo4kyi0DqkQ1DRk-6xa8Ft6TVnPdur0jr-X-VRU26w9awzrgj3WNccG_pHo_LON7yfYGy-vNvYxP6gN0_E2ANvYw9X6Mt-CR1jiBdpBeCxsooHU-3RED6slae0nB-aAtNGidZw3SPnOR0ZTtND03Htx95_QKEMlYE?type=png)](https://mermaid.live/edit#pako:eNpNkMFuwjAMhl8l8slIIDWhpVChnXgDdvTFa9yBRF3UpQeEePd5oap2ir9Pzi_bT2iHKNDA98j3i_s8kR5wGFekBeqQ7D24zebDFaTl7DOXpAFZo4kyi0DqkQ1DRk-6xa8Ft6TVnPdur0jr-X-VRU26w9awzrgj3WNccG_pHo_LON7yfYGy-vNvYxP6gN0_E2ANvYw9X6Mt-CR1jiBdpBeCxsooHU-3RED6slae0nB-aAtNGidZw3SPnOR0ZTtND03Htx95_QKEMlYE)

From condition2 the following chart is generated from mermaid:
[![](https://mermaid.ink/img/pako:eNo9zrEKgzAQBuBXCTelrYIa7RBoJ9-gHW85zFkFc4pNhiK-e4ODy_F_8MN_G3SzY7DwWWkZ1LtFKfXjglJoSrdUef5UBUqjrycbFKNvic1Bg1LpMtEcrFBqXZ2sUe7anOU7ZOB59TS6NLqhKIUQBvaMYFN03FOcAgLKnqoUw_z6SQc2rJEziIujwO1I6V0Ptqfpy_sfTm04jQ?type=png)](https://mermaid.live/edit#pako:eNo9zrEKgzAQBuBXCTelrYIa7RBoJ9-gHW85zFkFc4pNhiK-e4ODy_F_8MN_G3SzY7DwWWkZ1LtFKfXjglJoSrdUef5UBUqjrycbFKNvic1Bg1LpMtEcrFBqXZ2sUe7anOU7ZOB59TS6NLqhKIUQBvaMYFN03FOcAgLKnqoUw_z6SQc2rJEziIujwO1I6V0Ptqfpy_sfTm04jQ)