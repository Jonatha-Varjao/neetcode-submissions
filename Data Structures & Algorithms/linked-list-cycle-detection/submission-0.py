# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        

        slow_pointer = head
        fast_pointer = head.next
        while fast_pointer and fast_pointer.next:
            if fast_pointer == slow_pointer:
                return True

            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        
        return False