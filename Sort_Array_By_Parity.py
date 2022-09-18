    def sortArrayByParity(nums):
        count= 0
        
     
        for j in range(len(nums)):
            if nums[j] % 2 == 0:
                nums[count],nums[j]=nums[j],nums[count]
                count+=1
        return nums