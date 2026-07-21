class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        n = len(cost)
        prices = [float('inf')] * n
        prices[0] = 0
        prices[1] = 0
        for i in range(n):
            if(i + 1 < n):
                prices[i + 1] = min(prices[i + 1],cost[i] + prices[i])
            if(i + 2 < n):
                prices[i + 2] = min(prices[i + 2],cost[i] + prices[i])
        return prices[-1]