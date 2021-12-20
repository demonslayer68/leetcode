# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        out = ListNode()
        Temp = out
        done1 = 0
        done2 = 0
        carry = 0
        l1temp = l1
        l2temp = l2
        while not done1 or not done2 or carry:
            if not done1 and not done2:
                Sum = l1temp.val + l2temp.val + carry
                l1temp = l1temp.next
                l2temp = l2temp.next
            elif not done1:
                Sum = l1temp.val + carry
                l1temp = l1temp.next
            elif not done2:
                Sum = l2temp.val + carry
                l2temp = l2temp.next
            else:
                Sum = carry
            carry = int(Sum / 10)
            Sum = Sum % 10
            Temp.val = Sum
            Temp = Temp.next
            if not l1temp:
                done1 = 1
            if not l2temp:
                done2 = 1
            if not done1 or not done2 or carry:
                Temp.next = ListNode()
        return out
