def twoNumberSum(array, targetSum):
    res = []
    if len(array) <= 1:
        return res

    hashMap = dict()
    for i in range(len(array)):
        item = array[i]
        if targetSum - item not in hashMap:
            hashMap[item] = i
        else:
            res.append(item)
            res.append(targetSum - item)
    return res