from hashTable import ChainingHashTable
from graph import Graph
from distance import load_distance_data
from readCSV import load_package_data

map_graph = Graph()
distance_dict = {}

load_distance_data('WGUPS Distance Table.csv')

key_list = list(map_graph.adjacency_list.keys())

myHashTable = ChainingHashTable()

load_package_data('WGUPS Package File.csv')



