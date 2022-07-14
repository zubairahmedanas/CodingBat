def climbing_stairs(n):
    if n <= 2:
        return n
    p1 =1
    p2 = 2
    cur = 0
    for i in range(2, 5):
        cur = p1 + p2
        p1 = p2
        p2 = cur


    return cur

print(climbing_stairs(2))
