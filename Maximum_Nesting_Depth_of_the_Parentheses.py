class Solution:
    def maxDepth(self, s: str) -> int:

        count = 0
        max = 0

        for i in s:
            if i == '(':
                count += 1
                if max < count:
                    max = count
            if i == ')':
                count -= 1
        return max
