class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        n = len(nums)
        for i in range(n): 
            left = target - nums[i]
            if(left in mp):
                ans = [i,mp[left]]
                ans.sort()
                return ans
            mp[nums[i]] = i
        return [-1,-1] 