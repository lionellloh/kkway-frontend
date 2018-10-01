from map_config import *
from graph import Graph, generate_route


g = Graph(map_graph)


if __name__ == '__main__':
    print("[ INFO] Sample Query:\n")
    nodes = g.shortest_path('2.201', '1.5corner4')
    print(generate_route(nodes))
    print("\n[ INFO] End Sample Query.")
