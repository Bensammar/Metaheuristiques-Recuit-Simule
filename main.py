import matplotlib.pyplot as plt
import math
import copy

import graph_ as graph
import random_ as random
import mutation_ as mutation

EDGE_WEIGHT = 5                 # La distance entre deux blocs

ROWS = 5                        # Nombre de lignes de graphe
COLS = 5                        # Nombre de colonnes de graphe

TMAX = 25000.0                  # Température maximale
TMIN = 0.1                      # Température minimale

EPOCH = 10000                   # Nombre d'itérations
UPDATES = 20                    # Nombre de mises à jour d'affichage graphique au cours du processus

NODES = ROWS * COLS             # Nombre de nœuds

print('Seed = ', random.seed()) # Initialise le générateur de nombres aléatoires
random = random.get()           # Renvoie le nombre aléatoire à virgule flottante


# Générer un état initial de graphe aléatoirement
def make_state(g):
    state = mutation.randomize(mutation.gen(g, COLS, ROWS), NODES * NODES)
    return mutation.cost(g, state, EDGE_WEIGHT), state


# Mise à jour de graphique affiché
def update(g, state, epoch, temp, acceptance=1, improvement=1):
    tmpsig = int(math.log10(TMAX) - math.log10(TMIN))
    print('Itération ' + ('%' + str(math.log10(EPOCH) + 1) + 'd') % epoch + ': Longueur optimale =', state[0], 'T∘ =', \
          (('{0:.' + str(tmpsig) + 'g}').format(temp) + ' ' * tmpsig)[:tmpsig + 1] + '\t', \
          '✓', '{0:.3g}'.format(acceptance * 100.), '🡹', '{0:.3g}'.format(improvement * 100.))
    graph.show(g, state[1])
    plt.savefig("Itération-" + str(epoch) + ".png")


# Permuter 2 composants (nœuds) et retourner l'état de graphe + le cout
def move(g, state):
    indiv = mutation.randomize(state[1])
    return mutation.cost(g, indiv, EDGE_WEIGHT), indiv


# Appliquer l'algorithme de récuit simulé sur le graphe
def optimize(g):
    epoch = 0
    state = make_state(g)
    prev, best = copy.deepcopy(state), copy.deepcopy(state)

    tfactor = -math.log(TMAX / TMIN)
    temp = TMAX

    trials, accepts, improves = 0, 0, 0
    if UPDATES > 0:
        freq = EPOCH / UPDATES
        update(g, state, epoch, temp)

    while epoch < EPOCH:
        temp = TMAX * math.exp(tfactor * epoch / EPOCH)
        state = move(g, state)

        costdiff = state[0] - prev[0]
        trials += 1
        if costdiff > 0 and math.exp(-costdiff / temp) < random.random():
            state = copy.deepcopy(prev)
        else:
            accepts += 1
            if costdiff < 0:
                improves += 1
            prev = copy.deepcopy(state)
            if state[0] < best[0]:
                best = copy.deepcopy(state)

        epoch += 1

        if UPDATES > 1 and epoch // freq > (epoch - 1) // freq:
            update(g, state, epoch, temp, accepts / trials, improves / trials)
            trials, accepts, improves = 0, 0, 0

    return best


G = graph.regular_grid(COLS, ROWS)
best = optimize(G)

print('Longueur optimale trouvée :', best[0])
graph.show(G, best[1], cols=COLS, rows=ROWS)
plt.savefig("résultat.png")
plt.pause(0)
