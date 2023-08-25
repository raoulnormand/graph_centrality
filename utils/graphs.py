"""
Creates the Graph class and defines different methods to compute centrality.
"""

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


def compute_centrality(graph, cent_type, alpha=0.85):
    """
    Returns the centrality of each vertex as a dictionary.
    Centrality can be 'in' (in-degree), 'out' (out-degree),
    'ev' (eigenvector), 'Katz' (Katz), or 'PR' (PageRank).
    """
    adj_mat = graph.adj_matrix()
    if cent_type == 'in':
        centrality = np.sum(adj_mat, axis=0)
    elif cent_type == 'out':
        centrality = np.sum(adj_mat, axis=1)
    elif cent_type == 'ev':
        (eigenvalues, eigenvectors) = np.linalg.eig(adj_mat.T)
        eigenvalues = list(eigenvalues)
        largest_ev_index = eigenvalues.index(max(eigenvalues))
        centrality = np.real(eigenvectors.T[largest_ev_index])
    elif cent_type == 'Katz':
        id_mat = np.eye(graph.size)
        one = np.ones((graph.size, 1))
        centrality = np.linalg.solve(id_mat - alpha*adj_mat.T, one)
        centrality = centrality.reshape(graph.size)
        print(centrality.shape)
    elif cent_type == 'PR':
        id_mat = np.eye(graph.size)
        out_degrees = np.sum(adj_mat, axis=1)
        rescaled_mat = np.zeros(adj_mat.shape)
        for i in range(graph.size):
            rescaled_mat[i] = adj_mat[i]/max(out_degrees[i], 1)
        one = np.ones((graph.size, 1))
        centrality = np.linalg.solve(id_mat - alpha*rescaled_mat.T, one)
        centrality = centrality.reshape(graph.size)
    centrality = centrality / np.sum(centrality)
    return {vertex: centrality[graph.labels[vertex]] for vertex in graph.vertices}
