class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)
	
	# O(n) time | O(1) space
    def buildHeap(self, array):
        firstParentIdx = len(array) - 2 // 2
		for idx in reversed(range(firstParentIdx + 1)):
			self.siftDown(idx, array)
		return array
	
	# O(log(n)) time | O(1) space
    def siftDown(self, idx, heap):
		while ((2 * idx + 1) < len(heap)):
			leftChildIdx = 2 * idx + 1
			rightChildIdx = 2 * idx + 2
			smallerChildIdx = leftChildIdx
			if(rightChildIdx < len(heap) and heap[rightChildIdx] < heap[smallerChildIdx]):
				smallerChildIdx = rightChildIdx
			
			if heap[smallerChildIdx] < heap[idx]:
				self.swap(idx, smallerChildIdx, heap)
				idx = smallerChildIdx
			else:
				return
				
        
	# O(log(n)) time | O(1) space
    def siftUp(self, idx, heap):
        parentIdx = (idx - 1) // 2
		while (idx > 0) and (heap[idx] < heap[parentIdx]):
			self.swap(idx, parentIdx, heap)
			idx = parentIdx
			parentIdx = (idx - 1) // 2
	
	# O(1) time | O(1) space
    def swap(self, idx1, idx2, heap):
		tmp = heap[idx1]
		heap[idx1] = heap[idx2]
		heap[idx2] = tmp
	
	# O(1) time | O(1) space
    def peek(self):
        return self.heap[0]
	
	# O(log(n)) time | O(1) space
    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
		valueToBeRemoved = self.heap.pop()
		self.siftDown(0, self.heap)
		return valueToBeRemoved

	# O(log(n)) time | O(1) space
    def insert(self, value):
        self.heap.append(value)
		self.siftUp(len(self.heap) - 1, self.heap)


