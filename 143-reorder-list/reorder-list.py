# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # split 

        slow = head
        fast = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next
    
        right_head = slow.next
        slow.next = None
        left_head = head

        prev = None
        current = right_head
        
        while current:
            
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node 

        p1 = left_head
        p2 = prev
        i = 0
        while p1 and p1.next and p2:
            p1_next = p1.next 
            p2_next = p2.next
            p1.next = p2

            if p1_next:
                p2.next = p1_next
            p1 = p1_next
            p2 = p2_next
        
        
        return head