class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last = nums[0]
        idx = 1
        n = len(nums)
        for i in range(1,n):
            if(nums[i] != last):
                nums[idx] = nums[i]
                idx += 1
            last = nums[i]
        return idx 