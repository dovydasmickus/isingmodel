import numpy as np
import random

def init_lattice(rows,columns):
    lattice = np.zeros((rows,columns))
    for i in range(rows):
        for j in range(columns):
                lattice[i][j] = random.choice((-1,1))
    return lattice
    
print init_lattice(4,4)