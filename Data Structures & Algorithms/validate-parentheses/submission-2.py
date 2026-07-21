class Solution:
    def isValid(self, s: str) -> bool:
        st = {
            '(': -1,
            '{': -2,
            '[': -3,
        }
        en = {
            ')': 1,
            '}': 2,
            ']': 3,
        }
        stack = []
        for i in s:
            if(stack and stack[-1] in st and i in en and st[stack[-1]] + en[i] ==0):
                stack.pop()
            else:
                stack.append(i)
        return len(stack)==0