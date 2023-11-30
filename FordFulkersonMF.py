# Melody Jing
# Uses the Ford-Fulkerson algorithm to solve for max flow, with two simple 
# applications: snack-matching and debt-correcting.

import math

class Node():
    def __init__(self, label):
        self.label = label
        self.inEdges = []
        self.outEdges = []

    def getOutEdges(self):
        return self.outEdges
    def getInEdges(self):
        return self.inEdges


class Edge():
    def __init__(self, startNode, endNode, capacity):
        self.startNode = startNode
        self.endNode = endNode
        self.capacity = capacity
        self.flow = 0

    def setFlow(self, newFlow):
        self.flow = newFlow
    def modFlow(self, dFlow):
        self.flow += dFlow
    def getFlow(self):
        return self.flow
    def getEndNode(self):
        return self.endNode
    def getStartNode(self):
        return self.startNode
    def getTotalCapacity(self):
        return self.capacity
    def getPotential(self):
        return self.capacity - self.flow


class Network():
    def __init__(self):
        self.dict = {}
        self.source = Node("S")
        self.dict["S"] = self.source
        self.sink = Node("T")
        self.dict["T"] = self.sink
        self.edges = []
        self.currentMin = math.inf
        
    def add_node(self, label):
        newNode = Node(label)
        self.dict[label] = newNode
    
    def add_edge(self, a, b, c):
        newEdge = Edge(a, b, c)
        self.dict[a].getOutEdges().append(newEdge)
        self.dict[b].getInEdges().append(newEdge)
        self.edges.append(newEdge)
        
    def find_residual(self, current, visited, min_capacity):
        """
        Recursively use DFS to find a single residual path, given a network.

        Parameters
        ----------
        current : str
            Label corresponding to a node that the function starts from.
        visited : list
            List of ALL visited nodes.
        min_capacity : int
            Minimum capacity of all edges in a path.

        Returns
        -------
        list
            List of edges in the current path containing T.
        min_capacity
            Minimum capacity of all edges in a path.

        """
        currentNode, edgeFound = self.dict[current], False
        
        # Get all ingoing and outgoing edges
        neighbors = currentNode.getOutEdges() + currentNode.getInEdges()
        
        # Loop through neighbors
        for edge in neighbors:
            edgeFound = False

            # Check if unvisited node
            if edge.getEndNode() not in visited:
                
                # For outgoing edges
                if edge in currentNode.getOutEdges() and edge.getPotential() > 0:
                    edgeFound = True
                    visited.append(edge.getEndNode())
                    
                    # Update min capacity
                    min_capacity = min(min_capacity, edge.getPotential())
                    newNode = edge.getEndNode()
                    
                    # Check if end node
                    if edge.getEndNode() == "T":
                        return [edge], min_capacity

            # Check if unvisited node
            elif edge.getStartNode() not in visited:
                
                # For returning edges
                if edge.getFlow():
                    edgeFound = True
                    visited.append(edge.getStartNode())
                    min_capacity = min(min_capacity, edge.getFlow())
                    newNode = edge.getStartNode()

            # Recurse if edge is valid
            if edgeFound:
                currentPath, new_min_capacity = self.find_residual(newNode,
                                                                   visited,
                                                                   min_capacity)
                # Build current path
                if currentPath is not None:
                    return [edge] + currentPath, new_min_capacity
        
        # If all adjacent nodes are visited OR if there is only 1 adjacnet node
        return None, math.inf
    
    def solve_network(self):
        """
        Use find_residual recursively to find residual paths until max flow
        is found.

        Returns
        -------
        flow : int
            Maximum flow of a certain network.

        """
        flow = 0
        
        path, min_capacity = self.find_residual("S", ["S"], math.inf)
        while path is not None:

            dFlow = min_capacity
            prevNode = path[0].getStartNode()
            
            for edge in path:
                # Forward edges
                if edge.getStartNode() == prevNode:
                    edge.modFlow(dFlow)
                    prevNode = edge.getEndNode()

                # Backward edges
                else:  # edge.getEndNode() is prevNode:
                    edge.modFlow(-dFlow)
                    prevNode = edge.getStartNode()

            # Calculate flow
            flow = 0
            for edge in self.dict["S"].getOutEdges():
                flow += edge.getFlow()
            
            path, min_capacity = self.find_residual("S", [], math.inf)


        if flow:
            return flow
        else: 
            print("There are no paths from S to T.")


# Application: Matching people with their preferred snacks


def match_snacks():
    N = Network()

    # Nodes of people
    N.add_node("A")
    N.add_node("B")
    N.add_node("C")
    N.add_node("D")
    N.add_node("E")

    # Nodes of snacks
    N.add_node("TM")
    N.add_node("RP")
    N.add_node("S")
    N.add_node("K")
    N.add_node("P")
    N.add_node("CM")
    
    # Edges from source
    N.add_edge("S", "A", 1)
    N.add_edge("S", "B", 1)
    N.add_edge("S", "C", 1)
    N.add_edge("S", "D", 1)
    N.add_edge("S", "E", 1)
    
    # Edges in between
    N.add_edge("A", "TM", 1)
    N.add_edge("A", "RP", 1)
    N.add_edge("B", "S", 1)
    N.add_edge("B", "RP", 1)
    N.add_edge("B", "K", 1)
    N.add_edge("C", "CM", 1)
    N.add_edge("C", "P", 1)
    N.add_edge("C", "S", 1)
    N.add_edge("D", "CM", 1)
    N.add_edge("E", "TM", 1)
    N.add_edge("E", "RP", 1)
    N.add_edge("E", "S", 1)
    N.add_edge("E", "K", 1)
    N.add_edge("E", "P", 1)
    N.add_edge("E", "CM", 1)
    
    N.add_edge("TM", "T", 1)
    N.add_edge("RP", "T", 1)
    N.add_edge("S", "T", 1)
    N.add_edge("K", "T", 1)
    N.add_edge("P", "T", 1)
    N.add_edge("CM", "T", 1)
    
    maxFlow = N.solve_network()
    
    for edge in N.edges[5:20]:
        if edge.getFlow() > 0:
            print(edge.getStartNode(), "receives", edge.getEndNode())


# Application: Minimize transactions to relieve debts within a group of people


def debt_correct():
    N = Network()

    # Nodes
    N.add_node("A")
    N.add_node("B")
    N.add_node("C")
    N.add_node("D")
    
    # Edges from source
    N.add_edge("S", "A", 5)
    N.add_edge("S", "C", 3)
    
    # Edges in between
    N.add_edge("A", "B", 2)
    N.add_edge("A", "C", 3)
    N.add_edge("A", "D", 1)
    N.add_edge("C", "D", 1)
    N.add_edge("C", "B", 2)
    
    # Edges to sink
    N.add_edge("B", "T", 1)
    N.add_edge("C", "T", 2)
    N.add_edge("D", "T", 1)
    
    # Max flow
    maxFlow = N.solve_network()
    
    # No. of transactions
    trs = 0
    for edge in N.edges[2:7]:
        if edge.getFlow() > 0:
            trs += 1
    
    return trs

