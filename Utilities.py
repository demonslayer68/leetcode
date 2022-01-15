import collections
import typing

# ternary operator
x = 222 if 0 else 111
print(x)

# comprehension
input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
list_using_comp = [var for var in input_list if var % 2 == 0]
print("Output List using list comprehensions:", list_using_comp)

input_list = [1, 2, 3, 4, 5, 6, 7]
dict_using_comp = {var: var ** 3 for var in input_list if var % 2 != 0}
print("Output Dictionary using dictionary comprehensions:", dict_using_comp)

# func def with default params and type enforced
def pick(l: "list of ints", index: int = 0) -> int:
    return l[index]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Definition for a linked list.
class LinkedList:
    def __init__(self, val=0, Next=None):
        self.val = val
        self.Next = Next


#deque(doubly ended queue)
q = collections.deque()
q.append(1)
x = q.popleft()

# reverse an iterable
s = "abdc"
print(s[::-1])

# List with default values
s = typing.DefaultDict(int)
print(s[0])  # gives 0
s = typing.DefaultDict(list)
s["gasd"].append(89)
print(s)  # gives 0

# convert int to binary
a = bin(5)
print(a)

# convert binary to int
a = int('101', 2)
print(a)

#list with same element repeated
steps = [-1] * 10

