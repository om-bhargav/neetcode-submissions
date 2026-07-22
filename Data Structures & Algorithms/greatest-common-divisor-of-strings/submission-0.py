class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(s1, s2):
            if(s1 == ""):
                return s2
            if(s2 == ""):
                return s1
            if(len(s2) < len(s1)):
                return gcd(s2,s1)
            if(s2.endswith(s1)):
                m = len(s2)
                n = len(s1)                
                return gcd(s2[:m - n],s1)
            return ""
        return gcd(str1,str2)