# create a vertex with a label
class Vertex:
    def __init__(self, label):
        self.label = label
        self.distance = float('inf')
        self.last_vertex = None

    def __str__(self):
        return "%s" % self.label


# create the graph and add functionality to add vertices and map edges
class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}

    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []

    def add_directed_edge(self, from_vertex, to_vertex, weight=1.0):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)

    def add_undirected_edge(self, vertex_a, vertex_b, weight=1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)

    # def return_edge_weights(self, label1, label2):
    #     prev = None
    #     curr = None
    #     for i in range(len(self.adjacency_list)):
    #         if self.adjacency_list[i].label == label1:
    #             prev = i
    #         if self.adjacency_list[i].label == label2:
    #             curr = i
    #     return self.edge_weights[(prev, curr)]
