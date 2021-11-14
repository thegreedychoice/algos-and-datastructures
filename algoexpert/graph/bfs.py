# O(v+e) time | o(v) space
class Node:

    def __init__(self, name):
        self.children = []
        self.name = name
        self.visited = set()

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        queue = [self]

        while len(queue):
            item = queue.pop(0)

            if item not in self.visited:
                self.visited.add(item)
                array.append(item.name)

            for childItem in item.children:
                if childItem not in self.visited:
                    queue.append(childItem)

        return array

"""
Recursive

"""
