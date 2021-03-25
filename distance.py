import csv
from graph import Vertex


# load the distance data and then create a graph from it
def load_distance_data(filename):
    from main import map_graph
    # create an array to fit the names of the vertices
    location_name_list = []
    double_name_list = []
    mile_list = []
    # I created two lists of vertices that are added below. Then I created a list of miles in mile_list
    with open(filename) as csv_file:
        distance_data = csv.DictReader(csv_file)
        for row in distance_data:
            new_vertex = Vertex({row['Addresses']})
            map_graph.add_vertex(new_vertex)
            location_name_list.append(new_vertex)
            double_name_list.append(new_vertex)
            mile_values = list(row.values())
            mile_list.append(mile_values)
        print(mile_list)
        count = 0
        for k, first_vertex in enumerate(location_name_list):
            for j, second_vertex in enumerate(double_name_list):
                map_graph.add_directed_edge(first_vertex, second_vertex, float(mile_list[k][j + 2]))
                print(first_vertex, second_vertex, mile_list[k][j + 2])
                count += 1


# created a dictionary to pull data from package hash table. Package address is the key, and packages are in list.
def package_distance_into_dict(hash_table):
    from collections import defaultdict
    package_distance_dict = defaultdict(list)

    for i in range(len(hash_table.table)):
        package_object_list = []
        package_object_list.append(hash_table.search(i + 1).ID)
        package_object_list.append(hash_table.search(i + 1).address)
        package_object_list.append(hash_table.search(i + 1).city)
        package_object_list.append(hash_table.search(i + 1).state)
        package_object_list.append(hash_table.search(i + 1).postal)
        package_object_list.append(hash_table.search(i + 1).deadline)
        package_object_list.append(hash_table.search(i + 1).mass)
        package_object_list.append(hash_table.search(i + 1).notes)
        package_object_list.append(hash_table.search(i + 1).status)

        package_distance_dict[hash_table.search(i + 1).address].append(package_object_list)
    print(package_distance_dict.items())