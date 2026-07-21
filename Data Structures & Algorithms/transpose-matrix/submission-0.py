class Solution:
    def transpose(self, arr: List[List[int]]) -> List[List[int]]:
        m = len(arr)
        n = len(arr[0])
        matrix = [[0 for _ in range(m)] for __ in range(n)]
        for i in range(m):
            for j in range(n):
                matrix[j][i] = arr[i][j]
        return matrix