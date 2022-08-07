class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 1
        for right in range(1, len(nums)):
            if len(nums) == 0:
                return 0
            elif nums[right] != nums[right-1]:
                    nums[left]=nums[right]
                    left += 1
                # print("left val", nums[left])
            # else:
            #     # nums[right] == nums[right-1]
            right = right+1
        return left
           