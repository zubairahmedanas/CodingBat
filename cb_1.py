def front_back(str):
    if len(str) <= 1:
        return str

    first = str[0]
    last = str[-1]
    middle = str[1:-1]
    total = last + middle + first

    # last + mid + first
    return total


