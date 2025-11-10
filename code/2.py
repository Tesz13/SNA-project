import pandas as pd
from networkx import Graph
from collections import defaultdict
import networkx as nx

# Specify the file path and potentially adjust the encoding based on your file format
# (e.g., "ISO-8859-1" for Windows-1252 encoded CSV)
data_path = "./datasets/lastfm_asia_edges.csv"
data_encoding = None  # Use None for default UTF-8 or specify actual encoding if needed

# Read the data from the CSV file
data = pd.read_csv(data_path, encoding=data_encoding)

# Create nodes and edges from the data
nodes = list(data["source"].unique())
edges = list(zip(data["source"], data["target"]))

# Initialize the networkx graph
lastfm_graph = Graph()

# Add nodes and edges to the graph
lastfm_graph.add_nodes_from(nodes)
lastfm_graph.add_edges_from(edges)

# Define the Girvan-Newman community detection function
def girvan_newman(graph):
  """
  Implements the Girvan-Newman community detection algorithm.

  Args:
    graph: A networkx graph object representing the social network.

  Returns:
    communities: A dictionary mapping nodes to their assigned communities.
  """

  communities = defaultdict(lambda: -1)  # Initialize community assignments with -1 as placeholder
  edges = list(graph.edges())  # Create a list of all edges for iteration

  while edges:  # Loop until all edges are removed
    # Calculate edge betweenness centrality
    betweenness = nx.edge_betweenness_centrality(graph)

    # Find the edge with highest betweenness centrality
    max_bw_edge = max(edges, key=lambda edge: betweenness[edge])

    # Remove the edge
    graph.remove_edge(*max_bw_edge)
    edges.remove(max_bw_edge)

    # Update community assignments for affected nodes
    for node in max_bw_edge:
      if communities[node] != -1:  # Check if node belongs to a community
        community_id = communities[node]  # Store its current community ID
        for neighbor in graph.neighbors(node):  # Iterate through its neighbors
          if communities[neighbor] == community_id:  # Check if neighbor belongs to the same community
            communities[neighbor] = len(communities)  # Assign the neighbor to a new community if required

  return communities

# Run the Girvan-Newman algorithm on the networkx graph
communities = girvan_newman(lastfm_graph)

# Analyze and visualize the detected communities based on your specific needs (e.g., size distribution, connectivity)

# (Optional) Add further code for community analysis or visualization

