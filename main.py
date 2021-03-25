import csv


# Create the hash table class with chaining
class ChainingHashTable:
    # Create a constructor
    def __init__(self, initial_capacity=40):
        # initialize the hash table with empty bucket list entries
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # insert a new item or update existing to the hash table
    def insert(self, key, item):
        # get the bucket list where this item will go
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # insert the item to the end of the bucket list
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # searches for item with matching key in hash table
    # returns the item if found or None if not found
    def search(self, key):
        # get the bucket list where this item would be
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # search for the key in the bucket list
        for key_value in bucket_list:
            # find the item's index and then return the item that is in the bucket list
            if key_value[0] == key:
                return key_value[1]
            else:
                return None

    # removes the item with matching key from the hash table
    def remove(self, key):
        # get the bucket list where this item will be removed from
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove item from bucket list if key is present
        for key_value_pair in bucket_list:

            if key_value_pair[0] == key:
                bucket_list.remove([key_value_pair[0], key_value_pair[1]])


# bestMovies = [
#     [1, 'Tom Jones'],
#     [2, 'Chris Alvizuris'],
#     [3, 'Alex Ramos'],
#     [4, 'Trisha Mejia']
# ]
#

class DeliveryPackage:
    def __init__(self, ID, address, city, state, postal, deadline, mass, notes, status):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.postal = postal
        self.deadline = deadline
        self.mass = mass
        self.notes = notes
        self.status = status

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state, self.postal, self.deadline, self.mass, self.notes, self.status)


def load_package_data(filename):
    with open(filename) as csv_file:
        package_data = csv.reader(csv_file)
        next(package_data) # skip header
        for package in package_data:
            package_id = int(package[0]) # this needs to be an int for the code to work
            package_address = package[1]
            package_city = package[2]
            package_state = package[3]
            package_zip = package[4]
            package_deadline = package[5]
            package_weight = package[6]
            package_notes = package[7]
            package_status = "At the hub"

            package_to_deliver = DeliveryPackage(package_id, package_address, package_city, package_state, package_zip, package_deadline, package_weight, package_notes, package_status)

            myHashTable.insert(package_id, package_to_deliver)


myHashTable = ChainingHashTable()


load_package_data('WGUPS Package File.csv')

for i in range(len(myHashTable.table)):
    print("Key: {} and Package: {}".format(i+1, myHashTable.search(i+1)))


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


# load the distance data and then create a graph from it
def load_distance_data(filename):
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
    print(count)


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


def dijkstras_shortest_path_algorithm(g, starting_vertex):
    unvisited_queue = []
    for current_vertex in g.adjacency_list:
        unvisited_queue.append(current_vertex)

    starting_vertex.distance = 0
    while len(unvisited_queue) > 0:
        smallest_index = 0
        for j in range(1, len(unvisited_queue)):
            if unvisited_queue[j].distance < unvisited_queue[smallest_index].distance:
                smallest_index = j
        current_vertex = unvisited_queue.pop(smallest_index)

        for adj_vertex in g.adjacency_list[current_vertex]:
            edge_weight = g.edge_weights[(current_vertex, adj_vertex)]
            alt_path_distance = current_vertex.distance + edge_weight

            if alt_path_distance < adj_vertex.distance:
                adj_vertex.distance = alt_path_distance
                adj_vertex.last_vertex = current_vertex


def get_short_path(start_vertex, end_vertex):
    path = ""
    current_vertex = end_vertex
    while current_vertex is not start_vertex:
        path = " -> " + str(current_vertex.label) + path
        current_vertex = current_vertex.last_vertex
    path = str(start_vertex.label) + path
    return path


# def get_short_path_city(start_vertex, end_vertex):
#     path = ""
#     current_vertex = end_vertex
#     while current_vertex is not start_vertex:
#         my_package_object = myHashTable.search(int(current_vertex.vert_index))
#         path = " -> " + my_package_object.address + path
#         current_vertex = current_vertex.last_vertex
#     path = "WGU Hub " + path
#     return path


map_graph = Graph()


load_distance_data('WGUPS Distance Table.csv')


key_list = list(map_graph.adjacency_list.keys())


dijkstras_shortest_path_algorithm(map_graph, key_list[0])

print("\nDijkstra's Shortest Path:")
for v in map_graph.adjacency_list:
    if v.last_vertex is None and v is not key_list[0]:
        print("1 to %s ==> no path exists" % v.label)
    else:
        print("1 to %s ==> %s (total distance: %g)" % (v.label, get_short_path(key_list[0], v), v.distance))


# print("\nDijkstra's Shortest Path with addresses:")
# p = 1
# for v in map_graph.adjacency_list:
#     my_package = myHashTable.search(p)
#     if v.last_vertex is None and v is not key_list[0]:
#         print("WGU Hub to %s ==> no path exists" % my_package.address)
#     else:
#         print("WGU Hub to %s ==> %s (total distance: %g)" % (my_package.address, get_short_path_city(key_list[0], v),
#                                                              v.distance))
#     p += 1
package_distance_into_dict(myHashTable)