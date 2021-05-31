"""
Graph realization
"""
from queue import Queue
from linked_list import LinkedList


class GraphNode:
    """
    Represents a graph node.
    Stores node data and connected nodes
    """
    def __init__(self, data):
        self.data = data
        self.connections = LinkedList()

    def add_connection(self, graph, node_to):
        """
        add_connection(graph: LinkedList, node_to) -> None

        Adds node to self.connections if it`s not there yet
        """
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
        """
        delete_connections(connection: GraphNode)

        Deletes node from self.connections if it`s there
        """
        for i in range(len(self.connections) - 1):
            if self.connections[i] == connection:
                self.connections.delete(i)

    def delete_connections(self):
        """
        delete_connections()

        Used to remove connections from a node when deleting it
        """
        for i in range(len(self.connections)):
            self.connections[i].delete_connection(self)


class Graph:
    """
    Represents undirected graph.
    Store list of graph nodes
    """
    def __init__(self, edges):
        self.nodes = LinkedList()
        for i in range(len(edges)):
            self.create_node(edges[i][0], edges[i][1])

    def __str__(self):
        result = LinkedList()
        for i in range(len(self.nodes)):
            connections = LinkedList()
            for j in range(len(self.nodes[i].connections)):
                connections.append(self.nodes[i].connections[j].data)
            connections = str(connections)
            node = f'{self.nodes[i].data}: {connections}'
            result.append(node)
        return str(result)

    def insert(self, data, connections):
        """
        insert(data, connections: LinkedList) -> None

        Adds a node and its connections to graph.
        If node is already in graph it only adds connections
        """
        for i in range(len(self.nodes)):
            if self.nodes[i].data == data:
                for j in range(len(connections)):
                    self.nodes[i].add_connection(self.nodes, connections[j])
                return

        node = GraphNode(data)
        for i in range(len(connections)):
            node.add_connection(self.nodes, connections[i])
        self.nodes.append(node)

    def lookup(self, value):
        """
        lookup(value) -> GraphNode

        Searches a node by value.
        Raises ValueError if node with given value is not in graph
        """
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
        """
        delete(value) -> None

        Deletes a node and all its connections by value.
        Raises ValueError if node with given value is not in graph
        """
        for i in range(len(self.nodes)):
            if self.nodes[i].data == value:
                self.nodes[i].delete_connections()
                self.nodes.delete(i)
                return
        raise ValueError('Node is not in graph')

    def create_node(self, node_from, node_to):
        """
        create_node(node_from, node_to) -> None

        Creates a node.
        Used when initializing a graph.
        Raises ValueError if start and end nodes are the same
        """
        if node_to == node_from:
            raise ValueError('Nodes must be different')
        for i in range(len(self.nodes)):
            if self.nodes[i].data == node_from:
                self.nodes[i].add_connection(self.nodes, node_to)
                return
        node_from = GraphNode(node_from)
        node_from.add_connection(self.nodes, node_to)
        self.nodes.append(node_from)


def main():
    """
    main()

    Main function to demonstrate program functionality
    """
    edg = LinkedList(LinkedList(0, 1), LinkedList(0, 2), LinkedList(1, 4),
                     LinkedList(2, 3), LinkedList(3, 1), LinkedList(4, 3))
    grp = Graph(edg)
    print('graph:\n')
    print(grp)
    grp.insert(5, LinkedList(0, 1, 3))
    print('\ninsert(5: 0, 1, 3)\n')
    print(grp)
    print('\nlookup(5)\n')
    print(f'{grp.lookup(5)}: {grp.lookup(5).data}')
    grp.delete(0)
    print('\ndelete(0)\n')
    print(grp)


if __name__ == "__main__":
    main()
