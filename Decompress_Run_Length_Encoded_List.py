    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        freq = 0
        for i in range (0, len(nums)):
            if i%2 == 1:
                freq = nums[i-1]
                
                for j in range(0, freq):
                    res.append(nums[i])
        return res