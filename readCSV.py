import csv
from deliveryPackage import DeliveryPackage


def load_package_data(filename):
    from main import myHashTable
    with open(filename) as csv_file:
        package_data = csv.reader(csv_file)
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
        for i in range(len(myHashTable.table)):
            print("Key: {} and Package: {}".format(i+1, myHashTable.search(i+1)))