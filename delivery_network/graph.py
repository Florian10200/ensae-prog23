class Graph:

    def __init__(self, nodes=[]):
        self.nodes = nodes
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0
    

    def __str__(self):
        if not self.graph:
            output = "The graph is empty"            
        else:
            output = f"The graph has {self.nb_nodes} nodes and {self.nb_edges} edges.\n"
            for source, destination in self.graph.items():
                output += f"{source}-->{destination}\n"
        return output
    
    def add_edge(self, node1, node2, power_min, dist=1):
        if node1 not in self.graph:
            self.graph[node1] = []
            self.nb_nodes += 1
            self.nodes.append(node1)
        if node2 not in self.graph:
            self.graph[node2] = []
            self.nb_nodes += 1
            self.nodes.append(node2)

        self.graph[node1].append((node2, power_min, dist))
        self.graph[node2].append((node1, power_min, dist))
        self.nb_edges += 1


    def get_path_with_power(self, src, dest, power):
        visited_nodes = {node : False for node in self.nodes}
        visited_nodes[src] = True
   
        def finding_a_path(node, path):
            if node == dest:
                return path
            for neighbor in self.graph[node]:
                neighbor, power_min, dist = neighbor[0], neighbor[1], neighbor[2]
                if not visited_nodes[neighbor] and power_min <= power:
                    visited_nodes[neighbor] = True
                    result = finding_a_path(neighbor, path+[neighbor])
                    if result is not None:
                        return result
            return None

        return finding_a_path(src, [src])

        raise NotImplementedError
    

    def connected_components(self):
        components_list = []
        visited_nodes = {node : False for node in self.nodes}

        def exploration(node):
            component = [node]
            for neighbor in self.graph[node]:
                neighbor = neighbor[0]
                if not visited_nodes[neighbor]:
                    visited_nodes[neighbor] = True
                    component += exploration(neighbor)
            return component
        
        for node in self.nodes:
            if not visited_nodes[node]:
                components_list.append(exploration(node))

        return components_list

        raise NotImplementedError


    def connected_components_set(self):
        return set(map(frozenset, self.connected_components()))
    

    def min_power(self, src, dest):
        power_list = []

        
        def binary_search(self,L): #L is a liste
            left,right = 0,(len(L)-1)
            while left != right:
                middle = (left+right)//2
                path = self.get_path_with_power( src, dest, L[middle])
                if path == None:
                    left = middle+1
                else:
                    right = middle
            return(path,L[left])

        for node in self.nodes:
            for neighbor in self.graph[node]:
                power_list.append(neighbor[1])
        F = frozenset(power_list)
        power_list = sorted(list(F))
        power_max = power_list[-1]
        if self.get_path_with_power(src, dest, power_max) == None: #to avoid the case where there is no path
            return None
        else:
            return binary_search(self,power_list)

    def Dijkstra(self,src,dest,power):
        infinity = 1000000000
        distance_list = ["décalage"] + [infinity for node in self.nodes]
        distance_list[src] = 0
        predecessor = {node : node for node in self.nodes}

        def finding_min(non_reached_nodes):
            mini = infinity
            vertex = -1
            print("distance_list",distance_list)
            for node in non_reached_nodes:
                if distance_list[node] < mini:
                    mini = distance_list[node]
                    vertex = node
            return(vertex)

        def dist(node1,node2):
            for neighbor in self.graph[node1]:
                if neighbor[0] == node2:
                    return neighbor[2]
            return("Erreur")

        def power_fct(node1,node2):
            for neighbor in self.graph[node1]:
                if neighbor[0] == node2:
                    return neighbor[1]
            return("Erreur")

        def distance_update(node1,node2):
            if (distance_list[node2] > distance_list[node1] + dist(node1,node2)) and (power_fct((node1),node2) < power) :
                distance_list[node2] = distance_list[node1] + dist(node1,node2)
                predecessor[node2] = node1

        my_non_reached_node = (list(self.nodes))
        while my_non_reached_node != []:
            print("my_non_reached_non",my_non_reached_node)
            node_min = finding_min(my_non_reached_node)
            print("node_min",node_min)
            my_non_reached_node.remove(node_min)
            for neighbor in self.graph[node_min]:
                neighbor = neighbor[0]
                distance_update(node_min, neighbor)
        moving_node = dest
        min_path = []
        while moving_node != src:
            min_path = [moving_node] + min_path
            moving_node = predecessor[moving_node]
        min_path = [src] + min_path
        return(min_path)


def graph_from_file(filename):

    with open(filename, "r") as file:
        n, m = map(int, file.readline().split())
        g = Graph(range(1, n+1))
        for _ in range(m):
            edge = list(map(int, file.readline().split()))
            if len(edge) == 3:
                node1, node2, power_min = edge
                g.add_edge(node1, node2, power_min) # will add dist=1 by default
            elif len(edge) == 4:
                node1, node2, power_min, dist = edge
                g.add_edge(node1, node2, power_min, dist)
            else:
                raise Exception("Format incorrect")
    return g
 
