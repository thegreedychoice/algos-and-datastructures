'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
class EdgeNode:
    """
    DataStructure to represent an edge of graph
    """

    def __init__(self, y, weight):
        self.y = y
        self.weight = weight
        self.next = None


class Graph:
    """
    DataStructure to represent the complete graph with an adjacency list
    """

    def __init__(self, maxV, directed, weighted):
        self.maxV = maxV
        self.edges = None
        self.degree = None
        self.nvertices = 0
        self.nedges = 0
        self.directed = directed
        self.weighted = weighted

    def read_graph1(self):
        # read the num of vertices
        self.nvertices = int(input())
        self.degree = [0 for x in range(0, self.nvertices + 1)]
        # read the num of edges
        self.nedges = int(input())
        self.edges = [None for x in range(0, self.nvertices + 1)]

        # read the vertices for each edge
        for i in range(1, self.nedges + 1):
            print("Enter x-y for Edge{0}".format(i))
            x = int(input())
            y = int(input())
            if self.weighted:
                weight = int(input("Enter the weight for {0}-{1}: ".format(x, y)))
            else:
                weight = 0

            # insert each edge in the graph
            self.insert_edge(x, y, weight, self.directed, self.weighted)

    def read_graph(self):
        # read the num of vertices
        n, m = input().split()
        self.nvertices = int(n)
        self.degree = [0 for x in range(0, self.nvertices + 1)]
        # read the num of edges
        self.nedges = int(m)
        self.edges = [None for x in range(0, self.nvertices + 1)]

        # read the vertices for each edge
        for i in range(1, self.nedges + 1):
            #print("Enter x-y for Edge{0}".format(i))
            a, b = input().split()
            x = int(a)
            y = int(b)
            if self.weighted:
                weight = int(input("Enter the weight for {0}-{1}: ".format(x, y)))
            else:
                weight = 0

            # insert each edge in the graph
            self.insert_edge(x, y, weight, self.directed, self.weighted)

    def insert_edge(self, x, y, weight, directed, weighted):
        # create a temp edge node
        e = EdgeNode(y, weight)
        e.next = self.edges[x]

        # add the temp node to the front of the list
        self.edges[x] = e
        self.degree[x] = self.degree[x] + 1

        if not directed:
            self.insert_edge(y, x, weight, True, weighted)
        else:
            pass

    def isEdgePresent(self, x, y):
        edges = self.edges[x]

        while edges is not None:
            if edges.y == y:
                return "YES"

            edges = edges.next

        return "NO"



    def print_graph(self):
        # print num of edges
        print("Num of Edges: {0}".format(self.nedges))
        # print num of vertices
        print("Num of Edges: {0}".format(self.nvertices))
        # print the adjacency lists
        for i in range(1, self.nvertices + 1):
            try:
                ad_list = self.edges[i]
                if ad_list != self.nvertices:
                    print("Vertex {0} :".format(i), end=" ")

                    while ad_list != None:
                        print("{0} ->".format(ad_list.y), end=" ")
                        ad_list = ad_list.next
                    print(" None")
            except:
                print("Vertex {0} : None".format(i))
        print()


#input

g = Graph(100, False, False)
g.read_graph()
q = int(input())

for i in range(0, q):
    a, b = input().split()
    x = int(a)
    y = int(b)
    print(g.isEdgePresent(x, y))




