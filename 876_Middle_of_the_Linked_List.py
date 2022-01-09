from typing import  Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mid = head
        while head:
            head = head.next
            if head:
                head = head.next
            else:
                return mid
            mid = mid.next
        return mid
