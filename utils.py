# !/usr/bin/python
# -*- coding: utf-8 -*-
#from classes import *
from Maps import *
from settings import *

from collections import defaultdict, deque
    #graph and djisktra algorithm
    #defaultdict in contrast will simply create any items that you try to access
    #deque appends and pops on either end


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list) #returns a new empty list
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def  add_edge(self, node_from, final_node, distance):
       self.edges[node_from].append(final_node)
       self.edges[final_node].append(node_from)
       self.distances[(node_from, final_node)] = distance

g = Graph()
#GRAPH FOR CARS
for lines in range(len(NodeMap)):
    for columns in range(len(NodeMap[0])):
        if NodeMap[lines][columns] not in g.nodes:
            g.add_node(NodeMap[lines][columns])
            #print "added {}".format(NodeMap[lines][columns])
        for node in NodeMap[lines][columns]._adjacentNodes:
            if node not in g.nodes:
                g.add_node(node)
            g.add_edge(NodeMap[lines][columns],node, node._carHeuristic)

CAR_GRAPH = g

gp = Graph()
for lines in range(len(NodeMap)):
    for columns in range(len(NodeMap[0])):
        if  NodeMap[lines][columns]._type != WALL:
            if NodeMap[lines][columns] not in gp.nodes:
                gp.add_node(NodeMap[lines][columns])
            #for i in range(max(NodeMap[lines][columns]._position))
            if ((lines - 1) >= 0 and (NodeMap[lines - 1][columns] not in gp.nodes) and (NodeMap[lines-1][columns]._type != WALL)):
                gp.add_node(NodeMap[lines - 1][columns])
                gp.add_edge(NodeMap[lines][columns], NodeMap[lines-1][columns] , NodeMap[lines-1][columns]._pedestrianHeuristic)
            if ((lines + 1) < 20 and (NodeMap[lines + 1][columns] not in gp.nodes) and (NodeMap[lines+1][columns]._type != WALL)):
                gp.add_node(NodeMap[lines + 1][columns])
                gp.add_edge(NodeMap[lines][columns], NodeMap[lines + 1][columns], NodeMap[lines + 1][columns]._pedestrianHeuristic)
            if (columns - 1) >= 0 and (NodeMap[lines][columns - 1] not in gp.nodes and (NodeMap[lines][columns-1]._type != WALL)):
                gp.add_node(NodeMap[lines][columns - 1])
                gp.add_edge(NodeMap[lines][columns], NodeMap[lines][columns - 1], NodeMap[lines][columns - 1]._pedestrianHeuristic)
            if (columns + 1) < 40 and (NodeMap[lines][columns + 1] not in gp.nodes and (NodeMap[lines][columns+1]._type != WALL)):
                gp.add_node(NodeMap[lines][columns + 1])
                gp.add_edge(NodeMap[lines][columns], NodeMap[lines][columns + 1], NodeMap[lines][columns + 1]._pedestrianHeuristic)

PERSON_GRAPH = gp

# class Logger(object):
    # """Utils Logging has 4 variables that controls if the log goes to the output(screen)
    # _error, _debug, _warning and _info default:  all loggers are enable except debug, which is False
    # to enable debug log just add the following lines to your code
    # from utils import Logger
    # log = Logger(debug=True)
    # log.info("Information message")
    # """
    # def __init__(self, debug=False, info=True, error=True, warning=True):
        # self._error = error
        # self._debug = debug
        # self._warning = warning
        # self._info = info

    # def error(self, msg):
        # if self._error:
            # print("[ERROR]: {}".format(msg))

    # def debug(self, msg):
        # if self._debug:
            # print("[DEBUG]: {}".format(msg))

    # def info(self, msg):
        # if self._info:
            # print("[INFO]: {}".format(msg))

    # def warning(self, msg):
        # if self._warning:
            # print("[WARNING]: {}".format(msg))





def dijsktra(graph, start_node):
    print "1 - disjktra"
    visited = {start_node: 0}
    print "2 - disjktra"
    path = {}
    nodes = set(graph.nodes)
    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break
        nodes.remove(min_node)
        current_weight = visited[min_node]
        for edge in graph.edges[min_node]:
            try:
                weight = current_weight + graph.distances[(min_node, edge)]
            except:
                continue
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node
    print "thefucking path {}".format(path.values())
    return visited, path

    #final_node -> FINAL_DESTINATION in settings


