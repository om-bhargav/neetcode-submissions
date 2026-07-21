# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode(-1)
        curr = prev
        next = None
        while(head):
            next = head.next
            head.next = curr.next
            curr.next = head
            head = next
        prev = prev.next
        return prev