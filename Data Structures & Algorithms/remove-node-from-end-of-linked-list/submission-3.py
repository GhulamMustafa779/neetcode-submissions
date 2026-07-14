# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        curr = head
        while i < n:
            curr = curr.next
            i += 1
        
        if not curr:
            return head.next
        
        prev = head
        while curr and curr.next:
            curr = curr.next
            prev = prev.next
        
        prev.next = prev.next.next
        return head
