from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        slow = head.next
        fast = head.next.next
        while fast and fast.next:
            if slow != fast:
                slow = slow.next
                fast = fast.next.next
            else:
                while head != slow:
                    head = head.next
                    slow = slow.next
                return head
        return None