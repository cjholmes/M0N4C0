from collections import deque
import random
import time 

start_time = time.time()


currency = ["a","b","c","d"]
def add_edge(mat, i : float, j : float, weight : float):
  
    # Add an edge between two vertices
    mat[i][j] = weight  # Graph is 
    mat[j][i] = weight**(-1)  #directed

def display_matrix(mat):
  
    # Display the adjacency matrix
    for row in mat:
        print(" ".join(map(str, row)))  

def trade_opt(adj):
    optimal_value = 0
    optimal_route = 0
    current_value = 0
    current_route = 0
    for i in range(1,len(currency)):
        for j in range(len(currency)):
            for k in range(len(currency)):
                if j == 0:
                    current_route = (str(0) + str(i) + str(i) + str(j))
                    current_value = adj[0][i]*adj[i][j]
                elif k == 0:
                    current_route = (str(0) + str(i) + str(i) + str(j) + str(j) + str(k))
                    current_value = adj[0][i]*adj[i][j]*adj[j][k]
                else:
                    current_route = (str(0) + str(i) + str(i) + str(j) + str(j) + str(k) + str(k) +str(0))
                    current_value = adj[0][i]*adj[i][j]*adj[j][k]*adj[k][0]
                if current_value > optimal_value:
                    optimal_value = current_value
                    optimal_route = current_route
    return optimal_route,optimal_value

# Main function to run the program

V = len(currency)  # Number of vertices
adj = [[0] * V for i in range(V)]  


for j in range(1,len(currency)):
    for i in range(j,len(currency)):
        add_edge(adj, i, i-j, random.random())
# Add edges to the graph



# Display adjacency matrix
print("Adjacency Matrix:")
display_matrix(adj)
print(trade_opt(adj))
print("--- %s seconds ---" % (time.time() - start_time))

