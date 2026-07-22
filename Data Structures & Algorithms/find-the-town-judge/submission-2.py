class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inDegree = [0] * n
        outDegree = [0] * n
        for x,y in trust:
            inDegree[y - 1] += 1
            outDegree[x - 1] += 1
        for i in range(n):
            if(outDegree[i] == 0 and inDegree[i] == (n - 1)):
                return i + 1
        return -1