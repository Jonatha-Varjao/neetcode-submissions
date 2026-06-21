# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        # find the middle position head
        slow_p, fast_p = head,head
        while fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next
        
        # reversing my second half
        prev = None
        current = slow_p
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        
        # iterate over ll storing max_sum of twins
        reversed_ll = prev
        current = head
        max_sum = 0
        while current and reversed_ll:
            max_sum = max(max_sum, current.val + reversed_ll.val)

            current = current.next
            reversed_ll = reversed_ll.next  

        return max_sum

