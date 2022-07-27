def test(row):
    result=[]

    for i in range (row):
        val = [None for j in range (i+1)]
            
        val[0], val[-1] = 1,1


        for j in range(1,len(val)-1):
            val[j] = result[i-1][j-1]+result[i-1][j]
        result.append(val)
    print(result)




test(3)


