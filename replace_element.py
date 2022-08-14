def replaceElements(arr):
    """
    :type arr: List[int]
    :rtype: List[int]
    """
    n = len(arr)

    new_arr = arr[:]

    for i in range(0, n - 1):
        arr[i] = max((new_arr[i + 1:]))
    arr[-1] = -1

    return arr