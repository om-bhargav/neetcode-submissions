class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = len(word1)
        n = len(word2)
        mn = min(m,n)
        final = ""
        for i in range(mn):
            final += (word1[i]+word2[i])
        if(m>mn):
            final = final + word1[mn:]
        else:
            final = final +word2[mn:]
        return final