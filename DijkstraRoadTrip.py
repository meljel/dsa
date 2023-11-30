# Melody Jing
# A modified implementation of Dijkstra's algorithm suited for a roadtrip 
# example: how many days will it take to travel from S to T given some 
# mileage limit for each day?

import math
from RandomGraph import randGeoGraph

class Vertex():
    def __init__(self, coords):
        self.coords = coords
        self.days = math.inf
        self.distSince = math.inf
    def setDays(self, days):
        self.days = days
    def getDays(self):
        return self.days
    def setDistSince(self, distSince):
        self.distSince = distSince
    def getDistSince(self):
        return self.distSince


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

            # print(corrEdgeInd)
            if wCoords:
                # corrWghtInd = wCoords.index(j)
                # print('w ', str(edgeInd))
                wObjects[i].append(wCoords[vCoords[ind]][edgeInd])

    if wCoords:
        return vObjects, eObjects, wObjects
    
    return vObjects, eObjects


def roadtrip(S, T, D):
    """
    Parameters
    ----------
    S : int
        Starting vertex index.
    T : int
        Ending vertex index.
    D : int
        Maximum distance allowed per day, >13.

    Returns
    -------
    None.

    """
    # Create graph
    vCoords, eCoords, wCoords = randGeoGraph(50, 50, 50, 13, True)
    
    # Convert coordinate lists into lists using vertex objects
    vObjects, eObjects, wObjects = coordsIntoObjects(vCoords, eCoords, wCoords)
    
    s = vObjects[S]
    dijkstra(vObjects, eObjects, wObjects, D, s)

    totalDays = vObjects[T].getDays()
    print("The total days to travel is", str(totalDays))

if __name__ == "__main__":
    roadtrip(1, 4, 14)