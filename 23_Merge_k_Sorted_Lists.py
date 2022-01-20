# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None
        head = lists[0]
        for i in range(1, len(lists)):
            elem = lists[i]
            if not elem:
                continue
            if not head:
                head = elem
                continue
            pointer = head
            if elem.val < pointer.val:
                head = ListNode(elem.val, pointer)
                pointer = head
                elem = elem.next
            while elem:
                if not pointer.next:
                    pointer.next = elem
                    break
                if elem.val < pointer.next.val:
                    temp = elem.next
                    elem.next = pointer.next
                    pointer.next = elem
                    elem = temp
                pointer = pointer.next
        return head