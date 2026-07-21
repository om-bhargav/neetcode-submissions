class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        n = len(digits)
        digits.reverse()
        for i in range(n):
            x = digits[i] + carry
            digits[i] = x%10
            x //= 10
            carry = x
        
        while(carry):
            digits.append(carry%10)
            carry //= 10
        digits.reverse()
        return digits
