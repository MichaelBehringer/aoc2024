import networkx as nx

def load_graph_from_file():
    graph = nx.Graph()
    for line in open("d23.txt", "rt"):
        node1, node2 = line.strip().split("-")
        graph.add_edge(node1, node2)
    return graph

def count_cycles_with_t_prefix(graph, max_cycle_length=3):
    cycle_count = 0
    for cycle in nx.simple_cycles(graph, length_bound=max_cycle_length):
        if any(str(node).startswith("t") for node in cycle):
            cycle_count += 1
    return cycle_count

def find_largest_clique(graph):
    max_clique = nx.approximation.max_clique(graph)
    return sorted(max_clique)

graph = load_graph_from_file()

print(count_cycles_with_t_prefix(graph))
print(find_largest_clique(graph))
