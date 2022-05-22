# Leetcode notes

### General notes
- Refer to the Utilities script for generic python syntax
- Write the if else blocks in order of usage, to further minimize runtime
- Generally try to use local variables for dp
- If you use class variables for dp, you should reinitialize it inside the main func, in case multiple test cases are run using the same class instance
- Use a deque(doubly ended queue) for stack, heap, queue problems( it has O(1) access time ) - [deque](https://www.geeksforgeeks.org/deque-in-python/)
- Bitwise operators are explained [here](https://www.geeksforgeeks.org/python-bitwise-operators/)
- x // y gives floor division. You can do -(-x // y) to get ceil.
- iterating through dict
  - use for i in dict to get keys
  - use for i in dict.values() to get values
  - use key, value in dict.items() to get the pairs

### data structures
- you can add a default value for a dict using: cont.get(value, 0)
  - This is a replacement for defaultdict()
- Use a Trie for dictionary / word storage type problems: [example here](https://leetcode.com/problems/design-add-and-search-words-data-structure/submissions/)

### DP
- Recursive is always top -> bottom, iterative is generally bottom -> top
- In some cases where number of calls is extremely high, iteration works much faster than recursion. Example [here](https://leetcode.com/problems/jump-game/).

### Tree / matrix / graph
- The usual default method for matrix problems is DFS/BFS
- Use a global variable to track visited / modified nodes: [example](https://leetcode.com/problems/set-matrix-zeroes/)
- if a process has n states, use new state = state + n along with (new state % n ) to store old and new without using additional space like [here](https://leetcode.com/problems/game-of-life/)
- basic graph algorithms
  - DFS
  - BFS
  - flood fill
  - [union find](https://www.youtube.com/watch?v=mHz-mx-8lJ8)
  - topological sort
    - there are 2 ways to do topological sort:
      1) Do a dfs like recursion. Append all nodes which have no leaves. reverse the list in the end. code [here](https://www.geeksforgeeks.org/topological-sorting/)
      2) maintain a queue of root nodes and iteratively remove edges and add new root nodes like [here](https://stackoverflow.com/questions/4168/graph-serialization/4577#4577)

### Bit manipulation
- bit manipulation has 4 basic operations
  - AND: 0011 & 0110 = 0010
  - OR: 0011 | 0110 = 0111
  - NOT: 10 = 1010. !1010 = 10101 = (-16 + 4 + 1 ) = -11(includes reversing the first sign bit)
    - the easiest way to get NOT of a number is (-(x+1)). example(-(10+1)) for above
  - XOR: 0110 ^ 0011 = 0101
    - the use of XOR is to get the original number back. if x = a ^ b. a = x ^ b and b = x ^ a
  - more detail [here](https://www.geeksforgeeks.org/python-bitwise-operators/)

### Hashing
There are some interesting things on hashing [here](https://en.wikipedia.org/wiki/Hash_table#Open_addressing), [here](https://leetcode.com/problems/design-hashset/solution/) and [here](https://leetcode.com/problems/design-hashmap/solution/)
Mainly, implement a hash table using a large key for modulo(preferable primary number)