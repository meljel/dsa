# Melody Jing
# Lab 09

import random
from graphics import *
import math
import copy


# Exercise 1


def randGeoGraph(A, B, N, D, returnWeights = False):
    """
    Create a geometric graph using the given dimensions, number of vertices.
    and maximum distance between connected points.

    Parameters
    ----------
    A : int
        Width of the window.
    B : int
        Height of the window.
    N : int
        Number of vertices in the graph.
    D : int
        Highest distance between connected vertices.
    returnWeights : bool, optional
        Whether to return a dictionary of edge weights as the third output.

    Returns
    -------
    V : list 
        List of tuples of the coordinates of each vertex.
    E : dictionary
        Dictionary with tuple indices and adjacent vertex coordinates. 
    W : dictionary
        Dictionary with edge weights. 

    """
    V, E, W = [], dict(), dict()

    # Randomly select points
    totalPoints = int(A) * int(B)
    vertNums = random.choices(range(totalPoints), k=N)
    for num in vertNums:
        # Create the name of the vertex
        x = num // int(B)
        y = num - x*int(B)
        tag = (x, y)  

        # Initialize edge entries
        E[tag] = []
        W[tag] = []

        # Find all edges with other vertices
        for vertex in V:
            a, b = (vertex)
            # List criteria: distance between vertices
            weight = math.sqrt((x-a)**2 + (y-b)**2)

            if weight <= D:
                E[tag].append(vertex)
                E[vertex].append(tag)
                # add weight to dict too
                W[vertex].append(weight)
                W[tag].append(weight)

        # Add vertex to list
        V.append(tag)

    if returnWeights:
        return V, E, W

    return V, E


def drawGraph(V, E, A=None, B=None, size=16, margin=30):
    """
    Create a graphics window that displays a graph.

    Parameters
    ----------
    V : list
        List containing coordinates of each vertex.
    E : dict
        Dictionary with tuple indices and adjacent vertex coordinates. 
    A : int, optional
        Custom width of the window. The default is None.
    B : int, optional
        Custom height of the window. The default is None.
    size : int, optional
        Custom scale of the graph. The default is 16.
    margin : int, optional
        Custom distance between displayed contents and edge. The default is 30.

    Returns
    -------
    None.

    """
    # Initialize the graph
    xVals, yVals = [vertex[0] for vertex in V], [vertex[1] for vertex in V]
    if A:
        xVals.append(A)
    if B:
        yVals.append(B)

    x, y = max(xVals), max(yVals)

    # Create graphics window
    win = GraphWin("Graph", size*x + 2*margin, size*y + 2*margin)

    ind = 1
    for vertex in V:
        # Draw vertex
        p1 = Point(margin + size*vertex[0], margin + size*(y-vertex[1]))
        c = Circle(p1, 3)
        c.setFill("black")
        c.draw(win)
        
        # Draw all edges
        for adj in E[vertex]:
            p2 = Point(margin + size*adj[0], margin + size*(y-adj[1]))
            edge = Line(p1, p2)
            edge.draw(win)

    win.getMouse()
    win.close()


# Exercise 2



def dijkstra(V, E, W, d, s):
    """
    Modified Dijkstra's algorithm to work with the road trip problem.

    Parameters
    ----------
    V : list
        List containing each vertex.
    E : dict
        Dictionary with Vertex indices and adjacent Vertex objects. 
    W : dict
        Dictionary with the weights of each of the edges in E; same order.
    d : int
        Maximum distance allowed per day.
    s : Vertex
        Initial (starting) vertex.

    Returns
    -------
    None.

    """
    # Initialize
    s.setDays(0)
    s.setDistSince(0)
    S = set()
    Q = [vObject for vObject in V]
    
    while Q:
        minDays = math.inf
        minVertex = None
        for vertex in Q:
            # Compare existing minimum with new minimum
            if vertex.getDays() < minDays:
                minDays = vertex.getDays()
                minVertex = vertex
        
        # Get the minimum Vertex
        if minVertex:
            u = minVertex
            Q.remove(minVertex)
        else:
            break
        
        # Add to overall set (not used here)
        S = S.union({u})
        ind = 0
        
        # Recurse
        for vertex in E[u]:
            weight = W[u][ind]
            relax(u, vertex, weight, d)
            ind += 1


def relax(u, v, w, d):
    # Check if path is travelable
    if w <= d:
        
        days, distSince = u.getDays(), u.getDistSince()
        # If a hotel stay is needed because the distance since the last
        # hotel exceeds the maximum possible
        if u.getDistSince() + w > d:
            days += 1
            distSince = w

        # no hotel stay is needed
        else:
            distSince += w

        # Compare with any previously found paths
        if v.getDays() > days:
            v.setDays(days)
            v.setDistSince(distSince)
        
        elif v.getDays() == days:
            if v.getDistSince() > distSince:
                v.setDistSince(distSince)


def coordsIntoObjects(vCoords, eCoords, wCoords = None, cl = Vertex):
    # Turn vertex coords list into vertex object list
    vObjects = []
    for coords in vCoords:
        vObjects.append(cl(coords))
    
    # Turn edge coords dictionary into edge vertex object dictionary
    eObjects, wObjects = dict(), dict()
    
    for i in vObjects:  # i is a Vertex
        ind = vObjects.index(i)
        eObjects[i], wObjects[i] = [], []
        
        for edgeInd, j in enumerate(eCoords[vCoords[ind]]):  # j is a V coordinate
            corrEdgeInd = vCoords.index(j)
            eObjects[i].append(vObjects[corrEdgeInd])

            print(corrEdgeInd)
            if wCoords:
                # corrWghtInd = wCoords.index(j)
                print('w ', str(edgeInd))
                wObjects[i].append(wCoords[vCoords[ind]][edgeInd])

    if wCoords:
        return vObjects, eObjects, wObjects
    
    return vObjects, eObjects


def roadtrip(S, T, D):
    
    # Create graph
    vCoords, eCoords, wCoords = randGeoGraph(50, 50, 50, 13, True)
    
    # Convert coordinate lists into lists using vertex objects
    vObjects, eObjects, wObjects = coordsIntoObjects(vCoords, eCoords, wCoords)
    
    s = vObjects[S]
    dijkstra(vObjects, eObjects, wObjects, D, s)

    totalDays = vObjects[T].getDays()
    print("The total days to travel is ", str(totalDays))


# Exercise 4

class Vertex():
    def __init__(self, coords):
        self.coords = coords
    def getCoords(self):
        return self.coords
    def setCoords(self, coords):
        self.coords = coords

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
    print(start)
    print(end)
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
                print(newVertex.coords)
                return True

            # Recurse if not
            found = DFSVisit(V, E, newVertex, end, L, step+1)
            if found:
                print(newVertex.coords)
                return True
            
    # Revert color to white if we have to back out of this branch
    # (different from normal DFS because of the length constraint)
    vertex.setColor("white")
    
    return False


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
