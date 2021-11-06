def sortedSquaredArray(array):
    res = []
    (s, l) = (0, len(array) - 1)
    while s <= l:
        if abs(array[s]) >= abs(array[l]):
            res.insert(0, array[s] ** 2)
            s += 1
        else:
            res.insert(0, array[l] ** 2)
            l -= 1

        return res