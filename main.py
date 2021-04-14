from hashTable import ChainingHashTable
from graph import Graph
from distance import load_distance_data
from readCSV import load_package_data
import datetime

map_graph = Graph()
distance_dict = {}

load_distance_data('WGUPS Distance Table.csv')

key_list = list(map_graph.adjacency_list.keys())

myHashTable = ChainingHashTable()

load_package_data('WGUPS Package File.csv')


def time_conversion(time):
    (h, m, s) = time.split(':')
    return datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))


# which_package = input('Please enter a package ID you would like to locate')
# which_time = input('Please enter a time in the following format 00:00:00')

