from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp = Counter(nums)
        lst = [True if i==1 else False for i in mp.values()]
        return not all(lst)