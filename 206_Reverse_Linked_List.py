from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        head2 = head
        while head2:
            next = head2.next
            head2.next = prev
            prev = head2
            head2 = next
        return prev