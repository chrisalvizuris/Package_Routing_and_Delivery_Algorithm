import datetime
from truck import truck_1, truck_2, truck_3, greedy_algorithm_for_package_loading, send_out_trucks, calculate_path_miles
from readCSV import myHashTable

"""
This is where I run the greedy algorithm with my hash table (which includes packages) and the three truck objects I 
created on truck.py. I then calculate the total miles of each truck's path to confirm that the total distance driven 
is under 140 miles. Then I send the trucks out. This allows me to know what time they get delivered and leave the hub.
"""
greedy_algorithm_for_package_loading(truck_1, truck_2, truck_3, myHashTable)
total_miles = calculate_path_miles(truck_1) + calculate_path_miles(truck_2) + calculate_path_miles(truck_3)
send_out_trucks(truck_1, truck_2, truck_3)


def time_conversion(times):
    """
    O(1)

    Converts the string that is passed into a datetime object. This will be used to later convert the input from the
    user. Example scenario is '08:00:00' will be converted to 08:00:00 am.

    :param times: The time input from the user, which should be a string object
    :return: Returns the datetime timedelta that will include an hour, minute, and second.
    """
    (h, m, s) = times.split(':')
    return datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))


"""
This is the prompt that the user will see when the program is running. It requests the user to make a selection from
the menu. There are currently only 2 options, exit or view packages.
"""
input_prompt = """Select an option below or enter 'X' to exit:
    1. View All Packages
    """


"""
O(N)

This is the main class that will be used to run the program. It shows a menue to the user, requests input, and then 
provides results.

This also sets the delivery status for each package in the hash table for the given time entered by the user.
"""
class Main:
    global time_left_converted, time_delivered_converted, delivery_address, time_left, time_delivered, delivery_status
    print('*' * 100)
    print('WGUPS Package Routing and Delivery Program')
    print('The WGUPS Drivers Traveled a Total Distance of ' + str(total_miles) + ' miles')
    print('*' * 100)

    menu_prompt = input(input_prompt)
    while menu_prompt != 'X':
        if menu_prompt == '1':
            try:
                request_time = input('Which Time? HH:MM:SS')
                converted_user_time = time_conversion(request_time)

                for i, package in enumerate(myHashTable.table):
                    try:
                        time_left = myHashTable.search(i + 1).time_left_hub
                        time_left_converted = time_conversion(str(time_left))
                        time_delivered = myHashTable.search(i + 1).time_delivered
                        time_delivered_converted = time_conversion(str(time_delivered))
                        delivery_address = myHashTable.search(i + 1).address
                        delivery_deadline = myHashTable.search(i + 1).deadline
                    except ValueError:
                        pass
                    if time_left_converted >= converted_user_time:
                        delivery_status = 'Delivery Status: At the Hub, leaving at ' + str(time_left)
                    elif time_left_converted < converted_user_time:
                        if converted_user_time < time_delivered_converted:
                            delivery_status = 'Delivery Status: Package Currently En Route'
                        else:
                            delivery_status = 'Delivery Status: Package Delivered at ' + str(time_delivered)

                    print('Package ID: ' + str(i + 1) + ', Address: ' + delivery_address + ', Deadline: ' +
                          delivery_deadline + ', ' + delivery_status)

                print('Complete!\n\n')
                print('*' * 100)
                print('*' * 100)
                menu_prompt = input(input_prompt)
            except ValueError:
                print("Invalid time entry")
                menu_prompt = input(input_prompt)

    exit()
