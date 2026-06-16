# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # need to find the middle?
        # slip into two lists
        # reverse te second one
        # compare while l1[i] != l2[i]

        slow_p = head   
        fast_p = head

        # O( N )
        while fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next


        # slow_p will stop at the middle
        # reverse it
        prev = None
        current = slow_p
        # O(N)
        while current:
            # store next
            temp = current.next
            
            # change pointer to previous
            current.next = prev
            # update the next previous
            prev = current
            # move pointer
            current = temp

        list_2 = prev

        while list_2:
            if list_2.val != head.val:
                return False
            
            head = head.next
            list_2 = list_2.next


        return True
