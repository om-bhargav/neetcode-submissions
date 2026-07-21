from collections import deque
class Solution:
    def plusOne(self, nums: List[int]) -> List[int]:
        carry = 1
        n = len(nums)
        digits = deque(nums)
        for i in range(n-1 , -1 , -1):
            x = digits[i] + carry
            digits[i] = x%10
            x //= 10
            carry = x

        while(carry):
            digits.appendleft(carry%10)
            carry //= 10
        return list(digits)
