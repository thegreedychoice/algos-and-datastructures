# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
	currentNode = linkedList
	while currentNode is not None:
		nextNode = currentNode.next
		
		while nextNode is not None and currentNode.value == nextNode.value:
			nextNode = nextNode.next
		currentNode.next = nextNode
		currentNode = nextNode
		
	return linkedList