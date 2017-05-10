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
			weight = current_weight + graph.distance[(min_node, edge)]
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

	return visited[destination], list(complete_path)

#def possiblePosition(new_pos):
#	if new_pos not in Map:
#		return False
#	else:
#		return True

def didICrash(pos):
	return None  
