class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        last = 0
        curr = 0
        for i in nums:
            if(curr == 0):
                last = i
                curr = 1
            elif(i==last):
                curr += 1
            else:
                curr -= 1
        return last