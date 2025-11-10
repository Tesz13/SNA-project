from scipy.stats import pearsonr
import networkx as nx
import pandas as pd

# Define functions for data reading, score calculation, and ranking
def read_data(data_path):
  data = pd.read_csv(data_path, sep=",")
  source_list, target_list = list(data["source"]), list(data["target"])
  return nx.from_edgelist(list(zip(source_list, target_list)))

def calculate_scores(graph, algorithm):
  if algorithm == "HITS":
    hubs, authorities = nx.hits(graph)
    return hubs, authorities
  elif algorithm == "SALSA":
    ranks = nx.pagerank(graph, alpha=0.85)
    return {node: rank for node, rank in ranks.items()}
  else:
    raise ValueError(f"Invalid algorithm: {algorithm}")

def rank_nodes(scores, top_k=10):
  sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)
  return [node for node, _ in sorted_scores][:top_k]

# Read the data (expects a 'congress.edgelist' file under datasets/)
# If it's a CSV with source/target columns, use read_data()
# If it's an edgelist file, use nx.read_edgelist() directly
try:
    congress_graph = read_data("./datasets/congress.edgelist")
except:
    # If read_data fails, try reading as edgelist file
    congress_graph = nx.read_edgelist("./datasets/congress.edgelist", delimiter=" ")

# Calculate HITS scores
hits_hubs, hits_authorities = calculate_scores(congress_graph, "HITS")

# Calculate SALSA scores (PageRank returns a single dict, use same for hubs and authorities)
salsa_scores = calculate_scores(congress_graph, "SALSA")
salsa_hubs = salsa_scores
salsa_authorities = salsa_scores.copy()  # Use same scores for both

# Filter SALSA scores for nodes present in both algorithms
common_nodes = set(hits_hubs.keys()) & set(salsa_hubs.keys())
salsa_hubs = {node: score for node, score in salsa_hubs.items() if node in common_nodes}
salsa_authorities = {node: score for node, score in salsa_authorities.items() if node in common_nodes}

# Calculate Pearson's correlation coefficients
hub_correlation, hub_p_value = pearsonr(list(hits_hubs.values()), list(salsa_hubs.values()))
authority_correlation, authority_p_value = pearsonr(list(hits_authorities.values()), list(salsa_authorities.values()))

# Print results
print("**HITS vs. SALSA:**")
print(f"- Hubs correlation: {hub_correlation:.4f}, p-value: {hub_p_value:.4f}")
print(f"- Authorities correlation: {authority_correlation:.4f}, p-value: {authority_p_value:.4f}")

# (Optional) Perform further analysis based on your specific research questions

