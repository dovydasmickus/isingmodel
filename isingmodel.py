import numpy as np
import random

def init_lattice(rows,columns):
    lattice = np.zeros((rows,columns))
    for i in range(rows):
        for j in range(columns):
                lattice[i][j] = random.choice((-1,1))
    return lattice
    
def hamiltonian_energy(lattice,lattice_size , x, y): 
    left = 0
    right = 0
    top = 0
    bottom = 0
    if(x < lattice_size - 1):
        right = lattice[x+1][y]
    else:
        right = lattice[0][y]
        
    if(x > 0):
        left = lattice[x-1][y]
    else:
        left = lattice[lattice_size-1][y]
        
    if(y < lattice_size - 1):
        bottom = lattice[x][y+1]
    else:
        bottom = lattice[x][0]
        
    if(y > 0):
        top = lattice[x][y-1]
    else:
        top = lattice[x][lattice_size - 1]
    
    return -1 * lattice[x][y] * (left + right + top + bottom)
    
def spin_flip(lattice, lattice_size, i, j, T):
    energy = hamiltonian_energy(lattice, lattice_size, i, j)
    flip_energy = -energy
    energy_diff = flip_energy - energy
    if energy_diff < 0 or np.exp(-(energy_diff)/(T)) > random.random() :
        lattice[i][j] *= -1
        energy = flip_energy
    return lattice, energy 

    
def monte_carlo():
    
    lattice_size = 10
    T = 0.01
    Tlist = []
    Tmax = 5
    Tstep = 0.01
    lattice = init_lattice(lattice_size, lattice_size)
    lattice_energies = []
    lattice_mag = []
    
    while T < Tmax:
        i = 0
        
        while i < (lattice_size**2) * 3:
            x = random.randint(0,lattice_size-1)
            y = random.randint(0,lattice_size-1)
            latt_E = spin_flip(lattice, lattice_size, x, y, T)
            lattice = latt_E[0]
            i += 1
            
        i = 0
        energy = 0
        mag = 0
        
        while i < (lattice_size** 2) * 1:
            x = random.randint(0,lattice_size-1)
            y = random.randint(0,lattice_size-1)
            temp_energy = hamiltonian_energy(lattice,lattice_size, x, y)
            energy += temp_energy
            mag += lattice[x][y]
            i += 1
            
        energy = energy / ((lattice_size ** 2) * 1)
        mag = mag / (((lattice_size ** 2) * 1) ** 2)
        lattice_energies.append(energy)
        lattice_mag.append(mag)
        Tlist.append(T)
        T += Tstep
        


    
monte_carlo()
