# O(depth = log(N)) time | O(1) space
class AncestralTree:

    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne,
                              descendantTwo):
    if not descendantOne or not descendantTwo:
        return topAncestor

        depthOne = getDescendentDepth(descendantOne)
        depthTwo = getDescendentDepth(descendantTwo)

        difference = abs(depthOne - depthTwo)
        if depthOne > depthTwo:
            longer = descendantOne
            shorter = descendantTwo
        else:
            longer = descendantTwo
            shorter = descendantOne

        while difference > 0:
            longer = longer.ancestor
            difference -= 1

        while longer != topAncestor or shorter != topAncestor:
            if longer == shorter:
                return longer
            longer = longer.ancestor
            shorter = shorter.ancestor

        return topAncestor


def getDescendentDepth(node):
    depth = 0

    while node.ancestor:
        node = node.ancestor
        depth += 1
    return depth
