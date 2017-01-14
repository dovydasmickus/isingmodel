import numpy as np
import random

kb = 1.36 * 10**-23

def init_lattice(rows,columns):
    lattice = np.zeros((rows,columns))
    for i in range(rows):
        for j in range(columns):
                lattice[i][j] = random.choice((-1,1))
    return lattice
    
#print init_lattice(4,4) test code

def hamiltonian_energy(lattice,lattice_size , x, y): # buggy function
    left = 0
    right = 0
    top = 0
    bottom = 0
    print x, y
    if(x < lattice_size - 1):
        right = lattice[x+1][y]
    else:
        right = 0
        
    if(x > 0):
        left = lattice[x-1][y]
    else:
        left = 0
        
    if(y < lattice_size - 1):
        bottom = lattice[x][y+1]
    else:
        bottom = 0
        
    if(y > 0):
        top = lattice[x][y-1]
    else:
        top = 0
    
    return -2 * lattice[x][y] * (left + right + top + bottom)
    
def monte_carlo():
    lattice_size = 4
    monte_iteration = 5
    T = 5
    lattice = init_lattice(lattice_size, lattice_size)
    for s in range(monte_iteration):
        print s # debug print
        for i in range(lattice_size):
            for j in range(lattice_size):
                energy = hamiltonian_energy(lattice, lattice_size, i, j)
                if energy < 0 :
                    lattice[i][j] *= -1
                elif np.exp((-1/(kb*T))*energy) > random.random():
                    lattice[i][j] *= -1
                else:
                    continue
            
monte_carlo()