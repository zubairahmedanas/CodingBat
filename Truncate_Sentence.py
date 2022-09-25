class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s.split()
        res = s[:k]
        output = ' '.join(res)
        return output