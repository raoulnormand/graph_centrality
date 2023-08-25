from utils.graphs import Graph, compute_centrality

small_graph_connections = {'A': {'B', 'C'}, 'B': {'C'}, 'C': {'A'}}
small_graph = Graph(small_graph_connections)

big_graph_connections = {'A': {'B'},
                         'B': {'A', 'C', 'D', 'E'},
                         'C': {'B', 'E'},
                         'D': {'E'},
                         'E': {'B'},
                         'F': {'E'}
                         }
big_graph = Graph(big_graph_connections)
