# Leetcode notes

### General notes
- refer to the Utilities script for generic python syntax
- write the if else blocks in order of usage, to further minimize runtime
- generally try to use local variables for dp
- if you use class variables for dp, you should reinitialize it inside the main func, in case multiple test cases are run using the same class instance
- use a deque(doubly ended queue) for stack, heap, queue problems( it has O(1) access time ) - [deque](https://www.geeksforgeeks.org/deque-in-python/)

### DP
- recursive is always top -> bottom, iterative is generally bottom -> top
- In some cases where number of calls is extremely high, iteration works much faster than recursion. Example [here](https://leetcode.com/problems/jump-game/).

