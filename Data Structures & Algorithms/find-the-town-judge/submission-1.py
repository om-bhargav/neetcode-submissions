class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj = {}
        inDegree = [0] * n
        outDegree = [0] * n
        for x,y in trust:
            adj[x] = adj.get(x,[])
            adj[x].append(y)
            inDegree[y - 1] += 1
            outDegree[x - 1] += 1
        for i in range(n):
            if(outDegree[i] == 0 and inDegree[i] == (n - 1)):
                return i + 1
        return -1