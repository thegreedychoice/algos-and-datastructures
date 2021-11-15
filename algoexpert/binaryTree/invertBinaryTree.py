# O(n) time | O(n) space
def invertBinaryTree(tree):
    bfsInterative(tree)
    return tree


def dfsRecursive(node):
    if node is None:
        return

    dfsRecursive(node.left)
    dfsRecursive(node.right)

    (node.left, node.right) = (node.right, node.left)


def bfsInterative(node):
    queue = [node]

    while len(queue):
        parent = queue.pop(0)
        (parent.left, parent.right) = (parent.right, parent.left)

        if parent.left:
            queue.append(parent.left)

        if parent.right:
            queue.append(parent.right)
    return node


# This is the class of the input binary tree.

class BinaryTree:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
