This code creates a 'Graph' class. A graph is defined by a dictionary whose keys are the vertices and values the set of vertices it points too.

	from graphs import Graph, compute_centrality

	graph_connections = {'A': {'B'},
							'B': {'A', 'C', 'D', 'E'},
							'C': {'B', 'E'},
							'D': {'E'},
							'E': {'B'},
							'F': {'E'}
							}
	graph = Graph(graph_connections)

The function 'compute_centrality' returns the centrality of each vertex as a dictionary.  Centrality can be 'in' (in-degree), 'out' (out-degree), 'ev' (eigenvector), 'Katz' (Katz), or 'PR' (PageRank).

Input:
	compute_centrality(graph, 'ev')
Output
	{'A': 0.14285714285714277,
	'B': 0.285714285714286,
	'C': 0.14285714285714282,
	'D': 0.14285714285714277,
	'E': 0.28571428571428575,
	'F': 0.0}