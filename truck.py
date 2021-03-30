import collections
from datetime import time, timedelta

# create a truck class that is initialized with data about the truck
from graph import Vertex
from main import map_graph, myHashTable, distance_dict


class Truck:
    def __init__(self, Id, graph):
        self.Id = Id
        self.graph = graph
        self.start_location = '4001 South 700 East'
        self.current_location = '4001 South 700 East'
        self.mph = 18.0
        self.max_packages = 16
        self.time = time()
        self.time_left_hub = time()
        self.package_list = collections.deque()
        self.path = collections.deque()
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


truck_1 = Truck(1, map_graph)
truck_2 = Truck(2, map_graph)
truck_3 = Truck(3, map_graph)


def greedy_algorithm_for_package_loading(truck_1, truck_2, truck_3, hash_table):

    # determine which packages to load into a truck using a greedy algorithm
    # add to path for each truck at the end of each if statement
    # iterate through the package hash
    for i, package in enumerate(hash_table.table):

        # starting going through each package and requirements
        # truck 1 will get 9 packages
        if (hash_table.search(i + 1).deadline == '10:30 AM') and (
                hash_table.search(i + 1).notes == '') and (hash_table.search(i + 1).ID != 13) and (hash_table.search(i + 1).ID != 34) and (
                hash_table.search(i + 1) not in truck_3.package_list and hash_table.search(i + 1) not in truck_2.package_list):
            truck_1.package_list.appendleft(hash_table.search(i + 1))
            if hash_table.search(i + 1).address not in truck_1.path:
                truck_1.path.appendleft(hash_table.search(i + 1).address)

        elif hash_table.search(i + 1).ID == 27 or hash_table.search(i + 1).ID == 35:
            truck_1.package_list.append(hash_table.search(i + 1))
            if hash_table.search(i + 1).address not in truck_1.path:
                truck_1.path.append(hash_table.search(i + 1).address)

        # truck 2 will get 16 packages
        # 9am package will be added to truck 2
        elif hash_table.search(i + 1).deadline == '9:00 AM':
            truck_2.package_list.appendleft(hash_table.search(i + 1))
            if hash_table.search(i + 1).address not in truck_2.path:
                truck_2.path.appendleft(hash_table.search(i + 1).address)

        elif hash_table.search(i + 1).ID == 13:
            truck_2.package_list.appendleft(hash_table.search(i + 1))
            if hash_table.search(i + 1).address not in truck_2.path:
                truck_2.path.appendleft(hash_table.search(i + 1).address)

        # 10:30 am packages required for truck 2 will be added
        elif (hash_table.search(i + 1).deadline == '10:30 AM') and \
                (('Must be delivered' in hash_table.search(i + 1).notes) or (hash_table.search(i + 1).ID == 34)):
            truck_2.package_list.appendleft(hash_table.search(i + 1))
            if hash_table.search(i + 1).address not in truck_2.path:
                truck_2.path.appendleft(hash_table.search(i + 1).address)

        # packages specifically needed on truck 2 but EOD are added to the right of deque
        elif (hash_table.search(i + 1).deadline == 'EOD') and \
                (hash_table.search(i + 1).notes == 'Can only be on truck 2'):
            truck_2.package_list.append(hash_table.search(i + 1))
            if hash_table.search(i + 1).address not in truck_2.path:
                truck_2.path.append(hash_table.search(i + 1).address)

        # adding extra EOD packages to end of truck 2 to fill it to max capacity if they aren't already in truck 1
        elif (hash_table.search(i + 1).deadline == 'EOD') and (hash_table.search(i + 1).notes == '') and \
                (hash_table.search(i + 1).ID >= 24) and (hash_table.search(i + 1) not in truck_1.package_list):
            if len(truck_2.package_list) < truck_2.max_packages:
                truck_2.package_list.append(hash_table.search(i + 1))
                if hash_table.search(i + 1).address not in truck_2.path:
                    truck_2.path.append(hash_table.search(i + 1).address)

        # truck 2 will add the delayed packages that have a deadline to the left of deque
        elif (hash_table.search(i + 1).deadline == '10:30 AM') and \
                (hash_table.search(i + 1).notes == 'Delayed on flight---will not arrive to depot until 9:05 am'):
            if len(truck_2.package_list) < truck_2.max_packages:
                truck_2.package_list.appendleft(hash_table.search(i + 1))
                if hash_table.search(i + 1).address not in truck_2.path:
                    truck_2.path.appendleft(hash_table.search(i + 1).address)

        # truck 3 will start getting 16 packages
        elif (hash_table.search(i + 1).deadline == 'EOD') and \
                (hash_table.search(i + 1).notes == 'Delayed on flight---will not arrive to depot until 9:05 am' or
                    hash_table.search(i + 1).notes == 'Wrong address listed'):
            if len(truck_3.package_list) < truck_3.max_packages:
                truck_3.package_list.append(hash_table.search(i + 1))
                if hash_table.search(i + 1).address not in truck_3.path:
                    truck_3.path.append(hash_table.search(i + 1).address)

        # truck 3 will add the rest of the non-urgent packages that aren't already in trucks 1 and 2
        elif (hash_table.search(i + 1).deadline == 'EOD' and hash_table.search(i + 1).notes == '') and (
                hash_table.search(i + 1) not in truck_1.package_list and hash_table.search(i + 1) not in truck_2.package_list):
            if len(truck_3.package_list) < truck_3.max_packages:
                truck_3.package_list.append(hash_table.search(i + 1))
                if hash_table.search(i + 1).address not in truck_3.path:
                    truck_3.path.append(hash_table.search(i + 1).address)
    truck_1.path.appendleft(truck_1.start_location)
    truck_1.path.append(truck_1.start_location)
    truck_2.path.appendleft(truck_2.start_location)
    truck_2.path.append(truck_2.start_location)
    truck_3.path.appendleft(truck_3.start_location)
    truck_3.path.append(truck_3.start_location)

    print('Truck 1 packages:')
    for i in range(len(truck_1.package_list)):
        print(truck_1.package_list[i])
    print('Truck 1 path:')
    for i in range(len(truck_1.path)):
        print(truck_1.path[i])
    print('')
    print('Truck 2 packages:')
    for i in range(len(truck_2.package_list)):
        print(truck_2.package_list[i])
    print('Truck 2 path:')
    for i in range(len(truck_2.path)):
        print(truck_2.path[i])
    print('')
    print('Truck 3 packages:')
    for i in range(len(truck_3.package_list)):
        print(truck_3.package_list[i])
    print('Truck 3 path:')
    for i in range(len(truck_3.path)):
        print(truck_3.path[i])


greedy_algorithm_for_package_loading(truck_1, truck_2, truck_3, myHashTable)


# calculate total path miles for a given truck
def calculate_path_miles(truck):
    for i, location in enumerate(truck.path):
        if i > 0:
            prev = truck.path[i - 1]
            curr = truck.path[i]

            truck.path_miles += distance_dict[prev, curr]
    return truck.path_miles


print(calculate_path_miles(truck_1))

# return the number of miles between two addresses
def miles_between_locations(location1, location2):
    return distance_dict[location1, location2]



# def send_out_trucks(truck_1, truck_2, truck_3):
#     truck1.time_left_hub = time(hour=08)
#     print()
