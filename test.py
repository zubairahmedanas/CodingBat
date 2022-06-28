n, c = [int(x) for x in input().split()]
par = arr = [int(x) for x in input().split()]
cl = [int(x) for x in input().split()]

parent = [-1] * (n + 1)
for i in range(n - 1):
    parent[i + 2] = par[i]


# print(parent)


def find_cl(node, target):
    if parent[node] == -1:
        return -1

    if cl[parent[node] - 1] == target:
        return parent[node]

    return find_cl(parent[node], target)





