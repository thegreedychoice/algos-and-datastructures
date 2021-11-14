class Node:

    def __init__(self, name):
        self.children = []
        self.name = name
        self.visited = set()

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        stack = []
        stack.append(self)

        while len(stack) > 0:
            item = stack.pop()

            if item not in self.visited:
                self.visited.add(item)
                array.append(item.name)

            for idx in reversed(range(len(item.children))):
                stack.append(item.children[idx])

        return array

"""
Recursive

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name
        self.visited = set()

    def addChild(self, name):
        self.children.append(Node(name))
        return self
        
    def depthFirstSearch(self, array):
        stack = []
        stack.append(self)
        
        while len(stack) > 0:
			item = stack.pop()
			
			if item not in self.visited:
				self.visited.add(item)
				array.append(item.name)
			
			for idx in reversed(range(len(item.children))):
				stack.append(item.children[idx])
    return array
"""
