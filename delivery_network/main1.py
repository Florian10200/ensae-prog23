from graph import Graph, graph_from_file, time_estimation, union_find, new_minpower, new_minpower_aux, bfs, route_from_file, truck_from_file
from graph import truck_affectation
import time
from time import perf_counter

import sys 
sys.path.append("delivery_network/")


G = graph_from_file("input/network.1.in")
list_trucks = truck_from_file("tests/trucks.1.in")
list_route = route_from_file("input/routes.1.in")

print(truck_affectation(G, list_route, list_trucks))

