from hashTable import ChainingHashTable
from graph import Graph
from distance import load_distance_data
from truck import Truck, greedy_algorithm_for_package_loading
from readCSV import load_package_data

myHashTable = ChainingHashTable()

map_graph = Graph()

load_distance_data('WGUPS Distance Table.csv')

key_list = list(map_graph.adjacency_list.keys())

load_package_data('WGUPS Package File.csv')

greedy_algorithm_for_package_loading(myHashTable)
#
# for i in range(len(myHashTable.table)):
#     print("Key: {} and Package: {}".format(i+1, myHashTable.search(i+1)))
#
#
# def dijkstras_shortest_path_algorithm(g, starting_vertex):
#     unvisited_queue = []
#     for current_vertex in g.adjacency_list:
#         unvisited_queue.append(current_vertex)
#
#     starting_vertex.distance = 0
#     while len(unvisited_queue) > 0:
#         smallest_index = 0
#         for j in range(1, len(unvisited_queue)):
#             if unvisited_queue[j].distance < unvisited_queue[smallest_index].distance:
#                 smallest_index = j
#         current_vertex = unvisited_queue.pop(smallest_index)
#
#         for adj_vertex in g.adjacency_list[current_vertex]:
#             edge_weight = g.edge_weights[(current_vertex, adj_vertex)]
#             alt_path_distance = current_vertex.distance + edge_weight
#
#             if alt_path_distance < adj_vertex.distance:
#                 adj_vertex.distance = alt_path_distance
#                 adj_vertex.last_vertex = current_vertex
#
#
# def get_short_path(start_vertex, end_vertex):
#     path = ""
#     current_vertex = end_vertex
#     while current_vertex is not start_vertex:
#         path = " -> " + str(current_vertex.label) + path
#         current_vertex = current_vertex.last_vertex
#     path = str(start_vertex.label) + path
#     return path


# def get_short_path_city(start_vertex, end_vertex):
#     path = ""
#     current_vertex = end_vertex
#     while current_vertex is not start_vertex:
#         my_package_object = myHashTable.search(int(current_vertex.vert_index))
#         path = " -> " + my_package_object.address + path
#         current_vertex = current_vertex.last_vertex
#     path = "WGU Hub " + path
#     return path


# dijkstras_shortest_path_algorithm(map_graph, key_list[0])
#
# print("\nDijkstra's Shortest Path:")
# for v in map_graph.adjacency_list:
#     if v.last_vertex is None and v is not key_list[0]:
#         print("1 to %s ==> no path exists" % v.label)
#     else:
#         print("1 to %s ==> %s (total distance: %g)" % (v.label, get_short_path(key_list[0], v), v.distance))

