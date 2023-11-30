# Melody Jing
# Get a minimum spanning tree of a graph using Prim's algorithm.

import math

class Vertex():
    """Stores Vertex characteristics."""
    def __init__(self, index):
        self.name = index
        self.key = math.inf
        self.pi = None
        self.adjList = []
    def getKey(self):
        return self.key
    def setKey(self, newKey):
        self.key = newKey
    def getAdj(self):
        return self.adjList
    def setAdj(self, newList):
        self.adjList = newList
    def getName(self):
        return self.name
    def getPi(self):
        return self.pi
    def setPi(self, newPi):
        self.pi = newPi


def PrimMST(G):
    """Input an adjacency matrix and generate a minimum-spanning tree.
       Print the edges in the MST and their weights."""
    V, E = [], []
    
    # Initialize vertices
    for i in range(len(G)):
        u = Vertex(i) # Create vertices
        V.append(u) # Add Vertex objects to vertex list
        
        # Create adjacency list
        adjList = []
        for j, w in enumerate(G[i]):
            if w: # Include in adjacency list if there is an edge between them
                adjList.append(j) # Add indixces to adjacency lists
        u.setAdj(adjList) # Set in Vertex object
    
    V[0].setKey(0) # Set starting vertex
    unvisited = list(V) # Shallow copy of list of Vertex objects
    while unvisited: # Loop until all vertices are visited

        # Extract minimum key vertex
        currentMin, m = math.inf, None
        for j in unvisited: # Check every unvisited vertex
            if j.getKey() <= currentMin: 
                currentMin, m = j.getKey(), j # Update current minimum
        unvisited.remove(m) # Remove visited vertex from unvisited list
    
        # Check all neighbors
        for k in m.getAdj(): # Loop through each neighbor
            if k in [v.getName() for v in unvisited]: # Check if unvisited
                if G[m.getName()][k] < V[k].getKey(): # Check if more optimal
                    V[k].setKey(G[m.getName()][k]) # Update Vertex key
                    V[k].setPi(m) # Update Vertex previous node
    
    # Compile edges
    for v in V: # Check each vertex
        if v.getPi() is not None: # Exclude starting node
            E.append([(v.getPi().getName(), v.getName()), G[v.getPi().getName()][v.getName()]])
    
    # Print
    print("Edge \tWeight") # Print header
    minWeight = 0
    for edge in E: # Loop through each edge
        print(edge[0], "\t", edge[1]) # Print edge and weight
        minWeight += edge[1] # Add onto total weight
    print("MST weight:", minWeight) # Print total weight
