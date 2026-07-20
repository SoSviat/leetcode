# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        def find_middle(head):
            slow = head 
            fast = head

            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            return slow
        
        def reverse(head):
            prev = None
            current = head

            while current:
                tmp = current.next
                current.next = prev
                prev = current
                current = tmp 
            return prev
        
        mid = find_middle(head)
        second_linked_list = reverse(mid)

        first = head

        while second_linked_list:
            if first.val == second_linked_list.val:
                first = first.next
                second_linked_list = second_linked_list.next
            else:
                return False
        
        return True
