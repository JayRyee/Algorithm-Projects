"""
Name:
CSE 331 SS20 (Onsay)
"""

import heapq, math, itertools
from collections import OrderedDict
import matplotlib.pyplot as plt, matplotlib.patches as patches, matplotlib.cm as cm
import numpy as np
import time
import random
from queue import Queue



class Vertex:
    """
    Class representing a Vertex object within a Graph
    """

    __slots__ = ['id', 'adj', 'visited', 'x', 'y']

    def __init__(self, idx, x=0, y=0):
        """
        DO NOT MODIFY
        Initializes a Vertex
        :param idx: A unique string identifier used for hashing the vertex
        :param x: The x coordinate of this vertex (used in a_star)
        :param y: The y coordinate of this vertex (used in a_star)
        """
        self.id = idx
        self.adj = OrderedDict()  # dictionary {id : weight} of outgoing edges
        self.visited = False      # Boolean flag used in search algorithms
        self.x = x
        self.y = y

    def __eq__(self, other):
        """
        DO NOT MODIFY
        Overloads equality operator for Graph Vertex class
        :param other: vertex to compare
        """
        return (self.id == other.id
                and self.adj == other.adj
                and self.visited == other.visited
                and self.x == other.x
                and self.y == other.y)

    def __repr__(self):
        """
        DO NOT MODIFY
        Represents Vertex as string
        :return: string representing Vertex object
        """
        lst = [f"<id: '{k}', weight: {v}>" for k, v in self.adj.items()]

        return f"<id: '{self.id}'" + ", Adjacencies: " + "".join(lst) + ">"

    def __str__(self):
        """
        DO NOT MODIFY
        Represents Vertex as string
        :return: string representing Vertex object
        """
        return repr(self)

    def __hash__(self):
        """
        DO NOT MODIFY
        Hashes Vertex into a set; used in unit tests
        :return: hash value of Vertex
        """
        return hash(self.id)

    def degree(self):
        """
        Returns Degree of the vertex
        param: self
        return: Degree of the vertex
        """
        degree = len(self.adj)
        return degree

    def visit(self):
        """
        Sets visited flag
        param: self
        """
        self.visited = True

    def reset(self):
        """
        Resets visited flag
        param: self
        """
        self.visited = False

    def get_edges(self):
        """
        Creates list of tuples representing edges of the Vertex
        param: self
        return: list of tuples
        """

        my_list = []

        adj_dict = self.adj
        for adj_vert, weight in adj_dict.items():
            my_list.append((adj_vert, weight))

        return my_list

    def euclidean_distance(self, other):
        """
        Finds Euclidian distance between two vertices
        param: self
        param: other the adj vertex
        returns: distance
        """
        x1 = self.x
        y1 = self.y

        x2 = other.x
        y2 = other.y

        d1 = math.pow(x2-x1, 2)
        d2 = math.pow(y2-y1, 2)

        d = math.sqrt(d1+d2)
        return d


