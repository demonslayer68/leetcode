# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        size = 0
        while temp:
            size += 1
            temp = temp.next
        if not size:
            return head

        endindex = size - k + 1
        i = 1
        tempstart = head
        while i < k:
            i += 1
            tempstart = tempstart.next
        i = 1
        tempend = head
        while i < endindex:
            i += 1
            tempend = tempend.next

        val = tempstart.val
        tempstart.val = tempend.val
        tempend.val = val

        return head
