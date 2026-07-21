class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        n = len(digits)
        for i in range(n-1 , -1 , -1):
            x = digits[i] + carry
            digits[i] = x%10
            x //= 10
            carry = x

        while(carry):
            digits.insert(0,carry%10)
            carry //= 10
        return digits
