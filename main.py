
currency = [a,b,c,d]
def add_edge(mat, i, j, weight):
  
    # Add an edge between two vertices
    mat[i][j] = weight  # Graph is 
    mat[j][i] = weight**(-1)  #directed

def display_matrix(mat):
  
    # Display the adjacency matrix
    for row in mat:
        print(" ".join(map(str, row)))  

# Main function to run the program

V = 4  # Number of vertices
mat = [[0] * V for _ in range(V)]  

# Add edges to the graph
add_edge(mat, 0, 1,1)
add_edge(mat, 0, 2,1)
add_edge(mat, 1, 2,1)
add_edge(mat, 2, 3,1)


# Display adjacency matrix
print("Adjacency Matrix:")
display_matrix(mat)