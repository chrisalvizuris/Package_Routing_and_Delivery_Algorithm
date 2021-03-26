# create a truck class that is initialized with data about the truck
class Truck:
    def __init__(self, Id, graph, start_location, current_location, mph=18.0, max_packages=16):
        self.Id = Id
        self.graph = graph
        self.start_location = start_location
        self.current_location = current_location
        self.mph = mph
        self.max_packages = max_packages
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

