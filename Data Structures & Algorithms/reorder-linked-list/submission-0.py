# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        

       
        slow_pointer = fast_pointer = head
        while(fast_pointer and fast_pointer.next ):
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        # l2
        l2 = slow_pointer.next
        # l1
        slow_pointer.next = None

       
        prev = None
        current = l2
        while current:
            temp = current.next
            
            current.next = prev
            prev = current
            current = temp
        
        l2 = prev
            
        # now merge
        current_l1 = head 
        current_l2 = l2
        while current_l2:
            templ1 = current_l1.next
            templ2 = current_l2.next


            current_l1.next = current_l2
            current_l2.next = templ1

            current_l1 = templ1
            current_l2 = templ2







