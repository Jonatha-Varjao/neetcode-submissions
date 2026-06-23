# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0

        dummy = ListNode()
        tail = dummy

        while l1 or l2 or carry:
            l1_val, l2_val = 0,0
        
            if l1:
                l1_val = l1.val
                l1 = l1.next

            if l2:
                l2_val = l2.val
                l2 = l2.next

            total = l1_val + l2_val + carry
            
            digit = total%10
            carry = total//10

            tail.next = ListNode(val=digit)
            tail = tail.next
            
            

        return dummy.next