import sys 
sys.path.append("delivery_network/")

from graph import Graph, graph_from_file, time_estimation, union_find, new_minpower, new_minpower_aux, bfs, route_from_file, truck_from_file
from graph import truck_affectation, knapsack, optimized_truck, only_useful_truck
import time
from time import perf_counter


def new_time_estimation(n):
    with open("input/routes." + str(n) + ".in","r") as file:
        time_est = 0
        a = int(file.readline()) # We save the amount of itineraries
        g = graph_from_file("input/network." + str(n) + ".in")
        g.kruskal()
        for i in range(10): # Average with 10 itineraries
            node1,node2,p = map(int, file.readline().split())
            t1 = time.perf_counter()
            print(t1)
            opti = new_minpower_aux(g, node1, node2)
            t2 = time.perf_counter()
            time_est += (t2-t1)


G = graph_from_file("input/network.3.in")
list_trucks = truck_from_file("tests/trucks.0.in")
list_route = route_from_file("input/routes.3.in")[:5]

print(knapsack(G, list_trucks, list_route))
