# Leetcode notes

### General notes
- Refer to the Utilities script for generic python syntax
- Write the if else blocks in order of usage, to further minimize runtime
- Generally try to use local variables for dp
- If you use class variables for dp, you should reinitialize it inside the main func, in case multiple test cases are run using the same class instance
- Use a deque(doubly ended queue) for stack, heap, queue problems( it has O(1) access time ) - [deque](https://www.geeksforgeeks.org/deque-in-python/)
- Bitwise operators are explained [here](https://www.geeksforgeeks.org/python-bitwise-operators/)

### DP
- Recursive is always top -> bottom, iterative is generally bottom -> top
- In some cases where number of calls is extremely high, iteration works much faster than recursion. Example [here](https://leetcode.com/problems/jump-game/).

## Tree / matrix / graph
- The usual default method for matrix problems is DFS/BFS
- Use a global variable to track visited / modified nodes: [example](https://leetcode.com/problems/set-matrix-zeroes/)
- if a process has n states, use new state = state + n along with (new state % n ) to store old and new without using additional space like [here](https://leetcode.com/problems/game-of-life/)
- basic graph algorithms
  - DFS
  - BFS
  - flood fill
  - [union find](https://www.youtube.com/watch?v=mHz-mx-8lJ8)