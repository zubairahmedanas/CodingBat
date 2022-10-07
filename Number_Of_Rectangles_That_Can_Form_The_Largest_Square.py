class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:

        res = {}

        for val in rectangles:
            values = min(val)
            if values in res:
                res[values] += 1
            else:
                res[values] = 1

        return res[(max(res.keys()))]





