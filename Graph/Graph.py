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

    def read_graph(self):
        # read the num of vertices
        self.nvertices = int(input("Num of Vertices: "))
        self.degree = [0 for x in range(0, self.nvertices + 1)]
        # read the num of edges
        self.nedges = int(input("Num of Edges: "))
        self.edges = [None for x in range(0, self.nvertices + 1)]

        # read the vertices for each edge
        for i in range(1, self.nedges + 1):
            print(f"Enter x-y for Edge{i}")
            x = int(input("Enter x: "))
            y = int(input("Enter y: "))
            if self.weighted:
                weight = int(input(f"Enter the weight for {x}-{y}: "))
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

    def print_graph(self):
        # print num of edges
        print(f"Num of Edges: {self.nedges}")
        # print num of vertices
        print(f"Num of Edges: {self.nvertices}")
        # print the adjacency lists
        for i in range(1, self.nvertices + 1):
            try:
                ad_list = self.edges[i]
                if ad_list != self.nvertices:
                    print(f"Vertex {i} :", end=" ")

                    while ad_list != None:
                        print(f"{ad_list.y} ->", end=" ")
                        ad_list = ad_list.next
                    print(" None")
            except:
                print(f"Vertex {i} : None")
        print()


if __name__ == "__main__":
    #g = Graph(100, False, False)
    #g.read_graph()
    #g.print_graph()
    pass
