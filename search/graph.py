import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def get_nodes(self):
        """
        Return all of the nodes in the graph
        """
        return self.graph.nodes()

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """
        # make a list for the queue
        queue = []
        # make a dictionary for hte visited nodes and the path
        visited = {}
        # start the queue with the start
        # make them tuples of a node and the search order
        queue.append((start, [start]))
        # mark the start node as visited
        visited[start] = True
        
        # go through the queue
        while queue:
            # current node and path
            current, cur_path = queue.pop(0)
            
            # if it is the end node, stop
            # * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
            if current == end:
                return cur_path
            
            # all the neighbors of the current node
            # also check that the start node exists
            try:
                neighbors = self.graph[current]
            except KeyError as e:
                # returns nothing if the start node does not exist
                return None
            
            # go through all the neighbors
            for neighbor in neighbors:
                # if a neighbor has not been visited, continue
                if neighbor not in visited:
                    # make it visited
                    visited[neighbor] = True
                    # add the neighbor and path to the queue
                    queue.append((neighbor, cur_path + [neighbor]))
        
        # * If there is an end node input and a path does not exist, return None
        if end is not None:
            return None
        # * If there's no end node input, return a list nodes with the order of BFS traversal
        else:
            return list(visited.keys())




