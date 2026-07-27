# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import sys
sys.setrecursionlimit(10000)
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(list1,list2):
            if(not list1):
                return list2
            if(not list2):
                return list1
            if(list1.val < list2.val):
                list1.next = merge(list1.next,list2)
                return list1
            list2.next = merge(list1,list2.next)
            return list2
        ans = None
        for lst in lists:
            ans = merge(lst,ans)
        return ans