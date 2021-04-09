from collections import defaultdict


class Graph:
    def __init__(self):
        """
        self.edges is a dict of all possible next nodes
        e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights has all the weights between two nodes,
        with the two nodes as a tuple as the key
        e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        """
        self.edges = defaultdict(list)
        self.weights = {}

    def add_edge(self, from_node, to_node, weight):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight


def dijsktra(graph, initial, end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()

    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)

        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path


def poland_graph() -> Graph:
    graph = Graph()
    graph.add_edge('Ustka', 'Slupsk', 21)
    graph.add_edge('Ustka', 'Leba', 64)
    graph.add_edge('Slupsk', 'Bytow', 70)
    graph.add_edge('Slupsk', 'Lebork', 55)
    graph.add_edge('Leba', 'Lebork', 29)
    graph.add_edge('Koscierzyna', 'Lebork', 58)
    graph.add_edge('Bytow', 'Chojnice', 65)
    graph.add_edge('Bytow', 'Koscierzyna', 40)
    graph.add_edge('Chojnice', 'Koscierzyna', 70)
    graph.add_edge('Koscierzyna', 'Tczew', 59)
    graph.add_edge('Gdansk', 'Tczew', 33)
    graph.add_edge('Gdansk', 'Elblag', 63)
    graph.add_edge('Gdansk', 'Gdynia', 24)
    graph.add_edge('Gdynia', 'Lebork', 60)
    graph.add_edge('Gdynia', 'Wladyslawowo', 42)
    graph.add_edge('Wladyslawowo', 'Hel', 35)
    graph.add_edge('Wladyslawowo', 'Leba', 66)
    graph.add_edge('Koscierzyna', 'Gdansk', 58)
    graph.add_edge('Tczew', 'Elblag', 53)
    return graph


path = dijsktra(poland_graph(), 'Gdansk', 'Ustka')
print(path)
