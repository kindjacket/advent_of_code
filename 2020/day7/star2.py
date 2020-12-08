import networkx as nx
from utils import get_input


def build_graph(input_data):
    G = nx.DiGraph()
    for i in input_data:
        bag_node = i.split(" contain ")[0].replace(" bags", "")
        contain_data_raw = i.split(" contain ")[1]
        if contain_data_raw != "no other bags.":
            contain_nodes_raw = contain_data_raw.replace(".", "").split(", ")
            contain_nodes = [
                (j.split(" ")[1] + " " + j.split(" ")[2], int(j.split(" ")[0]))
                for j in contain_nodes_raw
            ]
            for k in contain_nodes:
                G.add_edge(bag_node, k[0], weight=k[1])
        else:
            G.add_node(bag_node)
    return G


def generate_path_value(graph: nx.DiGraph, path: list[str]):
    product = 1
    for idx, i in enumerate(path):
        if idx < (len(path) - 1):
            product = product * graph[i][path[idx + 1]]["weight"]
    return product


def main():
    input_data = get_input()
    bag_graph = build_graph(input_data)
    bag_criteria = "shiny gold"
    sink_nodes = [i for i in bag_graph.nodes() if bag_graph.out_degree(i) == 0]
    possible_children = set()
    for i in sink_nodes:
        for path in nx.all_simple_paths(bag_graph, source=bag_criteria, target=i):
            possible_children.update(set(path))
    possible_children.remove(bag_criteria)
    all_paths = []
    for i in possible_children:
        all_paths.extend(nx.all_simple_paths(bag_graph, source=bag_criteria, target=i))
    path_lengths = [generate_path_value(bag_graph, i) for i in all_paths]
    print(sum(path_lengths))


if __name__ == "__main__":
    main()
