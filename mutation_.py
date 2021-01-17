import random_ as random

_random = random.get()


# Retourner le numéro de ligne et de la colonne de chaque nœud
def gen(g, cols, rows):
    return [(i % cols, i // rows) for i in range(0, len(g.nodes()))]


# Retourner une permutation des 2 emplacements obtenus aléatoirement (parmi les emplacements des nœuds)
def randomize(i, n=1):
    for j in range(0, n):
        first = _random.randrange(len(i))
        second = _random.randrange(len(i))
        while first == second:
            second = _random.randrange(len(i))
        i[first], i[second] = i[second], i[first]
    return i


# Retourner le cout entre tous les nœuds (longueur des connexions)
def cost(g, indiv, weight):
    dist = 0
    for u, v in g.edges():
        dist += (abs(indiv[u][0] - indiv[v][0]) + abs(indiv[u][1] - indiv[v][1])) * weight
    return dist
