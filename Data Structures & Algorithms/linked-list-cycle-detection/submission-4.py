# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        curr = prev = head
    
        while curr and curr.next:
            curr = curr.next.next
            prev = prev.next
            if curr == prev:
                return True
        
        return False