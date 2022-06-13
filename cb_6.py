sentence = str(input("Enter a string : "))

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()! "
ascii = []
count = 0
for x in sentence:
    char_count = sentence.count(x)
    if char_count > count:
        char_freq = []
        count = char_count
        char_freq.append(x)
    elif char_count == count and x not in char_freq:
        char_freq.append(x)
    ascii = []
    for i in char_freq:
        ascii.append((ord(i)))
        res = min(ascii)

print('count:', count, char_freq, ascii,res)

# print("ur result is :", result)


# string= "aaaAAA"
#
#
# char_freq={}
#
# for i in string:
#     if i in char_freq:
#         char_freq[i]=char_freq[i]+1
#     else:
#         char_freq[i] = 1
# result= max(char_freq, key = char_freq.get)
# res = result.count
# print(char_freq,"Most frequent character: ",result,res)
