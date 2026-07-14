# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        curr = slow.next
        prev = None
        slow.next = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        tail = prev

        while tail:
            headNext = head.next
            tailNext = tail.next
            head.next = tail
            tail.next = headNext
            head = headNext
            tail = tailNext
        
        # if not head.next:
        #     return None
        
        # prev = head
        # curr = head.next
        # last = None

        # while curr and curr.next:
        #     last = curr
        #     secLast = curr
        #     while last and last.next:
        #         secLast = last
        #         last = last.next
            
        #     secLast.next = None

        #     temp = prev.next
        #     prev.next = last
        #     last.next = temp

        #     prev = last.next
        #     curr = curr.next
        
        # return None