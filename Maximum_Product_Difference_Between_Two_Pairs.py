class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums = sorted(nums)
        nums_len = len(nums) - 2
        print(nums_len)

        x = nums[:2]
        y = nums[nums_len:]
        prod1 = x[0] * x[1]
        prod2 = y[0] * y[1]

        res = prod2 - prod1
        return res
