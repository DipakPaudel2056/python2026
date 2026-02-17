# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # let's create new list with reverse 
        if not head or not head.next:
            return True

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev,curr = None,slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        first,second = head,prev
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next

        return True
            
        
        
#leetcode 234
# the approach is simple,
# reach to the middle of the linked list,
# reverse the half of the linked list and compare the first and the second half of the linked list