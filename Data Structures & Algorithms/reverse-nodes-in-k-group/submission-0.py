# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def get_length(node: Optional[ListNode]):
            curr = 0
            while(node):
                curr += 1
                node = node.next
            return curr
        def reverse(node):
            rev = None
            temp = node
            left = k
            while(temp and left):
                next = temp.next
                temp.next = rev
                rev = temp 
                temp = next
                left -= 1
            return [rev,temp]
        length = get_length(head)
        ans = ListNode(-1)
        curr = ans
        while(head):
            if(length < k):
                curr.next = head
                break
            else:
                nxth,nxtl = reverse(head)
                curr.next = nxth
                curr = head
                head = nxtl
                length -= k
        return ans.next