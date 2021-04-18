import collections
import datetime
from readCSV import myHashTable
from distance import map_graph, distance_dict


class Truck:
    """
    The truck class takes in an ID and a graph. The graph (which is created from the graph class on graph.py) will later
    be used to help plot out and calculate the path that the truck drives on.

    Location:
    Every truck's starting and current location will be set to the Hub's address.

    Truck Speed:
    Each truck travels at a constant speed of 18 MPH

    Packages:
    Each truck can carry a maximum of 16 packages. The package IDs will be stored as a list in the package_list. These
    can be used when referencing the hash table that was created.

    Path:
    Each truck has a path that it can travel. This will be a container that stores addresses only.

    Time:
    Each truck has initial time and scheduled departure time, which are both set to April 13th 2021 at 01:01:01 am

    """
    def __init__(self, Id, graph):
        self.Id = Id
        self.graph = graph
        self.start_location = '4001 South 700 East'
        self.current_location = '4001 South 700 East'
        self.previous_location = None
        self.mph = 18.0
        self.max_packages = 16
        self.time = datetime.datetime(2021, 4, 13, 1, 1, 1)
        self.time_left_hub = datetime.datetime(2021, 4, 13, 1, 1, 1)
        self.package_list = collections.deque()
        self.path = collections.deque()
        self.distance_traveled = 0.0
        self.path_miles = 0.0


"""
Initialize three trucks with a graph object. These trucks are what we'll be using to run this program.
"""
truck_1 = Truck(1, map_graph)
truck_2 = Truck(2, map_graph)
truck_3 = Truck(3, map_graph)


def nearest_neighbor_path_sort(truck):
    """
    O(n^2).

    This function uses the nearest neighbor methodology to sort the truck's path. The truck's path was initially set
    when the packages were loaded onto the truck, but this algorithm will sort the path based on the next nearest
    location from the truck's current location.

    To keep track of where the truck has been and where the truck still needs to go, I've created two lists (unvisited
    and visited addresses).

    :param truck: This function takes in a truck object. I'll later use this function with the 3 truck objects I created.
    :return: This function doesn't return anything. It just sorts the delivery path that is already in the truck.
    """
    unvisited_list = list(truck.path)  # This unvisited list is a list version of the existing truck's path
    visited_list = []  # An empty list that will start to get populated as the truck visits locations on the unvisited list
    optimized_path = collections.deque()  # This dequeue will be later used to initialize a final list to the truck's path
    min_distance = 50  # just an arbitrary number to start with
    min_address = ''
    optimized_path.append(unvisited_list[0])
    current_address = unvisited_list[0]
    unvisited_list.remove(unvisited_list[0])
    # iterate through the unvisited list until it is empty. When this list is empty, the visited list should be full.
    while unvisited_list:
        count = None
        for i in range(len(unvisited_list)):
            if i in visited_list:
                break
            if distance_dict[current_address, unvisited_list[i]] < min_distance:
                min_distance = distance_dict[current_address, unvisited_list[i]]
                min_address = unvisited_list[i]
                count = i
        current_address = min_address
        optimized_path.append(min_address)
        min_distance = 50.0
        min_address = ''
        visited_list.append(current_address)
        unvisited_list.remove(unvisited_list[count])
    optimized_path.append(truck.start_location)
    truck.path = optimized_path


