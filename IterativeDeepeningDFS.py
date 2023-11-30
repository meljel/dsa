# Melody Jing
# An implementation of Iterative Deepening Depth First Search.

from graphics import *
from DijkstraRoadTrip import Vertex, coordsIntoObjects

def iterativeDeepening(V, E, S, T, LB, UB):
    """
    Binary search with DFS on the distance between two points on a graph.

    Parameters
    ----------
    V : list
        List containing coordinates of each vertex.
    E : dict
        Dictionary with tuple indices and adjacent vertex coordinates. 
    S : int
        Index of the first vertex.
    T : int
        Index of the final vertex.
    LB : int
        Known lower bound of the length.
    UB : int
        Known upper bound of the length.

    Returns
    -------
    int
        Found distance between the specified two vertices.

    """
    # Base case of one possible length
    if UB - LB <= 1:
        return UB
    
    # Finding the midpoint for recursive case
    mid = (UB + LB) // 2 
    found = checkPath(V, E, S, T, mid)
    
    # If length is less than attempted
    if found:
        return iterativeDeepening(V, E, S, T, LB, mid)
    
    # If length is greater than attempted
    return iterativeDeepening(V, E, S, T, mid, UB)


class DFSVertex(Vertex):
    def __init__(self, coords):
        self.color = "white"
        Vertex.__init__(self, coords)
    def getColor(self):
        return self.color
    def setColor(self, newColor):
        self.color = newColor


def checkPath(V, E, S, T, L):
    start, end = V[S], V[T]
    # Convert coordinate format into Vertex format
    vObjects, eObjects = coordsIntoObjects(V, E, cl = DFSVertex)
    
    # Recursive DFS process thing
    found = DFSVisit(vObjects, eObjects, vObjects[S], vObjects[T], L)
    return found


def DFSVisit(V, E, vertex, end, L, step=1):
    """
    DFS Recursive step.

    Parameters
    ----------
    V : list
        List containing each DFSVertex.
    E : dict
        Dictionary with DFSVertex indices and adjacent DFSVertex objects. 
    vertex : Vertex
        Vertex to start/continue DFS.
    end : Vertex
        Vertex to end DFS.
    L : int
        Maximum allowed path length.
    step : int, optional
        Counts the length of the path in progress. The default is 0.

    Returns
    -------
    bool
        Whether the final vertex was found within a possible path.

    """
    # If we go beyond the maximum length, stop
    if step > L:
        return False
            
    # Visited vertices are grey
    vertex.setColor("grey")

    # Get neighbors
    neighbors = E[vertex].copy()

    for newVertex in neighbors:
        if newVertex.getColor() == "white":
            
            # Check if final vertex is reached
            if newVertex is end:
                return True

            # Recurse if not
            found = DFSVisit(V, E, newVertex, end, L, step+1)
            if found:
                return True
            
    # Revert color to white if we have to back out of this branch
    # (different from normal DFS because of the length constraint)
    vertex.setColor("white")
    
    return False
