from Heap.MinPriorityQueue import MinPriorityQueue, Node

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

    def read_graph(self, n, m):
        self.nvertices = int(n)
        self.degree = [0 for x in range(0, self.nvertices + 1)]
        # read the num of edges
        self.nedges = int(m)
        self.edges = [None for x in range(0, self.nvertices + 1)]

        # read the vertices for each edge
        for i in range(1, self.nedges + 1):
            #print("Enter x-y for Edge{0}".format(i))
            a, b, w = input("Enter Edge-{0} -> u v weight".format(i)).split()
            x = int(a)
            y = int(b)
            weight = int(w)

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
                        if self.weighted:
                            print("{0}({1}) -> ".format(ad_list.y, ad_list.weight), end=" ")
                        else:
                            print("{0} ->".format(ad_list.y), end=" ")
                        ad_list = ad_list.next
                    print(" None")
            except:
                print("Vertex {0} : None".format(i))
        print()


def prims(N, g, startVertex):
    minCost  = 0
    marked = [None for val in range(0, N+1)]
    start = Node(startVertex, 0)

    pq = MinPriorityQueue(N)
    pq.insert(start)

    while not pq.isEmpty():
        u = pq.extractMin()
        u_vertex = u.key
        u_weight = u.value

        if marked[u_vertex]:
            continue

        minCost += u_weight
        marked[u_vertex] = True

        edges_u = g.edges[u_vertex]

        while edges_u is not None:
            v_vertex = edges_u.y
            v_weight = edges_u.weight

            if marked[v_vertex] is None:
                pq.insert(Node(v_vertex, v_weight))

            edges_u = edges_u.next


    return minCost


if __name__ == "__main__":
    g = Graph(100, False, True)
    n, m = [int(value) for value in input("Enter N M").split()]
    g.read_graph(n, m)
    g.print_graph()

    print(prims(n,g,1))

    """

    k = int(input("Enter k: "))
    pq = MinPriorityQueue(n)

    for i in range(0, n):
        item = int(input("Enter value for item {0}: ".format(i + 1)))
        pq.insert(item)

    pq.printHeap()
    print()

    while k > 0:
        max = pq.extractMin()
        pq.printHeap()
        print(max)
        print()
        k -= 1
    """