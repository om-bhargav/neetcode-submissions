class Solution:
    def isPalindrome(self,s: str) -> bool:
        return s==s[::-1]
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        if(self.isPalindrome(s)):
            return True
        for i in range(n):
            left = s[:i]
            right = s[i + 1:]
            combined = left + right
            if(self.isPalindrome(combined)):
                return True
        return False