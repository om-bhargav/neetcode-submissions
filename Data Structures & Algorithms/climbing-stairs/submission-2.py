class Solution:
    def climbStairs(self, n: int) -> int:
        n += 1
        arr = [1] * n
        for i in range(2,n):
            arr[i] = arr[i-1] + arr[i-2]
            
        return arr[-1]