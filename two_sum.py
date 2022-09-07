   for i in range (len(nums)):
            for j in range (i+1,len(nums)):
                print(nums[j])
                if nums[i] + nums[j] == target:
                    return([i,j])