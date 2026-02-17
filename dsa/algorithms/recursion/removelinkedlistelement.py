# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head, val):
        if head == None: #base case
            return head
        newNext = self.removeElements(head.next,val)
        if head.val == val:
            return newNext
        else:
            head.next = newNext
            return head

        