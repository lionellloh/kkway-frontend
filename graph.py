# graph object definition
# generate_route function

import heapq
import sys

class Graph:

    def __init__(self, vertices={}):
        self.vertices = vertices

    def add_vertex(self, name, edges):
        self.vertices[name] = edges

    def shortest_path(self, start, finish):
        distances = {}  # Distance from start to node
        previous = {}  # Previous node in optimal path from source
        nodes = []  # Priority queue of all nodes in Graph

        for vertex in self.vertices:
            if vertex == start:  # Set root node as distance of 0
                distances[vertex] = 0
                heapq.heappush(nodes, [0, vertex])
            else:
                distances[vertex] = sys.maxsize
                heapq.heappush(nodes, [sys.maxsize, vertex])
            previous[vertex] = None

        while nodes:
            # Vertex in nodes with smallest distance in distances
            smallest = heapq.heappop(nodes)[1]
            if smallest == finish:  # If the closest node is our target we're done so print the path
                path = []
                # Traverse through nodes til we reach the root which is 0
                while previous[smallest]:
                    path.append(smallest)
                    smallest = previous[smallest]
                path.append(start)
                path.reverse()
                return path
            # All remaining vertices are inaccessible from source
            if distances[smallest] == sys.maxsize:
                break

            # Look at all the nodes that this vertex is attached to
            for neighbor in self.vertices[smallest]:
                # Alternative path distance
                alt = distances[smallest] + self.vertices[smallest][neighbor]
                # If there is a new shortest path update our priority queue (relax)
                if alt < distances[neighbor]:
                    distances[neighbor] = alt
                    previous[neighbor] = smallest
                    for n in nodes:
                        if n[1] == neighbor:
                            n[0] = alt
                            break
                    heapq.heapify(nodes)
        return distances

    def __str__(self):
        return str(self.vertices)

# def simplify_nodes(nodes):
#     '''
#     to aviod intermediate nodes
#     e.g.
    
#     '''
#     temp = None
#     out_nodes = []
#     for n in nodes:
#         if len(n) == temp:
#             pass
#         # for corner case, len('1.2corner4')=10
#         elif len(n) == 10:
#             out_nodes.append(n)
#             temp = 10
#         # for elevator case, len('1.2elevator')=11
#         elif len(n) == 11:
#             out_nodes.append(n)
#             temp = 11
#         # for clsroom case, len('1.204')=5
#         else:
#             out_nodes.append(n)
#             temp = 5
#     return out_nodes

def generate_route(nodes):
    """
    @input: list of nodes, ['1.206', '1.205', '1.203', '1.2corner1', '1.201', '1.2elevator', '1.3elevator', '1.4elevator'] 
    @output: string of guide generated based on nodes
    """
    # assume we dont start from a corner here
    out_s = "Starting from " + nodes[0] + " and go straight to "
    i = 1
    # from element 0 to n-1
    while i<len(nodes)-1:
        out_s += nodes[i] + ', '

        # current node is elevator
        if "elevator" in nodes[i]:
            if "corner" in nodes[i+1]: # 1. next node is corner:
                if nodes[i+1][0] == '1': # A. building 1
                    if nodes[i-1][0] == nodes[i][0]:
                        out_s += "exit lift then turn right and reach "
                    else:
                        out_s += "go straight and reach "
                elif nodes[i+1][0] == '2': # B. building 2
                    if nodes[i-1][0] == nodes[i][0]:
                        out_s += "exit lift then turn left and reach "
                    else:
                        out_s += "go straight and reach "
            elif "elevator" in nodes[i+1]: # 2. next node is elevator
                if nodes[i][0] != nodes[i+1][0]: # A. the two lift is not on the same building
                    if nodes[i+1][0] == '1': # a. building2 lift to buidling1 lift
                        out_s += "exit lift and turn right and reach "
                    if nodes[i+1][0] == '2': # b. building1 lift to building2 lift
                        out_s += "exit lift and turn left and reach "
                elif nodes[i][0] == nodes[i+1][0]: # B. take the lift to a different store in the same building
                    while "elevator" in nodes[i+1]:
                        i += 1
                    if int(nodes[i][2]) > int(nodes[i-1][2]):
                        out_s += "enter the lift and going up to " # a. going up
                    else:
                        out_s += "enter the lift and going down to " # b. going down
                    i -= 1 # we add this 1 later on
        
        # current node is corner
        elif "corner" in nodes[i]:
            if "corner1" in nodes[i]: # for corner1
                if "elevator" in nodes[i-1]:
                    if '01' in nodes[i+1]:
                        out_s += "turn right and reach "
                    elif '12' in nodes[i+1]:
                        out_s += "turn left and reach "
                    elif '13' in nodes[i+1]:
                        out_s += "go straight and reach "
                if "01" in nodes[i-1]:
                    if 'elevator' in nodes[i+1]:
                        out_s += "turn left and reach "
                    elif '12' in nodes[i+1]:
                        out_s += "go straight and reach "
                    elif '13' in nodes[i+1]:
                        out_s += "turn right and reach "
                if "13" in nodes[i-1]:
                    if '01' in nodes[i+1]:
                        out_s += "turn left and reach "
                    if 'elevator' in nodes[i+1]:
                        out_s += "go straight and reach "
                    if '12' in nodes[i+1]:
                        out_s += "turn right and reach "
                if "12" in nodes[i+1]:
                    if '01' in nodes[i+1]:
                        out_s += "go straight and reach "
                    if 'elevator' in nodes[i+1]:
                        out_s += "turn right and reach "
                    if '13' in nodes[i+1]:
                        out_s += "turn left and reach "
            elif "corner4" in nodes[i]: # for corner2
                if "07" in nodes[i-1]:
                    if '13' in nodes[i+1]:
                        out_s += "turn left and reach "
                    if '09' in nodes[i+1]:
                        out_s += "go straight and reach "
                if "13" in nodes[i-1]:
                    if '17' in nodes[i+1]:
                        out_s += "turn right and reach "
                    if '09' in nodes[i+1]:
                        out_s += "turn left and reach "
                if "09" in nodes[i-1]:
                    if '13' in nodes[i+1]:
                        out_s += "turn right and reach "
                    if '07' in nodes[i+1]:
                        out_s += "go straight and reach "
            else: # 3. other nodes
                if int(nodes[i+1][3:]) > int(nodes[i-1][3:]):
                    out_s += "turn left and reach"
                else:
                    out_s += "turn right and reach"
        
        # current nodes is clsroom
        elif len(nodes[i]) == 5:
            if 'corner' in nodes[i+1]:
                out_s += "and then reach "
            else:
                out_s += "pass by "
        i += 1
    out_s += nodes[-1]
    out_s += ", You have reached your destination!"
    return [step.strip() for step in out_s.split(",")]