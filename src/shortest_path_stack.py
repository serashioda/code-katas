"""Module with implementation of Linked List, Stack and Weighted Graph."""
#from my_queue import Queue
from collections import OrderedDict
import sys


#------------------------Linked List--------------------------
class LinkedList(object):
    """Classic linked list data structure."""

    def __init__(self, iterable=None):
        """Initialize LinkedList instance."""
        self.head = None
        self._length = 0
        try:
            for el in iterable:
                self.push(el)
        except TypeError:
            self.head = iterable

    def push(self, val):
        """Insert val at the head of linked list."""
        self.head = Node(val, self.head)
        self._length += 1

    def pop(self):
        """Pop the first value off of the head and return it."""
        if self.head is None:
            raise IndexError("Cannot pop from an empty linked list.")
        first = self.head.val
        self.head = self.head.next
        self._length -= 1
        return first

    def size(self):
        """Return length of linked list."""
        return self._length

    def search(self, val):
        """Will return the node from the list if present, otherwise none."""
        search = self.head
        while search:
            if search.val == val:
                return search
            search = search.next
        return None

    def remove(self, node):
        """Remove a node from linked list."""
        if type(node) is Node:
            prev = None
            curr = self.head
            while curr:
                if curr is node:
                    if prev:
                        prev.next = curr.next
                    else:
                        self.head = curr.next
                    self._length -= 1
                    break
                prev = curr
                curr = curr.next
            else:
                raise ValueError("Cannot remove node not in list.")
        else:
            raise ValueError("Argument to remove must be of node type.")

    def display(self):
        """Display linked list in tuple literal form."""
        res = "("
        curr = self.head
        while curr:
            val = curr.val
            if type(val) is str:
                val = "'" + val + "'"
            else:
                val = str(val)
            res += val
            if curr.next:
                res += ', '
            curr = curr.next
        return res + ')'

    def __len__(self):
        """Return length of linked_list."""
        return self.size()

    def __repr__(self):
        """Shortcut for displaying representation of list."""
        return self.display()


#------------------------Stack--------------------------


class Node(object):
    """Node class."""

    def __init__(self, val, next=None):
        """Initialize Node instance."""
        self.val = val
        self.next = next

class Stack(object):
    """Stack data structure class."""

    def __init__(self, iterable=None):
        """Stack constructor."""
        self._linkedlist = LinkedList(iterable)
        self._update_attr()

    def push(self, val):
        """Add value to top of stack."""
        self._linkedlist.push(val)
        self._update_attr()

    def pop(self):
        """Remove and return top of stack."""
        try:
            res = self._linkedlist.pop()
            self._update_attr()
            return res
        except IndexError:
            raise IndexError("Cannot pop from empty stack.")

    def size(self):
        """Return size of stack."""
        return self._linkedlist.size()

    def __len__(self):
        """Return size of stack with len builtin."""
        return self.size()

    def _update_attr(self):
        self.top = self._linkedlist.head


