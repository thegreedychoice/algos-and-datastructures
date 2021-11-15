# O(n) time | O(n) space where n is number of nodes in B tree
class BinaryTree:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    if root is None:
        return 0

    result = []
    dfs(root, 0, result)
    return result


def dfs(node, branchSum, result):
    if not (node.left or node.right):
        result.append(branchSum + node.value)

    if node.left:
        dfs(node.left, branchSum + node.value, result)

    if node.right:
        dfs(node.right, branchSum + node.value, result)



"""
DFS iterative:

def nodeDepths(root):
    sumOfDepths = 0
	stack = [Node(root, 0)]
	
	while len(stack):
		item = stack.pop()
		node, depth = item.info, item.depth
		
		if node is None:
			continue
		
		sumOfDepths += depth
		
		stack.append(Node(node.left, depth + 1))
		stack.append(Node(node.right, depth + 1))
	
	return sumOfDepths

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
		
class Node:
	def __init__(self, info, depth):
		self.info = info
		self.depth = depth
"""