class Graph:
    """
    Class implementing the Graph ADT using an Adjacency Map structure
    """

    __slots__ = ['size', 'vertices', 'plot_show', 'plot_delay']

    def __init__(self, plt_show=False):
        """
        DO NOT MODIFY
        Instantiates a Graph class instance
        :param: plt_show : if true, render plot when plot() is called; else, ignore calls to plot()
        """
        self.size = 0
        self.vertices = OrderedDict()
        self.plot_show = plt_show
        self.plot_delay = 0.2

    def __eq__(self, other):
        """
        DO NOT MODIFY
        Overloads equality operator for Graph class
        :param other: graph to compare
        """
        return self.vertices == other.vertices and self.size == other.size

    def __repr__(self):
        """
        DO NOT MODIFY
        :return: String representation of graph for debugging
        """
        return "Size: " + str(self.size) + ", Vertices: " + str(list(self.vertices.items()))

    def __str__(self):
        """
        DO NOT MODFIY
        :return: String representation of graph for debugging
        """
        return repr(self)

    def plot(self):
        """
        Modify if you'd like - use for debugging!
        :return: Plot a visual representation of the graph using matplotlib
        """
        if self.plot_show:
            # seed random generator to reproduce random placements if no x,y specified
            random.seed(2020)

            # show edges
            max_weight = max([edge[2] for edge in self.get_edges()])
            colormap = cm.get_cmap('cool')
            for edge in self.get_edges():
                origin = self.get_vertex(edge[0])
                destination = self.get_vertex(edge[1])
                weight = edge[2]

                # if no x, y coords are specified, randomly place in (0,1)x(0,1)
                if not origin.x and not origin.y:
                    origin.x, origin.y = random.random(), random.random()
                if not destination.x and not destination.y:
                    destination.x, destination.y = random.random(), random.random()

                # plot edge
                arrow = patches.FancyArrowPatch((origin.x, origin.y), (destination.x, destination.y),
                                                connectionstyle="arc3,rad=.2", color=colormap(weight / max_weight),
                                                zorder=0,
                                                **dict(arrowstyle="Simple,tail_width=0.5,head_width=8,head_length=8"))
                plt.gca().add_patch(arrow)

                # label edge
                plt.text((origin.x + destination.x) / 2 - (origin.x - destination.x) / 10,
                         (origin.y + destination.y) / 2 - (origin.y - destination.y) / 10,
                         weight, color=colormap(weight / max_weight))

            # show vertices
            x = np.array([vertex.x for vertex in self.get_vertices()])
            y = np.array([vertex.y for vertex in self.get_vertices()])
            labels = np.array([vertex.id for vertex in self.get_vertices()])
            colors = np.array(['yellow' if vertex.visited else 'black' for vertex in self.get_vertices()])
            plt.scatter(x, y, s=40, c=colors, zorder=1)

            # plot labels
            for i in range(len(x)):
                plt.text(x[i] - 0.03 * max(x), y[i] - 0.03 * max(y), labels[i])

            # show plot
            plt.show()
            # delay execution to enable animation
            time.sleep(self.plot_delay)

    def reset_vertices(self):
        """
        Resets all vertices visited flags
        param: self
        """

        for v in self.vertices.values():
            v.visited = False

    def get_vertex(self, vertex_id):
        """
        Gets vertex at given id
        param: self
        param: vertex_id
        return: vertex if found
        """
        if vertex_id in self.vertices.keys():
            return self.vertices[vertex_id]
        else:
            return None

    def get_vertices(self):
        """
        Returns list of all vertices
        param: self
        return: list of vertices
        """

        my_list = []
        for value in self.vertices.values():
            my_list.append(value)

        return my_list

    def get_edge(self, start_id, dest_id):
        """
        Gets edge betwen 2 vertices
        param: self
        param: start_id
        param: dest_id
        return: edge weight
        """
        vert_dict = self.vertices

        if start_id not in self.vertices.keys():
            return None

        if dest_id not in vert_dict.keys():
            return None

        vertex = vert_dict[start_id]

        if dest_id in vertex.adj.keys():
            return (start_id, dest_id, vertex.adj[dest_id])
        else:
            return None

    def get_edges(self):
        """
        Returns list of all edges in the graph
        param: self
        return: list of edges
        """
        my_list = []

        for v_id in self.vertices.keys():
            vertex = self.vertices[v_id]
            for adj, weight in vertex.adj.items():
                my_list.append((v_id, adj, weight))

        return my_list

    def add_to_graph(self, start_id, dest_id=None, weight=0):
        """
        Adds item to graph
        param: self
        param: start_id
        """

        if self.get_vertex(start_id) is None:
            self.vertices[start_id] = Vertex(start_id)
            self.size += 1

        if dest_id is not None:
            if self.get_vertex(dest_id) is None:
                self.vertices[dest_id] = Vertex(dest_id)
                self.size += 1

            start_vertex = self.vertices[start_id]
            start_vertex.adj[dest_id] = weight

    def construct_from_matrix(self, matrix):
        """
        Constructs graph from a matrix
        param: self
        param: matrix
        """

        for i in range(1, len(matrix)):

            for j in range(1, len(matrix)):

                # Check if Vertices are adjacent, if so add them to graph
                # If no adjacents, add vertex to the graph with no weight

                if matrix[i][j] is None:
                    # Same Vertex Intersection, add with no weights
                    if i == j:
                        self.add_to_graph(matrix[i][0])
                    # diff but no intersection
                    elif i != j:
                        self.add_to_graph(matrix[i][0])
                        self.add_to_graph(matrix[0][j])

                elif matrix[i][j] is not None:
                    # Intersection
                    self.add_to_graph(matrix[i][0], matrix[0][j], matrix[i][j])


    def construct_from_csv(self, csv):
        pass

    def construct_matrix_from_graph(self):
        pass

    def bfs(self, start_id, target_id):
        """
        BFS starting at start_id ending at target
        param: self
        param: start_id
        param: target_id
        return: bfs
        """


        my_list = []
        distance = 0

        if self.get_vertex(start_id) is None:
            return ([], 0)
        if self.get_vertex(target_id) is None:
            return ([], 0)

        discovered = dict()
        level = [start_id]

        while len(level) > 0:
            next_level = []
            for u in level:
                # w is the actual vertex, u is the ID
                w = self.get_vertex(u)
                # Get the incident edges
                edges = w.get_edges()
                for e in edges:
                    v = e[0]
                    if v not in discovered:
                        discovered[v] = (u, e[1])
                        next_level.append(v)

                        if v is target_id:
                            my_list.append(v)
                            key = v
                            while key is not start_id:
                                (new_key, weight) = discovered[key]
                                distance = distance + weight
                                my_list.append(new_key)
                                key = new_key
            level = next_level

        my_list.reverse()
        return (my_list, distance)

    def dfs(self, start_id, target_id):

        path1 = []
        d = 0
        self.reset_vertices()
        if self.get_vertex(start_id) is None:
            return ([], 0)
        if self.get_vertex(target_id) is None:
            return ([], 0)

        vertex = self.get_vertex(start_id)
        vertex.visited = True
        result = self._dfs_recursive(start_id, target_id, path1, d)

        path = result[0]
        distance = result[1]

        if path:

            path.append(start_id)
            path.reverse()

        else:
            path = []
            distance = 0

        return path, distance

    def _dfs_recursive(self, current_id, target_id, path=[], dist=0):

        if self.get_vertex(current_id) is None:
            return ([], 0)
        if self.get_vertex(target_id) is None:
            return ([], 0)

        w = self.get_vertex(current_id)
        edges = w.get_edges()
        for e in edges:
            v = e[0]
            vertex = self.get_vertex(v)

            if vertex.visited is False:
                vertex.visited = True

                if v is target_id:
                    path.append(v)
                    dist += e[1]
                    return path, dist

                result = self._dfs_recursive(v, target_id, path, dist)

                if result:
                    path = result[0]
                    path.append(v)
                    dist = result[1] + e[1]

        return path, dist



    def a_star(self, start_id, target_id):
        pass

    def make_equivalence_relation(self):
        pass


