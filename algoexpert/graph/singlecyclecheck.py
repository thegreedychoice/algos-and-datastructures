def hasSingleCycle(array):
    size = len(array)
    numOfElemsVisited = 0
    currentIdx = 0

    while numOfElemsVisited < size:
        if currentIdx == 0 and numOfElemsVisited > 0:
            return False

        numOfElemsVisited += 1
        currentIdx = calculateNextIndex(currentIdx, array)


    return currentIdx == 0


def calculateNextIndex(currentIdx, array):
    size = len(array)
    nextIdx = (currentIdx + array[currentIdx]) % size
    return (nextIdx if nextIdx >= 0 else nextIdx + size)

"""
[1, -1, 1, -1] - double cycle

3 conditions to check for:
1. Starting should be only reached once after completing traversal on all n elements in the array
2. After compeleting the traversal, the currentIndex should be 0
3. If 0 < m < n elements traversed and currentIndex == 0, then return False
"""