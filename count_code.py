def count_code(str):
    count = 0
    for i in range(0, len(str) - 3, 1):
        # print(str[i])
        if (str[i] == 'c') and (str[i+1] == 'o') and (str[i+3] == 'e'):
            count = count+1

    print(count)
count_code('aaacodebbb')
