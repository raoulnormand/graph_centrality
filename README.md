# Introduction

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

Compare with PageRank:

	compute_centrality(graph, 'PR')

	{'A': 0.10734492411964049,
	'B': 0.3875055252688964,
	'C': 0.10734492411964049,
	'D': 0.10734492411964049,
	'E': 0.2654597023721821,
	'F': 0.025000000000000005}

# Another example and more details

	graph_connections = {'A': {'F'},
						'B': {'C', 'D', 'E', 'G'},
						'C': {'A', 'B'},
						'D': {'A', 'B'},
						'E': {'A', 'B'},
						'F': {},
						'G': {}
						}
	graph = Graph(graph_connections)

With eigenvalue centrality, A and B get their centrality from C, D, E, so they have the same centrality. The other vertices get their centrality from A and B only, so they also have the same centrality.

	{'A': 0.2046349259880297,
	'B': 0.20463492598802974,
	'C': 0.11814602960478814,
	'D': 0.1181460296047881,
	'E': 0.11814602960478805,
	'F': 0.11814602960478812,
	'G': 0.11814602960478814}

With pageRank, the same applies, with a twist. However, A only points to F, whereas B points to C, D, E, and G. In PageRank, the centrality is diluted by the out-degree, so F gains a massive amount of centrality from A, whereas C, D, E, and G only gain some portion of B's centrality. It is worth noting that F becomes the most important vertex in this context, which may not be what one would desire. Naturally, this is mostly due to the small size of the graph.Decreasing the parameter $\alpha$ would fix this. 

	{'A': 0.188596150358799,
	'B': 0.188596150358799,
	'C': 0.10051553068573353,
	'D': 0.10051553068573353,
	'E': 0.10051553068573355,
	'F': 0.22074557653946789,
	'G': 0.10051553068573352}