def greedy_algorithm_for_package_loading(truck_1, truck_2, truck_3, hash_table):
    """
    O(N^2), because it runs the nearest neighbor algorithm.

    This algorithm uses the greedy algorithm to load the packages on trucks based on a variety of conditions.

    The algorithm grabs the addresses from each package and adds that address to the truck's path if it isn't already.

    At the end of this function, I call the Nearest Neighbor algorithm to sort the Truck's path after all
    packages have been loaded.

    :param truck_1: Takes in a truck object. I'll use Truck with ID 1 here
    :param truck_2: Takes in a truck object. I'll use Truck with ID 2 here
    :param truck_3: Takes in a truck object. I'll use Truck with ID 3 here
    :param hash_table: Take in the hash table that I created - myHashTable
    :return: Returns nothing. It just runs the algorithm for the truck's package list
    """
    # determine which packages to load into a truck using a greedy algorithm
    # add to path for each truck at the end of each if statement
    # iterate through the package hash
    for i, package in enumerate(hash_table.table):

        # starting going through each package and requirements
        # truck 1 will get 9 packages
        if (hash_table.search(i + 1).deadline == '10:30 AM') and (
                hash_table.search(i + 1).notes == '') and (hash_table.search(i + 1).ID != 13) and (hash_table.search(i + 1).ID != 34) and (
                hash_table.search(i + 1).ID not in truck_3.package_list and hash_table.search(i + 1).ID not in truck_2.package_list):
            truck_1.package_list.appendleft(hash_table.search(i + 1).ID)
            hash_table.search(i + 1).truck = "Truck 1"
            if hash_table.search(i + 1).address not in truck_1.path:
                truck_1.path.appendleft(hash_table.search(i + 1).address)

        elif hash_table.search(i + 1).deadline == '10:30 AM' and 'Delayed on flight' in hash_table.search(i + 1).notes \
                and (hash_table.search(i + 1).mass == '88' or '7') and hash_table.search(i + 1).ID not in truck_3.package_list and \
                hash_table.search(i + 1).ID not in truck_2.package_list:
            truck_1.package_list.append(hash_table.search(i + 1).ID)
            hash_table.search(i + 1).truck = "Truck 1"
            if hash_table.search(i + 1).address not in truck_1.path:
                truck_1.path.append(hash_table.search(i + 1).address)

        # truck 2 will get 16 packages
        # 9am package will be added to truck 2
        elif hash_table.search(i + 1).deadline == '9:00 AM':
            truck_2.package_list.appendleft(hash_table.search(i + 1).ID)
            hash_table.search(i + 1).truck = "Truck 2"
            if hash_table.search(i + 1).address not in truck_2.path:
                truck_2.path.appendleft(hash_table.search(i + 1).address)

        elif '1060' in hash_table.search(i + 1).address:
            truck_2.package_list.append(hash_table.search(i + 1).ID)
            hash_table.search(i + 1).truck = "Truck 2"
            if hash_table.search(i + 1).address not in truck_2.path:
                truck_2.path.append(hash_table.search(i + 1).address)

        elif '2010' in hash_table.search(i + 1).address and hash_table.search(i + 1).deadline == '10:30 AM':
            truck_2.package_list.appendleft(hash_table.search(i + 1).ID)
            hash_table.search(i + 1).truck = "Truck 2"
            if hash_table.search(i + 1).address not in truck_2.path:
                truck_2.path.appendleft(hash_table.search(i + 1).address)

        # 10:30 am packages required for truck 2 will be added
        elif (hash_table.search(i + 1).deadline == '10:30 AM') and \
                (('Must be delivered' in hash_table.search(i + 1).notes) or (hash_table.search(i + 1).ID == 34)):
            truck_2.package_list.appendleft(hash_table.search(i + 1).ID)
            hash_table.search(i + 1).truck = "Truck 2"
            if hash_table.search(i + 1).address not in truck_2.path:
                truck_2.path.appendleft(hash_table.search(i + 1).address)

        # packages specifically needed on truck 2 but EOD are added to the right of deque
        elif (hash_table.search(i + 1).deadline == 'EOD') and \
                (hash_table.search(i + 1).notes == 'Can only be on truck 2'):
            truck_2.package_list.append(hash_table.search(i + 1).ID)
            hash_table.search(i + 1).truck = "Truck 2"
            if hash_table.search(i + 1).address not in truck_2.path:
                truck_2.path.append(hash_table.search(i + 1).address)

        # adding extra EOD packages to end of truck 2 to fill it to max capacity if they aren't already in truck 1
        elif (hash_table.search(i + 1).deadline == 'EOD') and (hash_table.search(i + 1).notes == '') and \
                (hash_table.search(i + 1).ID >= 24) and (hash_table.search(i + 1).ID not in truck_1.package_list):
            if len(truck_2.package_list) < truck_2.max_packages:
                truck_2.package_list.append(hash_table.search(i + 1).ID)
                hash_table.search(i + 1).truck = "Truck 2"
                if hash_table.search(i + 1).address not in truck_2.path:
                    truck_2.path.append(hash_table.search(i + 1).address)

        # truck 2 will add the delayed packages that have a deadline to the left of deque
        elif (hash_table.search(i + 1).deadline == '10:30 AM') and \
                (hash_table.search(i + 1).notes == 'Delayed on flight---will not arrive to depot until 9:05 am') and \
                hash_table.search(i + 1).ID not in truck_3.package_list and hash_table.search(i + 1).ID not in truck_1.package_list:
            if len(truck_2.package_list) < truck_2.max_packages:
                truck_2.package_list.appendleft(hash_table.search(i + 1).ID)
                hash_table.search(i + 1).truck = "Truck 2"
                if hash_table.search(i + 1).address not in truck_2.path:
                    truck_2.path.appendleft(hash_table.search(i + 1).address)

        # truck 3 will start getting 16 packages
        elif (hash_table.search(i + 1).deadline == 'EOD') and \
                (hash_table.search(i + 1).notes == 'Delayed on flight---will not arrive to depot until 9:05 am' or
                    hash_table.search(i + 1).notes == 'Wrong address listed'):
            if len(truck_3.package_list) < truck_3.max_packages:
                truck_3.package_list.append(hash_table.search(i + 1).ID)
                hash_table.search(i + 1).truck = "Truck 3"
                if hash_table.search(i + 1).address not in truck_3.path:
                    truck_3.path.append(hash_table.search(i + 1).address)

        # truck 3 will add the rest of the non-urgent packages that aren't already in trucks 1 and 2
        elif (hash_table.search(i + 1).deadline == 'EOD' and hash_table.search(i + 1).notes == '') and (
                hash_table.search(i + 1).ID not in truck_1.package_list and hash_table.search(i + 1).ID not in truck_2.package_list):
            if len(truck_3.package_list) < truck_3.max_packages:
                truck_3.package_list.append(hash_table.search(i + 1).ID)
                hash_table.search(i + 1).truck = "Truck 3"
                if hash_table.search(i + 1).address not in truck_3.path:
                    truck_3.path.append(hash_table.search(i + 1).address)
    truck_1.path.appendleft(truck_1.start_location)
    truck_2.path.appendleft(truck_2.start_location)
    truck_3.path.appendleft(truck_3.start_location)

    # run the nearest neighbor to sort the path from each truck
    nearest_neighbor_path_sort(truck_1)
    nearest_neighbor_path_sort(truck_2)
    nearest_neighbor_path_sort(truck_3)


