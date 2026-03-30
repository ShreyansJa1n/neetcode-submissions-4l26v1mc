# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        p1, p2 = dummy, dummy
        prev = dummy
        counter = 0
        while p2:
            counter += 1
            p2 = p2.next
            if counter > n:
                prev = p1
                p1 = p1.next

        prev.next = p1.next
        
        return dummy.next