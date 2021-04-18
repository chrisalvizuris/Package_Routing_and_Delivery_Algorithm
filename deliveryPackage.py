import datetime

"""
This is the class for the delivery packages. The packages are pulled from the 'WGUPS Package File.csv' file. They will
be later moved onto the trucks and sent out for delivery.

Each package has important attributes, such as the address it is going, the ID, the delivery deadline, special notes, 
delivery status, time it was actually delivered, and time that it left the hub.
"""


class DeliveryPackage:
    def __init__(self, ID, address, city, state, postal, deadline, mass, notes, status):
        """
        O(1)

        The constructor for the package takes in a lot of important attributes, which are pulled from the previously
        mentioned csv file.

        :param ID: Package ID
        :param address: Address where the package needs to be delivered to
        :param city: The city of the address
        :param state: The state of the address
        :param postal: The address' postal code
        :param deadline: The delivery deadline (datetime). Package must be delivered before the deadline.
        :param mass: The weight of the package.
        :param notes: Special notes (eg. Truck requirements, address changes, etc)
        :param status: The delivery status (en route, delivered, at the hub)
        """
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.postal = postal
        self.deadline = deadline
        self.mass = mass
        self.notes = notes
        self.status = status
        self.time_delivered = datetime.datetime(1, 1, 1, 1, 1, 1)
        self.time_left_hub = datetime.datetime(1, 1, 1, 1, 1, 1)
        self.truck = ""

    def __str__(self):
        """
        O(1)

        This formats the package when it is printed as a string.

        :return: Returns the properly formatted string separated with comas
        """
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state, self.postal,
                                                       self.deadline, self.mass, self.notes, self.status,
                                                               self.time_delivered, self.time_left_hub)

