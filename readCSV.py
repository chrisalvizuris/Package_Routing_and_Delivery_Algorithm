import csv
from deliveryPackage import DeliveryPackage
from hashTable import ChainingHashTable

"""
O(N)

Reads the 'WGUPS Package File.csv' file and adds each package into a ChainingHashTable object, called myHashTable.

I set the package's status to 'At the hub'.
"""
with open('WGUPS Package File.csv') as csv_file:
    package_data = csv.reader(csv_file)
    myHashTable = ChainingHashTable()
    next(package_data)  # skip header
    for package in package_data:
        package_id = int(package[0])  # this needs to be an int for the code to work
        package_address = package[1]
        package_city = package[2]
        package_state = package[3]
        package_zip = package[4]
        package_deadline = package[5]
        package_weight = package[6]
        package_notes = package[7]
        package_status = "At the hub"

        package_to_deliver = DeliveryPackage(package_id, package_address, package_city, package_state, package_zip,
                                             package_deadline, package_weight, package_notes, package_status)

        myHashTable.insert(package_id, package_to_deliver)
