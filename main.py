import datetime
from truck import truck_1, truck_2, truck_3, greedy_algorithm_for_package_loading, send_out_trucks, calculate_path_miles
from readCSV import myHashTable


greedy_algorithm_for_package_loading(truck_1, truck_2, truck_3, myHashTable)
total_miles = calculate_path_miles(truck_1) + calculate_path_miles(truck_2) + calculate_path_miles(truck_3)
print('Total miles is:' + str(total_miles))
send_out_trucks(truck_1, truck_2, truck_3)


def time_conversion(time):
    (h, m, s) = time.split(':')
    return datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

