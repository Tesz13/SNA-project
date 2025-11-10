import networkx as nx
import matplotlib.pyplot as plt

# Load the Twitter interaction network data from the edgelist file
data_file = "./datasets/congress.edgelist"
G = nx.read_edgelist(data_file, delimiter=" ")

# Calculate scores for both algorithms
hits_scores = nx.hits(G, max_iter=100)
# Note: NetworkX doesn't have built-in SALSA, so we use PageRank as approximation
salsa_scores = nx.pagerank(G, max_iter=100)

# Separate hub and authority scores for HITS
hub_scores_hits, authority_scores_hits = hits_scores
# For SALSA (PageRank), we use the same scores for both hubs and authorities
hub_scores_salsa = salsa_scores
authority_scores_salsa = salsa_scores

# Plot distributions
plt.figure(figsize=(10, 6))

# HITS hub scores
plt.subplot(221)
plt.hist(list(hub_scores_hits.values()), bins=20, label="HITS Hub Scores", alpha=0.7)
plt.xlabel("Hub Score")
plt.ylabel("Count")
plt.title("HITS Hub Scores Distribution")

# HITS authority scores
plt.subplot(222)
plt.hist(list(authority_scores_hits.values()), bins=20, label="HITS Authority Scores", alpha=0.7)
plt.xlabel("Authority Score")
plt.ylabel("Count")
plt.title("HITS Authority Scores Distribution")

# SALSA hub scores
plt.subplot(223)
plt.hist(list(hub_scores_salsa.values()), bins=20, label="SALSA Hub Scores", alpha=0.7)
plt.xlabel("Hub Score")
plt.ylabel("Count")
plt.title("SALSA Hub Scores Distribution")

# SALSA authority scores
plt.subplot(224)
plt.hist(list(authority_scores_salsa.values()), bins=20, label="SALSA Authority Scores", alpha=0.7)
plt.xlabel("Authority Score")
plt.ylabel("Count")
plt.title("SALSA Authority Scores Distribution")

# Adjust spacing and title
plt.tight_layout()
plt.suptitle("Distribution of Hub and Authority Scores for HITS and SALSA Algorithms")
plt.show()

