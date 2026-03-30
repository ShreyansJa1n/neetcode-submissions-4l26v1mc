# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = ListNode()
        head1 = list1
        head2 = list2
        head = cur

        while head1 and head2:
            if head1.val > head2.val:
                cur.next = head2
                head2 = head2.next
            else:
                cur.next = head1
                head1 = head1.next

            cur = cur.next

        while cur and head1:
            cur.next = head1
            head1 = head1.next
            cur = cur.next

        while cur and head2:
            cur.next = head2
            head2 = head2.next
            cur = cur.next

        return head.next