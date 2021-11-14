# O(wh) time | O(n) space where n is number of results
def riverSizes(matrix):
    if not (len(matrix) or len(matrix[0])):
        return []

    visited = [[False for col in row] for row in matrix]
    result = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 1:
                size = dfsAtVertex(matrix, row, col, result)
                if size > 0:
                    result.append(size)
    return result


def dfsAtVertex(
    matrix,
    row,
    col,
    result,
    ):
    stack = [(row, col)]
    size = 0

    while len(stack):
        vertex = stack.pop()
        (rowV, colV) = vertex

        if matrix[rowV][colV] != -1:
            matrix[rowV][colV] = -1
            size += 1

        # find all neighbours and add valid ones to stack

        for neighbor in getUnvisitedNeighbors(rowV, colV, matrix):
            (rowN, colN) = neighbor
            if rowN >= 0 and rowN < len(matrix) and colN >= 0 and colN \
                < len(matrix[0]) and matrix[rowN][colN] == 1:
                stack.append((rowN, colN))

    return size


def getUnvisitedNeighbors(rowV, colV, matrix):
    unVisitedNeighbors = []
    if rowV > 0 and matrix[rowV - 1][colV] != -1:
        unVisitedNeighbors.append((rowV - 1, colV))

    if colV < len(matrix[0]) - 1 and matrix[rowV][colV + 1] != -1:
        unVisitedNeighbors.append((rowV, colV + 1))

    if rowV < len(matrix) - 1 and matrix[rowV + 1][colV] != -1:
        unVisitedNeighbors.append((rowV + 1, colV))

    if rowV > 0 and matrix[rowV][colV - 1] != -1:
        unVisitedNeighbors.append((rowV, colV - 1))

    return unVisitedNeighbors


"""
Recursive

currentSize = 0
def riverSizes(matrix):
	if not (len(matrix) or len(matrix[0])):
		return []
	global currentSize
    array = []
	ans = 0
	for row in range(len(matrix)):
		for col in range(len(matrix[0])):
			if matrix[row][col] == 1:
				currentSize = 0
				dfs(matrix, row, col)
				array.append(currentSize)
	return array
			
def dfs(matrix, row, col):
	if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or matrix[row][col] != 1:
		return
		
	matrix[row][col] = -1
	global currentSize
	currentSize += 1
		
	dfs(matrix, row+1, col)
	dfs(matrix, row-1 , col)
	dfs(matrix, row, col+1)
	dfs(matrix, row, col-1)


"""