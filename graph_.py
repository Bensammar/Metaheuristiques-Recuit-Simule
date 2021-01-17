import networkx as nx
import matplotlib.pyplot as plt


# Affichage graphique de graphe (nœuds avec étiquettes, connexions)
def show(g, pos=None, rows=None, cols=None, orig=(0, 0)):
    if pos is None:
        pos = [((i % cols), i // rows) for i in range(0, cols * rows)]
    plt.clf()
    p = [(x + orig[0], y - orig[1]) for x, y in pos]
    nx.draw_networkx_nodes(g, p, node_color="#00b4d9")
    nx.draw_networkx_edges(g, p)
    nx.draw_networkx_labels(g, p)
    plt.axis('off')
    plt.pause(0.01)


# Ajouter les connexions entre les nœuds
def regular_grid(cols, rows):
    g = nx.Graph()
    g.add_nodes_from(list(range(0, rows * cols)))

    for i in range(0, cols - 1):
        for j in range(0, rows - 1):
            g.add_edge(i + j * cols, i + 1 + j * cols)
            g.add_edge(i + j * cols, i + (j + 1) * cols)

    for i in range(0, rows - 1):
        g.add_edge((cols - 1) + i * cols, (cols - 1) + (i + 1) * cols)

    for i in range(0, cols - 1):
        g.add_edge(i + (rows - 1) * cols, i + 1 + (rows - 1) * cols)
    return g
