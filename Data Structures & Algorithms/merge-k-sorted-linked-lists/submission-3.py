# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(list1,list2):
            if(not list1):
                return list2
            if(not list2):
                return list1
            ans = ListNode(-1)
            curr = ans
            while(list1 and list2):
                x,y = list1.val,list2.val
                if(x < y):
                    curr.next = list1
                    list1 = list1.next
                elif(x >= y):
                    curr.next = list2
                    list2 = list2.next
                curr = curr.next
                curr.next = None
            if(list1):
                curr.next = list1
            else:
                curr.next = list2
            return ans.next
        ans = None
        for lst in lists:
            ans = merge(lst,ans)
        return ans