    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        
        n = len(nums)
        new_list = []
        for i in range(1, n + 1):
            new_list.append(i)
        for j in nums:            
            if j in new_list:
                new_list.remove(j)
        return new_list
                