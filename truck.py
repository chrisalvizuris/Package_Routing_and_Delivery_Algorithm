import collections
import datetime

# create a truck class that is initialized with data about the truck
from graph import Vertex
from main import map_graph, myHashTable, distance_dict


class Truck:
    def __init__(self, Id, graph):
        self.Id = Id
        self.graph = graph
        self.start_location = '4001 South 700 East'
        self.current_location = '4001 South 700 East'
        self.previous_location = None
        self.mph = 18.0
        self.max_packages = 16
        self.time = datetime.datetime(1, 1, 1, 1, 1, 1)
        self.time_left_hub = datetime.datetime(1, 1, 1, 1, 1, 1)
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


print('Truck 1 path miles:', calculate_path_miles(truck_1))
print('Truck 2 path miles:', calculate_path_miles(truck_2))
print('Truck 3 path miles:', calculate_path_miles(truck_3))


# return the number of miles between two addresses
def miles_between_locations(location1, location2):
    return distance_dict[location1, location2]



def send_out_trucks(truck_1, truck_2, truck_3):
    truck_1.time_left_hub = datetime.datetime(100, 1, 1, 8, 0, 0)
    truck_1.time = datetime.datetime(100, 1, 1, 8, 0, 0)
    truck_2.time_left_hub = datetime.datetime(100, 1, 1, 9, 5, 1)
    truck_2.time = datetime.datetime(100, 1, 1, 9, 5, 1)
    truck_3.time_left_hub = datetime.datetime(100, 1, 1, 9, 5, 1)
    truck_3.time = datetime.datetime(100, 1, 1, 9, 5, 1)

    # send out truck 1
    truck_1.path.popleft()
    truck1_path_copy = list(truck_1.path)
    for i, path in enumerate(truck1_path_copy):
        truck_1.distance_traveled += distance_dict[truck_1.current_location, truck1_path_copy[i]]
        distance_in_minutes = 3.33 * distance_dict[truck_1.current_location, truck1_path_copy[i]]
        # need to add the time ... possibly need to use datetime instead of time objects

        minutes_added = datetime.timedelta(minutes=distance_in_minutes)
        truck_1.time = truck_1.time + minutes_added
        for package in range(len(truck_1.package_list)):
            if truck_1.package_list[package].address == truck1_path_copy[i]:
                print('package address is equal to path')
                truck_1.package_list[package].status = "delivered"
                # truck_1.package_list.remove(truck_1.package_list[package])
        truck_1.current_location = truck1_path_copy[i]
        print('Truck 1 path:', truck_1.path)
        truck_1.path.popleft()
        print('Truck 1 made a stop at', truck_1.time.time())
    print('Truck 1 package list:', truck_1.package_list[1])

    print('')
    # send out truck 2
    truck_2.path.popleft()
    truck2_path_copy = list(truck_2.path)
    for i, path in enumerate(truck2_path_copy):
        truck_2.distance_traveled += distance_dict[truck_2.current_location, truck2_path_copy[i]]
        distance_in_minutes2 = 3.33 * distance_dict[truck_2.current_location, truck2_path_copy[i]]

        minutes_added = datetime.timedelta(minutes=distance_in_minutes2)
        truck_2.time = truck_2.time + minutes_added
        for package in range(len(truck_2.package_list)):
            if truck_2.package_list[package].address == truck2_path_copy[i]:
                truck_2.package_list[package].status = "delivered"
                # truck_2.package_list.remove(package)
        truck_2.current_location = truck2_path_copy[i]
        print('Truck 2 path:', truck_2.path)
        truck_2.path.popleft()
        print('Truck 2 made a stop at', truck_2.time.time())

    print('')
    # send out truck 3
    truck_3.path.popleft()
    truck3_path_copy = list(truck_3.path)
    for i, path in enumerate(truck3_path_copy):
        truck_3.distance_traveled += distance_dict[truck_3.current_location, truck3_path_copy[i]]
        distance_in_minutes3 = 3.33 * distance_dict[truck_3.current_location, truck3_path_copy[i]]

        minutes_added = datetime.timedelta(minutes=distance_in_minutes3)
        truck_3.time = truck_3.time + minutes_added
        for package in range(len(truck_3.package_list)):
            if truck_3.package_list[package].address == truck3_path_copy[i]:
                truck_3.package_list[package].status = "delivered"
                # truck_3.package_list.remove(package)
        truck_3.current_location = truck3_path_copy[i]
        print('Truck 3 path:', truck_3.path)
        truck_3.path.popleft()
        print('Truck 3 made a stop at', truck_3.time.time())


send_out_trucks(truck_1, truck_2, truck_3)
