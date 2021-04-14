import datetime


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
        self.time_delivered = datetime.datetime(1, 1, 1, 1, 1, 1)
        self.time_left_hub = datetime.datetime(1, 1, 1, 1, 1, 1)

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state, self.postal,
                                                       self.deadline, self.mass, self.notes, self.status,
                                                               self.time_delivered, self.time_left_hub)

