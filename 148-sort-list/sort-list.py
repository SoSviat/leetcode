# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head

        def findMiddleList(self, head):
            slow = head 
            fast = head
            prew = head

            while fast and fast.next:
                fast = fast.next.next
                prew = slow
                slow = slow.next

            return prew
        
        def MergeTwoLists(self, left, right):
            dummy = ListNode()
            res = dummy

            while left and right:
                if left.val < right.val:
                    res.next = left
                    left = left.next
                else:
                    res.next  = right
                    right = right.next
                
                res = res.next
            
            if left:
                res.next = left
            if right:
                res.next = right 

            return dummy.next 

                

        # separete to midle
        prew = findMiddleList(self, head)
        
        right_head = prew.next
        prew.next = None
        left_head = head

        left = self.sortList(left_head)
        right = self.sortList(right_head)

        f_res = MergeTwoLists(self,left,right)


        return f_res

        # O(n log n)
        # O (log n)