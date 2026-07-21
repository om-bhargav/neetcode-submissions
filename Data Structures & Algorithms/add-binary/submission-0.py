class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carr = 0
        res = ""
        i = len(a) - 1
        j = len(b) - 1
        while(i > -1 or j > -1 or carr):
            x = 0
            y = 0
            if(i > -1):
                x = int(a[i])
                i -= 1
            if(j > -1):
                y = int(b[j])
                j -= 1

            z = x + y + carr
            res += str(z%2)
            carr = z // 2
        res = res[::-1]
        return res
            