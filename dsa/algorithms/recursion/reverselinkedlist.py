# here we are using recursion technique to reverse the linked list 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or not head.next: #base case is if we are at the end of the linked list or the head itself is none, then we want to return none
            return head
        newNext = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newNext
        
            
        