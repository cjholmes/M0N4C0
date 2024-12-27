from collections import deque
import random


currency = ["a","b","c","d"]
def add_edge(mat, i : float, j : float, weight : float):
  
    # Add an edge between two vertices
    mat[i][j] = weight  # Graph is 
    mat[j][i] = weight**(-1)  #directed

def display_matrix(mat):
  
    # Display the adjacency matrix
    for row in mat:
        print(" ".join(map(str, row)))  

def trade_opt(adj, s):
    return

# Main function to run the program

V = len(currency)  # Number of vertices
adj = [[0] * V for i in range(V)]  

for i in range(1,len(currency)):
    add_edge(adj, i, i-1, random.random())
# Add edges to the graph



# Display adjacency matrix
print("Adjacency Matrix:")
display_matrix(adj)
for i in range(1,len(currency)):
    print(adj[i][i-1]*adj[i-1][i])
