# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return None
        
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        l = 0
        r = len(arr) - 1
        q = collections.deque()

        while l <= r:
            if l == r:
                q.append(arr[l])
            else:
                q.append(arr[l])
                q.append(arr[r])
            l += 1
            r -= 1
        
        while head:
            val = q.popleft()
            head.val = val
            head = head.next

        # slow = fast = head
        # while fast and fast.next:
        #     fast = fast.next.next
        #     slow = slow.next

        # curr = slow.next
        # prev = None
        # slow.next = None

        # while curr:
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp
        
        # tail = prev

        # while tail:
        #     headNext = head.next
        #     tailNext = tail.next
        #     head.next = tail
        #     tail.next = headNext
        #     head = headNext
        #     tail = tailNext
        
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