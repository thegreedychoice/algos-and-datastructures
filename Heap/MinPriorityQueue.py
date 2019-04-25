class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class MinPriorityQueue:
    """
    Min priority queue
    """

    def __init__(self, N):
        self.capacity = N
        self.size = 0
        self.items = [Node for i in range(N)]
        self.map = dict()

    def getLeftChildIndex(self, parentIndex):
        return 2 * parentIndex + 1

    def getRightChildIndex(self, parentIndex):
        return 2 * parentIndex + 2

    def getParentIndex(self, childIndex):
        return int((childIndex - 1) / 2)

    def hasLeftChild(self, parentIndex):
        return self.getLeftChildIndex(parentIndex) < self.size

    def hasRightChild(self, parentIndex):
        return self.getRightChildIndex(parentIndex) < self.size

    def hasParent(self, childIndex):
        return self.getParentIndex(childIndex) >= 0 and self.getParentIndex(childIndex) < self.size

    def getLeftChild(self, index):
        return self.items[self.getLeftChildIndex(index)].value

    def getRightChild(self, index):
        return self.items[self.getRightChildIndex(index)].value

    def getParent(self, index):
        return self.items[self.getParentIndex(index)].value

    def isEmpty(self):
        if self.size <= 0:
            return True
        else:
            return False

    def ensureExtraCapacity(self):
        if self.size == self.capacity:
            self.items.extend([Node for i in range(self.capacity)])

    def peek(self):
        if not self.isEmpty():
            return self.items[0]
        else:
            raise Exception('Array items is empty')

    def swap(self, indexA, indexB):
        temp = self.items[indexA]
        self.items[indexA] = self.items[indexB]
        self.items[indexB] = temp

        # update the map with these new index values
        self.map[self.items[indexA].value] = indexA
        self.map[self.items[indexB].value] = indexB


    def extractMin(self):
        min = self.peek().value
        # update the index of removed min value in the map

        if min in self.map:
            self.map[min] = None

        # update the items array
        self.items[0] = self.items[self.size - 1]
        # update the map
        self.map[self.items[0].value] = 0

        # remove min from the items array
        self.items[self.size - 1] = None
        self.size -= 1
        self.heapifyDown()
        return min

    def heapifyDown(self):
        index = 0
        while self.hasLeftChild(index):
            minIndex = self.getLeftChildIndex(index)

            if self.hasRightChild(index) and self.getRightChild(index) < self.getLeftChild(index):
                    minIndex = self.getRightChildIndex(index)

            if self.items[index].value > self.items[minIndex].value:
                self.swap(index, minIndex)
            else:
                break

            index = minIndex

    def insert(self, item):
        self.ensureExtraCapacity()
        # update the items array
        self.items[self.size] = item
        # update the map with initial index
        self.map[item.value] = self.size
        self.size += 1
        current_index = self.size - 1
        self.heapifyUp(current_index)

    def heapifyUp(self, index):

        while self.hasParent(index) and self.getParent(index) > self.items[index].value:
            self.swap(index, self.getParentIndex(index))
            index = self.getParentIndex(index)


    def contains(self, item):
        return self.map.__contains__(item.value)

    def decrease(self, oldValue, newValue):
        # check if the item first exists in the map
        index = self.map.get(oldValue)
        if index is not None:
            # remove the old item from map
            del self.map[oldValue]
            print(f"deleting {oldValue} from map")
            #add the new value to the map
            self.map[newValue] = index
            # update the value in the tree
            self.items[index].value = newValue
            self.heapifyUp(index)



    def printHeap(self):
        print("Printing Heap")
        print("Printing Keys")
        print("[", end= "")
        for i in range(0, self.size):
            print("{0}".format(self.items[i].key), end=",")
        print("]")

        print("Printing Values")
        print("[", end= "")
        for i in range(0, self.size):
            print("{0}".format(self.items[i].value), end=",")
        print("]")
        print()
        print("Printing Map")
        print(self.map)


if __name__ == "__main__":
    N = int(input("Enter no of nodes: "))
    k = int(input("Enter k: "))
    heap = MinPriorityQueue(N)

    for i in range(0, N):
        key = int(input("Enter key for item {0}: ".format(i + 1)))
        value = int(input("Enter value for item {0}: ".format(i + 1)))
        heap.insert(Node(key, value))

    heap.printHeap()
    print()


    heap.decrease(5, -2)
    heap.printHeap()
    print()

    while k > 0:
        max = heap.extractMin()
        heap.printHeap()
        print(max)
        print()
        k -= 1

"""
    heap.decrease(7, -2)
    heap.printHeap()
    print()

    heap.decrease(2, -5)
    heap.printHeap()
    print()



    while k > 0:
        max = heap.extractMin()
        heap.printHeap()
        print(max)
        print()
        k -= 1

"""

