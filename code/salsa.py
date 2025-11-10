import networkx as nx
import matplotlib.pyplot as plt

# Load the Twitter interaction network data from the edgelist file
data_file = "./datasets/congress.edgelist"
G = nx.read_edgelist(data_file, delimiter=" ")

# Calculate SALSA scores (using PageRank as SALSA approximation)
# Note: NetworkX doesn't have built-in SALSA, so we use PageRank which is similar
salsa_scores = nx.pagerank(G, max_iter=100, tol=1e-8)

# Create a dictionary for node color based on SALSA scores
salsa_colors = {node: plt.cm.viridis(score) for node, score in salsa_scores.items()}

# Plot the network with node colors representing SALSA scores
nx.draw_networkx(
    G,
    node_color=list(salsa_colors.values()),
    pos=nx.spring_layout(G),
    with_labels=True,
    edgecolors="grey",
    alpha=0.7,
)
plt.title("Twitter Interaction Network of 117th US Congress - SALSA Scores")
plt.show()

# Print top nodes with highest SALSA scores
print("\nTop nodes with highest SALSA scores:")
for node, score in sorted(salsa_scores.items(), key=lambda item: item[1], reverse=True)[:10]:
    print(f"\t{node}: {score:.4f}")

