def findNumbers(nums):
    strings = []
    count = 0
    for i in nums:
        strings.append(str(i))

    for j in strings:
        # print("value of j",len(j))
        if len(j) % 2 == 0:
            count += 1
    return count