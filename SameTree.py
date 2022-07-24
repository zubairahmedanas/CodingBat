def isSameTree(self, p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False

    pstack = []
    qstack = []

    pstack.append(p)
    qstack.append(q)

    while pstack or qstack:

        nodep = pstack.pop()
        nodeq = qstack.pop()

        if not nodep and not nodeq:
            continue

        if (not nodep or not nodeq) or nodep.val != nodeq.val:
            return False

        if nodep:
            pstack.append(nodep.left)
            pstack.append(nodep.right)

        if nodeq:
            qstack.append(nodeq.left)
            qstack.append(nodeq.right)

    if len(pstack) == 0 and len(qstack) == 0:
        return True

    return False

