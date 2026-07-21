class Solution:
    def isHappy(self, n: int) -> bool:
        vis = set()
        num = n
        while(num):
            sm = 0
            while(num):
                sm += ((num%10) ** 2)
                num //= 10
            if(sm==1):
                return True
            if(sm in vis):
                return False
            vis.add(sm)
            num = sm
        return False