import datetime
from truck import truck_1, truck_2, truck_3, greedy_algorithm_for_package_loading, send_out_trucks, calculate_path_miles
from readCSV import myHashTable


greedy_algorithm_for_package_loading(truck_1, truck_2, truck_3, myHashTable)
total_miles = calculate_path_miles(truck_1) + calculate_path_miles(truck_2) + calculate_path_miles(truck_3)
send_out_trucks(truck_1, truck_2, truck_3)


def time_conversion(times):
    (h, m, s) = times.split(':')
    return datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))


input_prompt = """Select an option below or enter 'X' to exit:
    1. View All Packages
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
            except IndexError:
                print(IndexError)
                exit()
            except ValueError:
                print("Invalid time entry")
                menu_prompt = input(input_prompt)
        elif menu_prompt == 'X':
            exit()
    exit()
