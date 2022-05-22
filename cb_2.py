def not_string(str):
    if 'is not' in str:
        word = 'not' + ' ' + str
        return word
    elif 'not' in str:
        # word = 'not' + ' ' + str
        return str
    else:
        word = 'not' + ' ' + str
        return word
