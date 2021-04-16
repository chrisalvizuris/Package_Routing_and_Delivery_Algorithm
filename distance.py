import csv
from graph import Vertex, Graph
from readCSV import myHashTable


"""
O(N^2)

Reads the 'WGUPS Distance Table.csv' file and adds it to a graph object, called map_graph.

I create Vertices of each location and add those to the graph.

I create a dictionary of the superset for the locations. Two locations will be the key of the dictionary (distance_dict)
and the value is the distance between those two destinations.

Since the algorithm iterates over two for loops, it is O(N^2).
"""
location_name_list = []
double_name_list = []
mile_list = []
distance_dict = {}
# I created two lists of vertices that are added below. Then I created a list of miles in mile_list
with open('WGUPS Distance Table.csv') as csv_file:
    distance_data = csv.DictReader(csv_file)
    map_graph = Graph()
    for row in distance_data:
        new_vertex = Vertex(str(row['Addresses']))
        map_graph.add_vertex(new_vertex)
        location_name_list.append(new_vertex)
        double_name_list.append(new_vertex)
        mile_values = list(row.values())
        mile_list.append(mile_values)
    count = 0
    # Start iterating through two lists of addresses and use those as the keys for the dictionary
    for k, first_vertex in enumerate(location_name_list):
        for j, second_vertex in enumerate(double_name_list):
            map_graph.add_directed_edge(first_vertex, second_vertex, float(mile_list[k][j + 2]))
            distance_dict[str(first_vertex.label), str(second_vertex.label)] = float(mile_list[k][j + 2])
            count += 1


"""
O(N)

Created a dictionary to pull data from package hash table. Package address is the key, and packages are in list.
"""
from collections import defaultdict

package_distance_dict = defaultdict(list)

for i in range(len(myHashTable.table)):
    package_object_list = []
    package_object_list.append(myHashTable.search(i + 1).ID)
    package_object_list.append(myHashTable.search(i + 1).address)
    package_object_list.append(myHashTable.search(i + 1).city)
    package_object_list.append(myHashTable.search(i + 1).state)
    package_object_list.append(myHashTable.search(i + 1).postal)
    package_object_list.append(myHashTable.search(i + 1).deadline)
    package_object_list.append(myHashTable.search(i + 1).mass)
    package_object_list.append(myHashTable.search(i + 1).notes)
    package_object_list.append(myHashTable.search(i + 1).status)

    package_distance_dict[myHashTable.search(i + 1).address].append(package_object_list)
