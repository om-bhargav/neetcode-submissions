class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        num = 2 ** n
        for i in range(1,num):
            temp = n - 1
            bit = i
            sm = 0
            while(temp > -1):
                if(bit%2):
                    sm ^= nums[temp]
                bit //= 2
                temp -= 1
            ans += sm
        return ans