def prefix(str):
    # for i in range(0,len(str[0])):
    #     # print("the values are", str[0][i])
    #     for s in str:
    #         print("lets see ",s[i])
    # small_word = min(len(liststr)))
    # print(small_word)
    str.sort()
    print(str)


    # print(y)
    x = min(str, key = len)
    print(len(x))

prefix(["asdasdaflower","flow","flight"])
