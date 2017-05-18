# !/usr/bin/python
# -*- coding: utf-8 -*-
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


def dijsktra(graph, start_node):
    visited = {start_node: 0}
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

    return visited, path

    #final_node -> FINAL_DESTINATION in settings


def shortest_path(graph, start_node, final_node):
    visited, path = dijsktra(graph, start_node)
    complete_path = deque()
    destination = path[final_node]
    while destination != start_node:
        complete_path.appendleft(destination)
        destination = path[destination]

    complete_path.appendleft(start_node)
    complete_path.append(final_node)

    return visited[final_node], list(complete_path)


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
print shortest_path(graph, 'A', 'D')
print shortest_path(graph, 'A', 'B')
print shortest_path(graph, 'B', 'G')



class Logger(object):
    """Utils Logging has 4 variables that controls if the log goes to the output(screen)
    _error, _debug, _warning and _info default:  all loggers are enable except debug, which is False
    to enable debug log just add the following lines to your code
    from utils import Logger
    log = Logger(debug=True)
    log.info("Information message")
    """
    def __init__(self, debug=False, info=True, error=True, warning=True):
        self._error = error
        self._debug = debug
        self._warning = warning
        self._info = info

    def error(self, msg):
        if self._error:
            print("[ERROR]: {}".format(msg))

    def debug(self, msg):
        if self._debug:
            print("[DEBUG]: {}".format(msg))

    def info(self, msg):
        if self._info:
            print("[INFO]: {}".format(msg))

    def warning(self, msg):
        if self._warning:
print("[WARNING]: {}".format(msg))
