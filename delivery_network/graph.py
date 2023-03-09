class Graph:
    """
    A class representing graphs as adjacency lists and implementing various algorithms on the graphs. Graphs in the class are not oriented. 
    Attributes: 
    -----------
    nodes: NodeType
        A list of nodes. Nodes can be of any immutable type, e.g., integer, float, or string.
        We will usually use a list of integers 1, ..., n.
    graph: dict
        A dictionnary that contains the adjacency list of each node in the form
        graph[node] = [(neighbor1, p1, d1), (neighbor1, p1, d1), ...]
        where p1 is the minimal power on the edge (node, neighbor1) and d1 is the distance on the edge
    nb_nodes: int
        The number of nodes.
    nb_edges: int
        The number of edges. 
    """

    def __init__(self, nodes=[]):
        """
        Initializes the graph with a set of nodes, and no edges. 
        Parameters: 
        -----------
        nodes: list, optional
            A list of nodes. Default is empty.
        """
        self.nodes = nodes
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0
    

    def __str__(self):
        """Prints the graph as a list of neighbors for each node (one per line)"""
        if not self.graph:
            output = "The graph is empty"            
        else:
            output = f"The graph has {self.nb_nodes} nodes and {self.nb_edges} edges.\n"
            for source, destination in self.graph.items():
                output += f"{source}-->{destination}\n"
        return output
    
    def add_edge(self, node1, node2, power_min, dist=1):
        """
        Adds an edge to the graph. Graphs are not oriented, hence an edge is added to the adjacency list of both end nodes. 

        Parameters: 
        -----------
        node1: NodeType
            First end (node) of the edge
        node2: NodeType
            Second end (node) of the edge
        power_min: numeric (int or float)
            Minimum power on this edge
        dist: numeric (int or float), optional
            Distance between node1 and node2 on the edge. Default is 1.
        """
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

        infini = 10^9
        distance_list = [infini for node in self.nodes]
        distance_list[src] = 0

            
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
        """
        The result should be a set of frozensets (one per component), 
        For instance, for network01.in: {frozenset({1, 2, 3}), frozenset({4, 5, 6, 7})}
        """
        return set(map(frozenset, self.connected_components()))
    

    def min_power(self, src, dest):
        power_list = []

        def get_path_with_power(self, src, dest, power):
            visited_nodes = {node : False for node in self.nodes}
            
            def finding_a_path(node, path):
                if node == dest:
                    return path
                for neighbor in self.graph[node]:
                    neighbor, power_min, dist = neighbor
                    if not visited_nodes[neighbor] and power_min <= power:
                        visited_nodes[neighbor] = True
                        result = finding_a_path(neighbor, path+[neighbor])
                        if result is not None:
                            return result
                return None

            return finding_a_path(src, [src])
        
        def binary_search(self,L): #L is a liste
            left,right = 0,(len(L)-1)
            while left != right:
                middle = (left+right)//2
                path = get_path_with_power(self, src, dest, L[middle])
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
        if get_path_with_power(self, src, dest, power_max) == None: #to avoid the case where there is no path
            return None
        else:
            return binary_search(self,power_list)

        raise NotImplementedError


def graph_from_file(filename):
    """
    Reads a text file and returns the graph as an object of the Graph class.

    The file should have the following format: 
        The first line of the file is 'n m'
        The next m lines have 'node1 node2 power_min dist' or 'node1 node2 power_min' (if dist is missing, it will be set to 1 by default)
        The nodes (node1, node2) should be named 1..n
        All values are integers.

    Parameters: 
    -----------
    filename: str
        The name of the file

    Outputs: 
    -----------
    g: Graph
        An object of the class Graph with the graph from file_name.
    """
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


    def Dijkstra(self,src,dest):
        infini = 10^9
        distance_list = [infini for node in self.nodes]
        distance_list[src] = 0
        predecessor = [infini for node in self.nodes]

        def finding_min(non_reached_nodes):
            mini = infini
            vertex = -1
            for node in non_reached_nodes:
                if distance_list[node] < mini:
                    mini = distance_list[node]
                    vertex = node
            return(vertex)

        def weight(node1,node2):
            for neighbor in self.graph[node1]:
                if neighbor[0] == node2:
                    return neighbor[2]
            return("Erreur")

        def distance_update(node1,node2):
            if distance_list[node2] > distance_list[node1] + weight(node1,node2):
                distance_list[node2] = distance_list[node1] + weight(node1,node2)
                predecessor[node2] = node1

        my_non_reached_node = (self.nodes).remove(src)
        while my_non_reached_node != []:
            node_min = finding_min(my_non_reached_node)
            my_non_reached_node.remove(node_min)
            for neighbor_of_node_min:
                distance_update(node_min, neighbor)
        moving_node = dest
        min_path = []
        while moving_node != src:
            min_path = [moving_node] + min_path
            moving_node = predecessor[moving_node]
        min_path = [src] + min_path



 
