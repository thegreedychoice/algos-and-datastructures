from Graph import *
import queue
class GraphTraversal:
    """
    Class with a bunch of graph traversal methods implemented
    """
    def __init__(self, algo, g):
        if algo == "bfs":
            self.processed = [None for x in range(0, g.nvertices + 1)]     # bool array to track which vertices have been processed
            self.discovered = [None for x in range(0, g.nvertices + 1)]     # bool array to track which vertices have been found
            self.parents = [None for x in range(0, g.nvertices + 1)]       # int array to track parents of each vertex
            self.initialize_bfs(g)
            self.bfs(g, 1)

    def initialize_bfs(self, g):
        for i in range(1, g.nvertices + 1):
            self.processed[i] = self.discovered[i] = False
            self.parents[i] = -1

    def process_vertex_early_bfs(self, v):
        print(f"processed vertex {v}", end="\n")

    def process_vertex_late_bfs(self, v):
        pass

    def process_edge(self, u, v):
        print(f"processed edge {u} - {v}", end="\n")

    def bfs(self, g, start):
        q = queue.Queue()       # queue to push discovered vertices so that they can be processed
        u = 0
        v = 0
        edge = EdgeNode(0, 0)

        print("Starting Breadth first Search!\n")
        # push the root vertex to the queue
        q.put(start)
        # mark the root as discovered
        self.discovered[start] = True

        # Loop until the queue is empty
        while not q.empty():
            # get the vertex from the queue
            u = q.get()

            # process vertex u as desired
            self.process_vertex_early_bfs(u)
            # get the edges connected to u
            edges = g.edges[u]  # edges is a linked list

            # extract the adjacent vertices from the edges
            while edges is not None:
                v = edges.y
                # process edge (u, v) as desired
                # if v has not been processed yet and graph is directed
                if not self.processed[v] or g.directed:
                    self.process_edge(u, v)

                # if v has not been discovered yet
                if not self.discovered[v]:
                    self.discovered[v] = True
                    self.parents[v] = u
                    q.put(v)
                edges = edges.next
            # vertex u processed completely
            self.process_vertex_late_bfs(u)
            self.processed[u] = True


if __name__  == "__main__":
    g = Graph(100, True, False)
    g.read_graph()
    g.print_graph()

    gt = GraphTraversal("bfs", g)