def shortest_path(graph, start_node, final_node):
    print 1
    visited, path = dijsktra(graph, start_node)
    print 2
    complete_path = deque()
    print "here comes the complete path {}".format(complete_path)
    print "here comes the path {}".format(path.values())
    print "here comes the path {}".format(path.keys())
    _destination = path[final_node]
    #_destination._position
    while _destination != start_node:
        complete_path.appendleft(_destination)
        print 4
        _destination = path[_destination]
        print 6
    print 7
    complete_path.appendleft(start_node)
    print 8
    complete_path.append(final_node)
    print 9
    positions = []
    for i in complete_path:
        print "I'm scared {}".format(i._position)
    return complete_path


#Auxiliary
def turnLeft(orientation):
    """turns the car to the left acording to his perspective, assume a birdseye view!
        effectively [x,y] becomes [-y,x]
    """
    if orientation not in ACCEPTABLE_ORIENTATIONS:
        raise OrientationError("I am a person and my orientation \"{}\" seems to be a bit wonky!".format(self.current_orientation))
    else:
        return [  - self.current_orientation [1] , self.current_orientation[0] ]
        
    
def turnRight(orientation):
    """turns the car to the right acording to his perspective, assume a birdseye view!
        effectively [x,y] becomes [y,-x]
    """
    if orientation not in ACCEPTABLE_ORIENTATIONS:
        raise OrientationError("I am a car and my orientation \"{}\" seems to be a bit wonky!".format(self.current_orientation))
    else:
        return [ self.current_orientation [1] ,  - self.current_orientation[0] ]
        
def determineNewOr(orientation,turn_signal_status):
    if turn_signal_status == TURN_SIG_OFF:
        return orientation
    elif turn_signal_status == TURN_SIG_LEFT:
        return turnLeft(orientation)
    elif turn_signal_status == TURN_SIG_RIGHT:
        return turnRight(orientation)

def lookForTurns(plan,orientation,turn_signal_status,map=NodeMap):
    """plan is a list with 4 elements, they are the nodes the car might turn in 
       the next cycle, this function returns the new plan, updated with more accurate information
    """
    new_plan = [plan[0]]
    new_orientation = determineNewOr(orientation,turn_signal_status)
    for n in plan[1:]:
        adjacentNodes = n._adjacentNodes
        pos_possible_node = [n._position[0] + new_orientation[0],[n._position[1] + new_orientation[1]]]
        for nod_adj in adjacentNodes:
            if nod_adj == pos_possible_node:
                new_plan += [n,nod_adj]
                break
    if len(new_plan) == 1:
        #This should never happen
        print "This shouldn't happen! Turn signal was off but I could not find an adjacent node with the correct description!"
    return new_plan

    
#testcode

graph = Graph()
for node in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
    graph.add_node(node)

graph.add_edge('A', 'B', 10)
graph.add_edge('A', 'C', 20)
graph.add_edge('B', 'D', 15)
graph.add_edge('C', 'D', 30)
graph.add_edge('B', 'E', 50)
graph.add_edge('D', 'E', 30)
graph.add_edge('E', 'F', 5)
graph.add_edge('F', 'G', 2)
    #def possiblePosition(new_pos):
    #	if new_pos not in Map:
    #		return False
    #	else:
    # #return True
# print shortest_path(graph, 'A', 'D')
#print shortest_path(graph, 'A', 'B')
#print shortest_path(graph, 'B', 'G')


########################################djisktra with matrixes we'll see#############
# def dijkstra_matrix():
#     #k = int(input("Enter the source vertex"))
#     k = ar.getCurrentNode()
#     matrix = NodeMap
#     m = len(matrix)
#     n = len(matrix[0])
#     cost = [[0 for x in range(m)] for x in range(1)]
#     offsets = []
#     offsets.append(k)
#     elepos = 0
#
#
#     for j in range(m):
#         cost[0][j] = matrix[k][j]
#     mini = 999
#     for x in range(m - 1):
#         mini = 999
#         for j in range(m):
#             if cost[0][j] <= mini and j not in offsets:
#                 mini = cost[0][j]
#                 elepos = j
#         offsets.append(elepos)
#         for j in range(m):
#             if cost[0][j] > cost[0][elepos] + matrix[elepos][j]:
#                 cost[0][j] = cost[0][elepos] + matrix[elepos][j]
#     print("The shortest path", offsets)
#     print("The cost to various vertices in order", cost)


#def main():
    #print("Dijkstras algorithum graph using matrix representation \n")
    #n = int(input("number of elements in row"))
    #m = int(input("number of elements in column"))
    # print("enter the values of the matrix")
    #matrix = [[0 for x in range(m)] for x in range(n)]
    #matrix = NodeMap
    #for i in range(n):
        #for j in range(m):

            #matrix[i][j] = int(input("enter the values of the matrix"))
    #print(matrix)
    #dijkstra_matrix()


#main()




