from graph import Graph, graph_from_file, time_estimation, union_find, new_minpower, new_minpower_aux, bfs, route_from_file, truck_from_file
from graph import truck_affectation, knapsack
import time
from time import perf_counter

import sys 
sys.path.append("delivery_network/")


G = graph_from_file("input/network.1.in")
list_trucks = truck_from_file("tests/trucks.0.in")
list_route = route_from_file("input/routes.1.in")

print(knapsack(G, list_trucks, list_route))

