def longestCommonPrefix(strs):
    # strs.sort()
    # minimum = min(len(strs[0]), len(strs[len(strs) - 1]))
    # print("the minimum ,", minimum)
    strs.sort(key=len)
    minimum = strs
    print(minimum)

    result = ""
    if (len(strs) == 0):
        return result
    for i in range(0, len(minimum[0])):
        # print("the values of i :", minimum[0][i])
        for j in minimum:
            if j[i] != minimum[0][i]:
                return result
        result = result + minimum[0][i]
        print(result)


print(longestCommonPrefix(["flower", "flow", "flight"]))
