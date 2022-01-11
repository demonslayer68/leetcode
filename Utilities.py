# convert binary to int
import typing

a = int('101', 2)
print(a)

# convert int to binary
a = bin(5)
print(a)

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

# reverse an iterable
s = "abdc"
print(s[::-1])

#List with default values
s = typing.DefaultDict(int)
print(s[0]) # gives 0
s = typing.DefaultDict(list)
s["gasd"].append(89)

print(s) # gives 0
