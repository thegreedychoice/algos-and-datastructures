def isValidSubsequence(array, sequence):
    if len(array) < len(sequence):
        return False
	
	subIdx = 0
    for idx in range(len(array)):
        if sequence[subIdx] == array[idx]:
            subIdx += 1
        if subIdx == len(sequence):
            return True
	return False