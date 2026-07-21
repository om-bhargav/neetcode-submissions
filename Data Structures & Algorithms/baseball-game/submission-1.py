class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        for i in operations:
            if(i == "+"):
                x = ans[-2]
                y = ans[-1]
                ans.append(x + y)
            elif(i == "C"):
                ans.pop()
            elif(i == "D"):
                ans.append(ans[-1] * 2)
            else:
                ans.append(int(i))

        return sum(ans)