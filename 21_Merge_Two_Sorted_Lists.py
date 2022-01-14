# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val < list2.val:
            output = list1
            list1 = list1.next
        else:
            output = list2
            list2 = list2.next
        final = output
        while list1 or list2:
            if list1 and (not list2 or list1.val < list2.val):
                print(1)
                output.next = list1
                list1 = list1.next
                output = output.next
            else:
                print(2)
                output.next = list2
                list2 = list2.next
                output = output.next
        return final

