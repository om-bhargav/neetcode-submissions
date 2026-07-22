class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index = {c: i for i,c in enumerate(order)}
        def compare(word):
            return [order_index[i] for i in word]
        return words == sorted(words,key = compare)