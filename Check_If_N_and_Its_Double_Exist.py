 def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        for i in range (len(arr)):
            for j in range (len(arr)):
                # print("value of j", j)
                if len(arr) == 0:
                    return False
                
                if arr[i] == arr[j]*2 and i != j:
                    return True
        
        return False