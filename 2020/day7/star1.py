import networkx as nx
from networkx_viewer import Viewer
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


def test_view_graph():
    input_data = [
        i
        for i in """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.""".splitlines()
    ]
    bag_graph = build_graph(input_data)
    app = Viewer(bag_graph)
    app.mainloop()


def main():
    input_data = get_input()
    bag_graph = build_graph(input_data)
    bag_criteria = "shiny gold"
    source_nodes = [i for i in bag_graph.nodes() if bag_graph.in_degree(i) == 0]
    possible_parents = set()
    for i in source_nodes:
        for path in nx.all_simple_paths(bag_graph, source=i, target=bag_criteria):
            possible_parents.update(set(path))
    possible_parents.remove(bag_criteria)
    print(len(possible_parents))


if __name__ == "__main__":
    main()
