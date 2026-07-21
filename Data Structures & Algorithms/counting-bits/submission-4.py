class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        curr = 1
        if(n>0):
            ans[1] = 1
        while(curr <= n):
            if((curr * 2) <=n ):
                ans[(curr * 2)] += ans[curr]
            if((curr * 2)+1 <=n):
                ans[(curr * 2)+1] += ans[curr] + 1
            curr += 1
        return ans