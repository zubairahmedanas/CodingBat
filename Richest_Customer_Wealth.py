 def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        
        
        rows = len(accounts)
        cols = len(accounts[0])
        arr=[]
        for i in range(0, rows):
            sum = 0
            
            for j in range (0, cols):
                sum = sum+ accounts[i][j]
            arr.append(sum)
            x = max(arr)
        return(x)