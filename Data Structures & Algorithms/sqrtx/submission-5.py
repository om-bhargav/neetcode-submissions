class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        r = x
        last = 0
        while(l<=r):
            mid = l + (r - l) // 2
            sq = mid * mid
            if(sq == x):
                return mid
            elif(sq < x):
                l = mid + 1
                last = mid
            else:
                r = mid - 1
        return last