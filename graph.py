"""
Created a vertex class that takes in a label as the parameter. The vertex is the address, and the label is the string
version of the address.

The vertexes will then be added to the graph object. You'll be able to map the distance between each vertex by using
the distances provided in the 'WGUPS Distance Table.csv' and map them with the add_directed_edge function.

"""


class Vertex:
    def __init__(self, label):
        """
        O(1)

        This is the constructor for the Vertex object. The vertex is the address.

        The vertex also has a distance which is currently set to infinity.

        :param label: The label is the string address.
        """
        self.label = label
        self.distance = float('inf')
        self.last_vertex = None

    def __str__(self):
        """
        O(1)

        This formats the print statement for the vertex label.

        :return: The label of the vertex.
        """
        return "%s" % self.label


"""
Create the graph class and add functionality to add vertices and map edges to a graph object.
"""
class Graph:
    def __init__(self):
        """
        O(1)

        Constructor for the graph object that assigns two dictionaries - an adjacency list (the list of adjacent
        addresses) and edge weights (distances between adjacent addresses).
        """
        self.adjacency_list = {}
        self.edge_weights = {}

    def add_vertex(self, new_vertex):
        """
        O(1)

        This function adds a new vertex. The new vertex is the key for the adjacency list dictionary, and adds an empty
        list. This list will get filled with adjacent addresses eventually.

        :param new_vertex: The new vertex being added.
        :return: Does not return anything.
        """
        self.adjacency_list[new_vertex] = []

    def add_directed_edge(self, from_vertex, to_vertex, weight=1.0):
        """
        O(1)

        This function takes in two vertices (will later be used as keys for dictionary) and the distance between each vertex.

        This also adds the second vertex to the first's adjacency list.

        :param from_vertex: The starting vertex.
        :param to_vertex: The destination vertex.
        :param weight: The distance between the starting and destination vertex.
        :return: Does not return anything.
        """
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)

    def add_undirected_edge(self, vertex_a, vertex_b, weight=1.0):
        """
        O(1)

        This function runs the add_directed_edge function on the first and second vertex. This will create an undirected
        edge between both vertices.

        :param vertex_a: The first vertex.
        :param vertex_b: The second vertex.
        :param weight: Distance between the two vertices.
        :return: Does not return anything.
        """
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)
