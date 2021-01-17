import random
import sys

# try:
#     _seed = int(sys.argv[1])
# except IndexError:
#     _seed = random.randint(0, sys.maxsize)

_seed = 9168599813312280181

# Retourne le nombre aléatoire à virgule flottante
def get():
    return random.Random(_seed)


# Retourne la variable qui permet d'initialiser le générateur de nombres aléatoires
def seed():
    return _seed
