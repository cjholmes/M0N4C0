from collections import deque
import random
import time 

start_time = time.perf_counter()


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
        for j in range(len(currency)): #loops through possible second paths, if it returns to the 0th node then moves to next iteration
            if j == 0:
                current_route = (str(0) + str(i) + str(i) + str(j))
                current_value = adj[0][i]*adj[i][j]
                if current_value > optimal_value:
                    optimal_value = current_value
                    optimal_route = current_route
                continue
            for k in range(len(currency)):
                current_route = (str(0) + str(i) + str(i) + str(j) + str(j) + str(k) + str(k) +str(0))
                current_value = adj[0][i]*adj[i][j]*adj[j][k]*adj[k][0]
                if current_value > optimal_value:
                    optimal_value = current_value
                    optimal_route = current_route
    return optimal_route,optimal_value


def trade_opt_rec(adj):
    def find_optimal_route(current_route,current_value, visited):
        nonlocal optimal_value, optimal_route
        last_node = current_route[-1]
        
        if len(current_route) > 1 and last_node == 0:
            if current_value > optimal_value:
                optimal_value = current_value
                optimal_route = current_route
            return
        
        for next_node in range(len(adj)):
            if next_node not in visited or next_node == 0:
                new_value = current_value * adj[last_node][next_node]
                find_optimal_route(current_route + [next_node], new_value, visited | {next_node})
    
    optimal_value = 0
    optimal_route = []
    
    for start_node in range(1, len(adj)):
        find_optimal_route([0, start_node], adj[0][start_node], {0, start_node})
    
    return ''.join(map(str, optimal_route)), optimal_value
# Main function to run the program

V = len(currency)  # Number of vertices
adj = [[0] * V for i in range(V)]  


for j in range(1,len(currency)):
    for i in range(j,len(currency)):
        add_edge(adj, i, i-j, 1 + i)
# Add edges to the graph



# Display adjacency matrix
print("Adjacency Matrix:")
display_matrix(adj)
print(trade_opt_rec(adj))
print((time.perf_counter() - start_time))

