import networkx as nx
import matplotlib.pyplot as plt

# Load the Twitter interaction network data from the edgelist file
data_file = "./datasets/congress.edgelist"
G = nx.read_edgelist(data_file, delimiter=" ")

# Define functions for HITS scores
def hubs_scores(G):
    hubs, authorities = nx.hits(G, max_iter=100)
    return hubs

def authorities_scores(G):
    hubs, authorities = nx.hits(G, max_iter=100)
    return authorities

# Calculate hub and authority scores
hub_scores = hubs_scores(G)
authority_scores = authorities_scores(G)

# Create a dictionary for node color based on hub scores
hub_colors = {node: plt.cm.Reds(score) for node, score in hub_scores.items()}

# Plot the network with node colors representing hub scores
nx.draw_networkx(
    G,
    node_color=list(hub_colors.values()),
    pos=nx.spring_layout(G),
    with_labels=True,
    edgecolors="grey",
    alpha=0.7,
)
plt.title("Twitter Interaction Network of 117th US Congress - Hub Scores (HITS)")
plt.show()

# Repeat the process for authority scores
authority_colors = {node: plt.cm.Blues(score) for node, score in authority_scores.items()}

nx.draw_networkx(
    G,
    node_color=list(authority_colors.values()),
    pos=nx.spring_layout(G),
    with_labels=True,
    edgecolors="grey",
    alpha=0.7,
)
plt.title("Twitter Interaction Network of 117th US Congress - Authority Scores (HITS)")
plt.show()

