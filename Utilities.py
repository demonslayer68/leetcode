import collections
import typing

# declaration
# tuple - immutable array. Faster more efficiet, speifically as dict key
a = (1, 2, 2, 3)
# list - mutable array
b = [1, 2, 2, 3]
# set - mutable unique elements. access is much faster
c = {1, 2, 3}
# dict - struct
d = { "a" : 1, "b" : 2}
type(d)
print(type(a), a, type(b), b, type(c), c, type(d), d)

### string operations
# split
s = 'a@bcx'
arr = s.split("@")

# remove all occurrences of a char
new_s = ''.join(s.split('-'))
new_s = new_s.upper()

#splice a string
new_s[i:i+k]    

### List operations
# reverse a string
list.reverse()

# sort a list based on another list
# below code sorts elements of Y based on X
[x for _, x in sorted(zip(X, Y) key=lambda pair: pair[0])]

### dict operations
# sort dict by values
sorted_ent = sorted(entropies, key=entropies.get, reverse=True)[:20]

# ternary operator
x = 222 if 0 else 111
print(x)

#min and max int
maxim = float('inf')
minim = float('-inf')

# comprehension
input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
list_using_comp = [var for var in input_list if var % 2 == 0]
print("Output List using list comprehensions:", list_using_comp)

# creating dict using comprehension

filtered_patterns = {key: value for key, value in patterns.items() if key in choices}

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

# list with same element repeated
steps = [-1] * 10

#### code snippets
# for a given arr, generate the next smallest element larger than element for each elem.
# i.e. index j such that i < j and arr[i] <= arr[j] and arr[j] is the smallest possible value.

arr = [10,13,12,14,15]
def getnext(sortedind):
    stack = []
    result = [None] * len(arr)
    for i in sortedind:
        while stack and i > stack[-1]:
            result[stack.pop()] = i
        stack.append(i)
    return result

sortedind = sorted(range(len(arr)), key=lambda x: arr[x])
next_largest = getnext(sortedind)
