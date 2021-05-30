from linked_list import LinkedList
from queue import Queue


class GraphNode:

    def __init__(self, data):
        self.data = data
        self.connections = LinkedList()

    def add_connection(self, graph, node_to):
        for i in range(len(self.connections)):
            if self.connections[i].data == node_to:
                return

        for i in range(len(graph)):
            if graph[i].data == node_to:
                self.connections.append(graph[i])
                graph[i].connections.append(self)
                return

        node_to = GraphNode(node_to)
        self.connections.append(node_to)
        node_to.connections.append(self)
        graph.append(node_to)

    def delete_connection(self, connection):
        for i in range(len(self.connections)):
            if self.connections[i] == connection:
                self.connections.delete(i)

    def delete_connections(self):
        for i in range(len(self.connections)):
            self.connections[i].delete_connection(self)


class Graph:

    def __init__(self, edges):
        self.nodes = LinkedList()
        for i in range(len(edges)):
            self.create_node(edges[i][0], edges[i][1])

    def insert(self, data, connections):
        for i in range(len(self.nodes)):
            if self.nodes[i].data == data:
                for j in range(len(connections)):
                    self.nodes[i].add_connection(self.nodes, connections[j])
                return

        node = GraphNode(data)
        for i in range(len(connections)):
            node.add_connection(self.nodes, i)
        self.nodes.append(node)

    def lookup(self, value):
        queue = Queue(self.nodes[0])
        checked = LinkedList()
        while len(queue) > 0:
            item = queue.dequeue()
            if item.data == value:
                return item
            checked.append(item)
            for i in range(len(item.connections)):
                if item.connections[i] not in checked:
                    queue.enqueue(item.connections[i])
        raise ValueError('Node is not in graph')

    def delete(self, value):
        for i in range(len(self.nodes)):
            if self.nodes[i].data == value:
                self.nodes[i].delete_connections()
                self.nodes.delete(i)
                return
        raise ValueError('Node is not in graph')

    def create_node(self, node_from, node_to):
        if node_to == node_from:
            raise ValueError('Nodes must be different')
        for i in range(len(self.nodes)):
            if self.nodes[i].data == node_from:
                self.nodes[i].add_connection(self.nodes, node_to)
                return
        node_from = GraphNode(node_from)
        node_from.add_connection(self.nodes, node_to)
        self.nodes.append(node_from)


edges = LinkedList(LinkedList(1, 2))
graph = Graph(edges)
print(graph.lookup(1))
graph.delete(1)
print(graph.lookup(2))

