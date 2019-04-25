class MaxHeap:
    """
    Binary Heap
    """
    def __init__(self, N):
        self.capacity = N
        self.size = 0
        self.items = [None for i in range(0, N)]

    def getLeftChildIndex(self, parentIndex):
        return 2 * parentIndex + 1

    def getRightChildIndex(self, parentIndex):
        return 2 * parentIndex + 2

    def getParentIndex(self, childIndex):
        return int((childIndex - 1) / 2)

    def hasLeftChild(self, parentIndex):
        return (self.getLeftChildIndex(parentIndex) < self.size)

    def hasRightChild(self, parentIndex):
        return (self.getRightChildIndex(parentIndex) < self.size)

    def hasParent(self, childIndex):
        parentIndex = self.getParentIndex(childIndex)
        return (parentIndex >= 0 and parentIndex < self.size)

    def getLeftChild(self, parentIndex):
        return self.items[self.getLeftChildIndex(parentIndex)]

    def getRightChild(self, parentIndex):
        return self.items[self.getRightChildIndex(parentIndex)]

    def getParent(self, childIndex):
        return self.items[self.getParentIndex(childIndex)]

    def isEmpty(self):
        if self.size <= 0:
            return True
        else:
            return False

    def ensureExtraCapacity(self):
        if self.size == self.capacity:
            # double up the size of the array
            self.items.extend([None for i in range(self.capacity)])

    def peek(self):
        if not self.isEmpty():
            return self.items[0]
        else:
            raise Exception('Array items is empty')

    def swap(self, indexA, indexB):
        temp = self.items[indexA]
        self.items[indexA] = self.items[indexB]
        self.items[indexB] = temp

    def extractMax(self):
        if not self.isEmpty():
            root = self.items[0]
            self.items[0] = self.items[self.size - 1]
            self.items[self.size - 1] = None
            self.size -= 1
            self.heapifyDown()
            return root
        else:
            raise Exception('Array items is empty: {0}'.format(x))

    def insert(self, item):
        self.ensureExtraCapacity()
        self.items[self.size] = item
        self.size += 1
        self.heapifyUp()

    def heapifyUp(self):
        index = self.size - 1
        while self.hasParent(index) and (self.getParent(index) < self.items[index]):
            self.swap(index, self.getParentIndex(index))
            index = self.getParentIndex(index)



    def heapifyDown(self):
        index = 0
        while (self.hasLeftChild(index)):
            # figure out the index of child with max value
            maxIndex = self.getLeftChildIndex(index)

            if (self.hasRightChild(index) and self.getRightChild(index) > self.getLeftChild(index)):
                maxIndex = self.getRightChildIndex(index)

            # swap the index with larger child if child > parent
            if (self.items[maxIndex] > self.items[index]):
                self.swap(index, maxIndex)
            else:
                break

            index = maxIndex


    def printHeap(self):
        print("Printing Heap")
        print(self.items)


if __name__ == "__main__":
    N = int(input("Enter no of nodes: "))
    k = int(input("Enter k: "))
    heap = MaxHeap(N)

    for i in range(0, N):
        item = int(input("Enter value for item {0}: ".format(i + 1)))
        heap.insert(item)

    heap.printHeap()

    while k > 0:
        max = heap.extractMax()
        k -= 1

    print(max)




