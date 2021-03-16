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


def loadPackageData(filename):
    with open(filename) as csv_file:
        packageData = csv.reader(csv_file)
        next(packageData) # skip header
        for package in packageData:
            packageId = int(package[0]) # this needs to be an int for the code to work
            packageAddress = package[1]
            packageCity = package[2]
            packageState = package[3]
            packageZip = package[4]
            packageDeadline = package[5]
            packageWeight = package[6]
            packageNotes = package[7]
            packageStatus = "At Station"

            packageToDeliver = DeliveryPackage(packageId, packageAddress, packageCity, packageState, packageZip, packageDeadline, packageWeight, packageNotes, packageStatus)

            myHashTable.insert(packageId, packageToDeliver)


myHashTable = ChainingHashTable()


loadPackageData('WGUPS Package File.csv')

for i in range(len(myHashTable.table)+1):
    print("Key: {} and Package: {}".format(i+1, myHashTable.search(i+1)))