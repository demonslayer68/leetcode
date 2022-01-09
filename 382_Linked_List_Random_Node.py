from typing import Optional
from random import randrange


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    start = ListNode()
    len = 1

    def __init__(self, head: Optional[ListNode]):
        self.start = head
        while head:
            self.len += 1
            head = head.next

    def getRandom(self) -> int:
        index = randrange(0, self.len-1)
        head = self.start
        while index > 0:
            head = head.next
            index -= 1
        return head.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
