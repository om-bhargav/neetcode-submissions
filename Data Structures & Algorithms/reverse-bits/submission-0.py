class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(31,-1,-1):
            leave = 31 - i
            ans <<= 1
            ans |= (n>>leave) & 1
        return ans