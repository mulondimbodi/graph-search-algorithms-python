import matplotlib.pyplot as plt
import networkx as nx

from bfs import bfs
from dfs import dfs
from iterative_deepening_dfs import iddfs


GRAPH = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": [],
}

POSITIONS = {
    "A": (0, 3),
    "B": (-1, 2),
    "C": (1, 2),
    "D": (-1.5, 1),
    "E": (-0.5, 1),
    "F": (1.5, 1),
    "G": (-0.5, 0),
}


def build_directed_graph(graph):
    directed_graph = nx.DiGraph()

    for node, neighbors in graph.items():
        if not neighbors:
            directed_graph.add_node(node)

        for neighbor in neighbors:
            directed_graph.add_edge(node, neighbor)

    return directed_graph


def visualize_graph(graph):
    directed_graph = build_directed_graph(graph)

    plt.figure(figsize=(6, 5))
    nx.draw(
        directed_graph,
        POSITIONS,
        with_labels=True,
        node_color="lightblue",
        node_size=2000,
        font_size=12,
        font_weight="bold",
        arrows=True,
    )
    plt.title("Directed Graph Representation")
    plt.show()


def main():
    visualize_graph(GRAPH)

    print("Breadth-First Search:", bfs(GRAPH, "A"))
    print("Depth-First Search:", dfs(GRAPH, "A"))
    print("Iterative Deepening DFS:", iddfs(GRAPH, "A", 3))


if __name__ == "__main__":
    main()