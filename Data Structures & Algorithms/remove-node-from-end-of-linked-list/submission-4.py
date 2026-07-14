# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = head
        i = 0
        while i < n:
            curr = curr.next
            i += 1
        
        prev = dummy
        while curr:
            curr = curr.next
            prev = prev.next
        
        prev.next = prev.next.next
        return dummy.next
