import heapq as h
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.lst = [-i for i in nums]
        self.k = k
        h.heapify(self.lst)

    def add(self, val: int) -> int:
        h.heappush(self.lst,-val)
        n = len(self.lst)
        k = self.k
        removed = []
        while(k):
            x = h.heappop(self.lst)
            removed.append(x)
            k -= 1
        ans = removed[-1]
        while(removed):
            h.heappush(self.lst,removed[-1])
            removed.pop()
        return -ans        
