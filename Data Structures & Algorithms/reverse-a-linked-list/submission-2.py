# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        curr = head

        # 0 -> 1 -> 2 -> 3
        while curr != None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        # at termination of while loop the curr is None
        # prev is pointing to new head since its 1 before the edge of the end of the linked list
        return prev




        