class Graph(object):
    """Implementation of Graph Traversal."""

    def __init__(self):
        """."""
        self.node_dict = {}

    def nodes(self):
        """Return a list of all nodes in the graph."""
        return list(self.node_dict.keys())

    def edges(self):
        """Return a list of all edges in the graph."""
        edge_list = []
        for node1 in self.node_dict:
            for node2 in self.node_dict[node1]:
                edge_list.append((node1,
                                  node2,
                                  self.node_dict[node1][node2]))
        return edge_list

    def weight(self, n1, n2):
        """."""
        return self.node_dict[n1][n2]

    def add_node(self, n):
        """Add a node 'n' to the graph."""
        self.node_dict.setdefault(n, OrderedDict())

    def add_edge(self, n1, n2, weight=0):
        """Add an edge to the graph with source, dest of 'n1', 'n2'. Add node if either not present."""
        self.add_node(n1)
        self.add_node(n2)
        if n2 in self.node_dict[n1]:
            raise ValueError("Edge already exists")
        self.node_dict[n1][n2] = weight

    def del_node(self, n):
        """Delete the node 'n' from the graph. Raise error if no such node exists."""
        if n in self.node_dict:
            del self.node_dict[n]
            for node in self.node_dict:
                try:
                    self.del_edge(node, n)
                except:
                    pass
        else:
            raise KeyError("Cannot remove node that does not exist.")

    def del_edge(self, n1, n2):
        """Delete edge from 'n1' to 'n2'. Raise error if no such edge exists."""
        if n1 in self.node_dict and n2 in self.node_dict[n1]:
            del self.node_dict[n1][n2]
        else:
            raise KeyError("Cannot remove edge that does not exist.")

    def has_node(self, n):
        """True or False based on if node 'n' is present in the graph."""
        return n in self.node_dict

    def neighbors(self, n):
        """Return the list of all nodes connected to 'n' by edges. Raise error if n is not present."""
        if n not in self.node_dict:
            raise KeyError("Cannot return neighbors of node that does not exist.")
        return self.node_dict[n]

    def adjacent(self, n1, n2):
        """Return True/False for if an edge connects 'n1' and 'n2'. Raises error if either nodes not present."""
        if n1 in self.node_dict and n2 in self.node_dict:
            return n2 in self.node_dict[n1]
        raise KeyError("Nodes not in graph!")

    def depth_first_traversal(self, start, track=None):
        """Graph traversal depth first."""
        res = [start]
        if track is None:
            track = set()
        track.add(start)
        try:
            for n in self.node_dict[start]:
                if n not in track:
                    res += self.depth_first_traversal(n, track)
        except KeyError:
            raise KeyError(str(start) + ' not in graph')
        return res

    # def breadth_first_traversal(self, start):
    #     """Breadth version of graph traversal."""
    #     try:
    #         res = []
    #         queue = Queue([start])
    #         track = set()
    #         while queue.head:
    #             cur_node = queue.dequeue()
    #             if cur_node not in track:
    #                 res.append(cur_node)
    #                 track.add(cur_node)
    #                 for child in self.node_dict[cur_node]:
    #                     queue.enqueue(child)
    #     except KeyError:
    #         raise KeyError(str(start) + ' not in graph')
    #     return res

    def depth_first_traversal_iterative(self, start):
        """Breadth version of graph traversal."""
        try:
            res = []
            stack = Stack([start])
            track = set()
            while stack.top:
                cur_node = stack.pop()
                if cur_node not in track:
                    res.append(cur_node)
                    track.add(cur_node)
                    for child in reversed(self.node_dict[cur_node]):
                        stack.push(child)
        except KeyError:
            raise KeyError(str(start) + ' not in graph')
        return res

    def dijkstra(self, start, end):
        """Dykstras shortest path implementation."""
        unvisited = self.nodes()
        distance = {}
        previous = {}
        for node in unvisited:
            distance[node] = sys.maxsize
        distance[start] = 0
        while len(unvisited) > 0:
            node = unvisited[0]
            smallest_curr = sys.maxsize
            for d in distance:
                if d in unvisited and distance[d] < smallest_curr:
                    node = d
                    smallest_curr = distance[d]
            unvisited.remove(node)
            for neighbor in self.neighbors(node).keys():
                alt_path = distance[node] + self.weight(node, neighbor)
                if alt_path < distance[neighbor]:
                    distance[neighbor] = alt_path
                    previous[neighbor] = node
        result = []
        result.append(end)
        curr = end
        while curr in previous:
            result.append(previous[curr])
            curr = previous[curr]
        return result

    def floyd_warshall(self):
        """Find all shortest paths and distances via floyd-warshall alg."""
        distance = {}
        path_dict = {}
        for from_node in self.nodes():
            distance[from_node] = {}
            path_dict[from_node] = {}
            for node in self.nodes():
                distance[from_node][node] = sys.maxsize
                path_dict[from_node][node] = None
            distance[from_node][from_node] = 0
            neighbors = self.neighbors(from_node)
            for neighbor in neighbors:
                distance[from_node][neighbor] = neighbors[neighbor]
                path_dict[from_node][neighbor] = neighbor
        for k in self.nodes():
            for i in self.nodes():
                for j in self.nodes():
                    if distance[i][k] + distance[k][j] < distance[i][j]:
                        distance[i][j] = distance[i][k] + distance[k][j]
                        path_dict[i][j] = path_dict[i][k]
        return path_dict, distance

    def floyd_warshall_path(self, path_dict, start, end):
            if path_dict[start][end] is None:
                return []
            path = [start]
            while start != end:
                start = path_dict[start][end]
                path.append(start)
            return path
