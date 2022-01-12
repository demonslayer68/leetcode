# Leetcode notes

### General notes
- refer to the Utilities script for generic python syntax
- write the if else blocks in order of usage, to further minimize runtime
- generally try to use local variables for dp
- if you use class variables for dp, you should reinitialize it inside the main func, in case multiple test cases are run using the same class instance

### DP
- recursive is always top -> bottom, iterative is generally bottom -> top
- In some cases where number of calls is extremely high, iteration works much faster than recursion. Example [here](https://leetcode.com/problems/jump-game/).

