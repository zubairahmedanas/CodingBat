def test(num):
    count = 0
    while num > 0:
        if num % 2 == 0:
            num = num / 2
            # print(num)
        else:
            num = num-1
        count = count + 1
        # print(count)
    return count

print(test(8))
