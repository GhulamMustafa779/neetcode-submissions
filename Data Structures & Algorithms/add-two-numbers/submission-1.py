# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = dummy = ListNode()
        carry = 0
        while l1 and l2:
            sum = l1.val + l2.val + carry
            digit = sum % 10
            carry = sum // 10
            head.next = ListNode(digit)
            head = head.next
            l1 = l1.next
            l2 = l2.next
        
        rem = l1 or l2
        while rem:
            sum = rem.val + carry
            digit = sum % 10
            carry = sum // 10
            head.next = ListNode(digit)
            head = head.next
            rem = rem.next
        
        if carry:
            head.next = ListNode(carry)
        
        return dummy.next
