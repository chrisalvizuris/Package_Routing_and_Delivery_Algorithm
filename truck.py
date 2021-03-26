# create a truck class that is initialized with data about the truck
class Truck:
    def __init__(self, Id, graph):
        self.Id = Id
        self.graph = graph
        self.start_location = '4001 South 700 East'
        self.current_location = '4001 South 700 East'
        self.mph = 18.0
        self.max_packages = 16
        self.time = None
        self.time_left_hub = None
        self.package_list = []
        self.path = []
        self.distance_traveled = 0.0
        self.path_miles = 0.0

    def load_package(self, package):

        # checks if the truck max package capacity has been reached
        if len(self.package_list) == self.max_packages:
            return False
        self.package_list.append(package)
        return True

    def is_truck_full(self):
        return len(self.package_list) == self.max_packages


def greedy_algorithm_for_package_loading(hash_table):

    # determine which packages to load into a truck using a greedy algorithm
    from main import myHashTable, map_graph

    truck_1 = Truck(1, map_graph)
    truck_2 = Truck(2, map_graph)
    truck_3 = Truck(3, map_graph)

    # iterate through the package hash
    for package in range(len(myHashTable.table)):

        # starting going through each package and requirements
        if myHashTable.search(package + 1).deadline == '9:00 AM':
            while len(truck_1.package_list) < len(truck_1.max_packages):
                truck_1.package_list.append(myHashTable.search(package + 1))

        if (myHashTable.search(package + 1).deadline == '10:30 AM') and (myHashTable.search(package + 1).notes is None):
            while len(truck_1.package_list) < len(truck_1.max_packages):
                truck_1.package_list.append(myHashTable.search(package + 1))


