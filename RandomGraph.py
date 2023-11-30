# Melody Jing
# Create a graph with randomly generated vertex locations, where each pair of 
# vertices is connected iff they are ≤ a certain distance from each other!

import random
from graphics import *
import math

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

if __name__ == "__main__":
    # Provide your own input here! 
    win_width, win_height = 40, 30
    vertices, edges = randGeoGraph(win_width, win_height, 30, 10)
    drawGraph(vertices, edges, win_width, win_height)