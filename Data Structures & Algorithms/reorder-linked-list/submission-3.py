# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return None
        
        prev = head
        curr = head.next
        last = None

        while curr and curr.next:
            last = curr
            secLast = curr
            while last and last.next:
                secLast = last
                last = last.next
            
            secLast.next = None

            temp = prev.next
            prev.next = last
            last.next = temp

            prev = last.next
            curr = curr.next
        
        return None