def findMin(arr: List[str]) -> str:
    curr = arr[0]
    n = len(arr)
    for i in range(1,n):
        if(len(arr[i])<len(curr)):
            curr = arr[i]
    return curr

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        n = len(strs)
        min_string = findMin(strs)
        for i in range(len(min_string)):
            ch = strs[0][i]
            isSame = True
            for j in range(n):
                if(ch!=strs[j][i]):
                    isSame = False
                    break
            if(isSame):
                ans += ch
            else:
                break
                
        return ans