def plus_one(digits):
    for i in reversed(range(len(digits))):
        digits[i]+=  1
        print(digits)
        if digits[i] < 10:
            return digits
        else:
            digits[i]=0
            # return digits


    digits.insert(0,1)
    return digits


# print(plus_one([2, 3, 9]))
print(plus_one([9,9]))