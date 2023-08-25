import numpy as np

#Creates the Graph class

class Graph:
    """
    Creates a Graph class and associated methods
    """
    def __init__(self,graph_dict=None):
        if graph_dict is None:
            graph_dict = {}
        # Create vertices
        self.vertices = graph_dict.keys()
        # Create edges
        self.edges = { (start, end) for start in self.vertices
                      for end in graph_dict[start]
                      }
        # Size of the graph
        self.size = len(self.vertices)
        # Convert vertices to integer lables
        self.labels = { vertex: label for (label, vertex) in enumerate(self.vertices)}
        # Create adjacency matrix
    def adj_matrix(self):
        """
        Creates the adjacency matric of the graph.
        """
        mat = np.zeros((self.size, self.size))
        for edge in self.edges:
            mat[self.labels[edge[0]], self.labels[edge[1]]] = 1
        return mat
    
