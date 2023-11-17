import pandas as pd
import networkx as nx
phases = {}
graphs = {}
for i in range(1,12): 
  var_name = "phase" + str(i)
  file_name = "https://raw.githubusercontent.com/ragini30/Networks-Homework/main/" + var_name + ".csv"
  phases[i] = pd.read_csv(file_name, index_col = ["players"])
  phases[i].columns = "n" + phases[i].columns
  phases[i].index = phases[i].columns
  phases[i][phases[i] > 0] = 1
  graphs[i] = nx.from_pandas_adjacency(phases[i])
  graphs[i].name = var_name

deg_phase3=nx.eigenvector_centrality(graphs[3])
deg_phase9=nx.eigenvector_centrality(graphs[9])

node_bc_sums = {}

# Calculate the betweenness centrality for each node in each graph and accumulate the values
for G in graphs:
    betweenness_centrality = nx.betweenness_centrality(G)
    for node, bc_value in betweenness_centrality.items():
        if node in node_bc_sums:
            node_bc_sums[node] += bc_value
        else:
            node_bc_sums[node] = bc_value

# Compute the mean betweenness centrality for each node across the 11 graphs
mean_betweenness_centrality = {node: bc_sum / len(graphs) for node, bc_sum in node_bc_sums.items()}

# Sort nodes by their mean betweenness centrality in descending order
sorted_nodes = sorted(mean_betweenness_centrality, key=mean_betweenness_centrality.get, reverse=True)

# Get the top three nodes with the highest mean betweenness centrality
top_three_nodes = sorted_nodes[:3]

# Print the results
for i, node in enumerate(top_three_nodes):
    print(f"Top Node {i + 1}: {node}, Mean Betweenness Centrality: {mean_betweenness_centrality[node]}")





