class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count = Counter(nums)
        res  = 0
        for i in count:
            if count[i] == 1:
                res = res + i
        return res