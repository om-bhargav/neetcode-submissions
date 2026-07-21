from bisect import bisect_left
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        def search(l,r):
            if(l>r):
                return -1
            mid = (l + r) // 2
            if(nums[mid] == target):
                return mid
            elif(nums[mid] > target):
                return search(l, r-1)
            else:
                return search(mid + 1,r)
        return search(0,n-1)