# calculate total path miles for a given truck
def calculate_path_miles(truck):
    """
    O(N)

    Calculate the total path miles for a given truck. This will be used later to calculate the total distance traveled.
    :param truck: Takes in a truck object as parameter, and uses the truck's path_miles attribute.
    :return: Total path miles driven by the truck
    """
    for i, location in enumerate(truck.path):
        if i > 0:
            prev = truck.path[i - 1]
            curr = truck.path[i]

            truck.path_miles += distance_dict[prev, curr]
    return truck.path_miles


def send_out_trucks(truck_1, truck_2, truck_3):
    """
    O(N^2)

    This function takes in truck objects and sends them out. It initializes their time and time they leave the hub. It
    also updates the status once they leave and when they're delivered.

    :param truck_1: Takes in a truck object. I'll use Truck with ID 1 here
    :param truck_2: Takes in a truck object. I'll use Truck with ID 2 here
    :param truck_3: Takes in a truck object. I'll use Truck with ID 3 here
    :return: Doesn't return anything. It just update's the truck's status and time after sending out.
    """
    truck_1.time_left_hub = datetime.datetime(2021, 4, 13, 9, 5, 1)
    truck_1.time = datetime.datetime(2021, 4, 13, 9, 5, 1)
    truck_2.time_left_hub = datetime.datetime(2021, 4, 13, 8, 0, 0)
    truck_2.time = datetime.datetime(2021, 4, 13, 8, 0, 0)
    truck_3.time_left_hub = datetime.datetime(2021, 4, 13, 10, 30, 0)
    truck_3.time = datetime.datetime(2021, 4, 13, 10, 30, 0)

    # set time left hub for packages on each truck and update package status to in route
    for package in range(len(truck_1.package_list)):
        myHashTable.search(truck_1.package_list[package]).time_left_hub = truck_1.time_left_hub.time()
        myHashTable.search(truck_1.package_list[package]).status = "En Route - Truck 1"

    for package in range(len(truck_2.package_list)):
        myHashTable.search(truck_2.package_list[package]).time_left_hub = truck_2.time_left_hub.time()
        myHashTable.search(truck_2.package_list[package]).status = "En Route - Truck 2"

    for package in range(len(truck_3.package_list)):
        myHashTable.search(truck_3.package_list[package]).time_left_hub = truck_3.time_left_hub.time()
        myHashTable.search(truck_3.package_list[package]).status = "En Route - Truck 3"

    # send out truck 1
    # pop the first item in the path because it is the hub's address
    truck_1.path.popleft()
    truck1_path_copy = list(truck_1.path)
    # iterate through the copy of the truck's path and the package list, O(N^2)
    for i, path in enumerate(truck1_path_copy):
        truck_1.distance_traveled += distance_dict[truck_1.current_location, truck1_path_copy[i]]
        distance_in_minutes = 3.33 * distance_dict[truck_1.current_location, truck1_path_copy[i]]
        minutes_added = datetime.timedelta(minutes=distance_in_minutes)
        truck_1.time = truck_1.time + minutes_added
        for package in range(len(truck_1.package_list)):
            if myHashTable.search(truck_1.package_list[package]).address == truck1_path_copy[i]:
                myHashTable.search(truck_1.package_list[package]).status = "Delivered at " + str(truck_1.time.time())
                myHashTable.search(truck_1.package_list[package]).time_delivered = truck_1.time.time().strftime('%H:%M:%S')
        truck_1.current_location = truck1_path_copy[i]
        truck_1.path.popleft()

    # send out truck 2
    # pop the first item in the path because it is the hub's address
    truck_2.path.popleft()
    truck2_path_copy = list(truck_2.path)
    # iterate through the copy of the truck's path and the package list, O(N^2)
    for i, path in enumerate(truck2_path_copy):
        truck_2.distance_traveled += distance_dict[truck_2.current_location, truck2_path_copy[i]]
        distance_in_minutes2 = 3.33 * distance_dict[truck_2.current_location, truck2_path_copy[i]]
        minutes_added = datetime.timedelta(minutes=distance_in_minutes2)
        truck_2.time = truck_2.time + minutes_added
        for package in range(len(truck_2.package_list)):
            if myHashTable.search(truck_2.package_list[package]).address == truck2_path_copy[i]:
                myHashTable.search(truck_2.package_list[package]).status = "Delivered at " + str(truck_2.time.time())
                myHashTable.search(truck_2.package_list[package]).time_delivered = truck_2.time.time().strftime('%H:%M:%S')
        truck_2.current_location = truck2_path_copy[i]
        truck_2.path.popleft()

    # send out truck 3
    # pop the first item in the path because it is the hub's address
    truck_3.path.popleft()
    truck3_path_copy = list(truck_3.path)
    # iterate through the copy of the truck's path and the package list, O(N^2)
    for i, path in enumerate(truck3_path_copy):
        truck_3.distance_traveled += distance_dict[truck_3.current_location, truck3_path_copy[i]]
        distance_in_minutes3 = 3.33 * distance_dict[truck_3.current_location, truck3_path_copy[i]]
        minutes_added = datetime.timedelta(minutes=distance_in_minutes3)
        truck_3.time = truck_3.time + minutes_added
        for package in range(len(truck_3.package_list)):
            if myHashTable.search(truck_3.package_list[package]).address == truck3_path_copy[i]:
                myHashTable.search(truck_3.package_list[package]).status = "Delivered at " + str(truck_3.time.time())
                myHashTable.search(truck_3.package_list[package]).time_delivered = truck_3.time.time().strftime('%H:%M:%S')
        truck_3.current_location = truck3_path_copy[i]
        truck_3.path.popleft()
