def front3(str):
    if len(str)<1:
        return str


    capture = str[0:3]
    total = capture+capture+capture
    print(capture)
    print(total)
print(front3('ab'))



