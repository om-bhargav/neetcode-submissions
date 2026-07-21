class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        windows = set()
        L = 0
        n = len(nums)
        for R in range(n):
            if R - L > k:
                windows.remove(nums[L])
                L += 1
            if(nums[R] in windows):
                return True
            windows.add(nums[R])
        return False 