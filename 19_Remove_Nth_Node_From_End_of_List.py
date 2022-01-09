from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = head
        delete = head
        while n > 0:
            head = head.next
            n -= 1
        if head:
            head = head.next
        else:
            return start.next
        while head:
            head = head.next
            delete = delete.next
        if delete.next:
            delete.next = delete.next.next
        return start