class AStarPriorityQueue:
    """
    Priority Queue built upon heapq module with support for priority key updates
    Created by Andrew McDonald
    Inspired by https://docs.python.org/2/library/heapq.html
    """

    __slots__ = ['__data', '__locator', '__counter']

    def __init__(self):
        """
        Construct an AStarPriorityQueue object
        """
        self.__data = []                        # underlying data list of priority queue
        self.__locator = {}                     # dictionary to locate vertices within priority queue
        self.__counter = itertools.count()      # used to break ties in prioritization

    def __repr__(self):
        """
        Represent AStarPriorityQueue as a string
        :return: string representation of AStarPriorityQueue object
        """
        lst = [f"[{priority}, {vertex}], " if vertex is not None else "" for priority,
              count, vertex in self.__data]
        return "".join(lst)[:-1]

    def __str__(self):
        """
        Represent AStarPriorityQueue as a string
        :return: string representation of AStarPriorityQueue object
        """
        return repr(self)

    def empty(self):
        """
        Determine whether priority queue is empty
        :return: True if queue is empty, else false
        """
        return len(self.__data) == 0

    def push(self, priority, vertex):
        """
        Push a vertex onto the priority queue with a given priority
        :param priority: priority key upon which to order vertex
        :param vertex: Vertex object to be stored in the priority queue
        :return: None
        """
        count = next(self.__counter)
        # list is stored by reference, so updating will update all refs
        node = [priority, count, vertex]
        self.__locator[vertex.id] = node
        heapq.heappush(self.__data, node)

    def pop(self):
        """
        Remove and return the (priority, vertex) tuple with lowest priority key
        :return: (priority, vertex) tuple where priority is key,
        and vertex is Vertex object stored in priority queue
        """
        vertex = None
        while vertex is None:
            # keep popping until we have valid entry
            priority, count, vertex = heapq.heappop(self.__data)
        del self.__locator[vertex.id]                   # remove from locator dict
        vertex.visit()                  # indicate that this vertex was visited
        return priority, vertex

    def update(self, new_priority, vertex):
        """
        Update given Vertex object in the priority queue to have new priority
        :param new_priority: new priority on which to order vertex
        :param vertex: Vertex object for which priority is to be updated
        :return: None
        """
        node = self.__locator.pop(vertex.id)    # delete from dictionary
        node[-1] = None                         # invalidate old node
        self.push(new_priority, vertex)         # push new node
