# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None

        cur = slow
        prev = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        rev_head = prev

        while head and rev_head:
            next = head.next
            head.next = rev_head
            rev_head_next = rev_head.next
            rev_head.next = next if next else rev_head_next
            rev_head = rev_head_next
            head = next
