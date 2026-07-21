import heapq as h
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        stones = [-i for i in stones]
        h.heapify(stones)
        while(len(stones)>1):
            x = -h.heappop(stones)
            y = -h.heappop(stones)
            if(x!=y):
                h.heappush(stones,-(x - y))
        
        return 0 if len(stones)==0 else -stones[0]    