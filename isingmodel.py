import numpy as np
import random
import matplotlib.pyplot as plt

def init_lattice(rows,columns):
    lattice = np.zeros((rows,columns))
    for i in range(rows):
        for j in range(columns):
                lattice[i][j] = 1  #value doesn't matter as the monte carlo sampling will achieve equilibrium regardless. Not calling np.choice saves computation time.
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
    
    lattice_size = 30
    samples = 1
    T = 0.01
    Tlist = []
    Tmax = 5
    Tstep = 0.01
    lattice = init_lattice(lattice_size, lattice_size)
    print lattice
    lattice_energies = []
    lattice_energy_var = []
    lattice_mag = []
    lattice_mag_var = []
    
    while T < Tmax:
        i = 0
        
        while i < (lattice_size**2) * 5:
            x = random.randint(0,lattice_size-1)
            y = random.randint(0,lattice_size-1)
            latt_E = spin_flip(lattice, lattice_size, x, y, T)
            lattice = latt_E[0]
            i += 1
            
        i = 0
        energy = 0
        mag = 0
        energy_arr = []
        mag_arr = []
        
        while i < (lattice_size** 2) * samples:
            x = random.randint(0,lattice_size-1)
            y = random.randint(0,lattice_size-1)
            temp_energy = hamiltonian_energy(lattice,lattice_size, x, y)
            energy_arr.append(temp_energy)
            mag_arr.append(lattice[x][y])
            energy += temp_energy
            mag += lattice[x][y]
            i += 1
            
        energy = energy / ((lattice_size ** 2) * samples)
        mag = mag / (((lattice_size ** 2) * samples) ** 2)
        lattice_energies.append(energy)
        lattice_energy_var.append(variance(energy_arr))
        lattice_mag.append(mag)
        lattice_mag_var.append(variance(mag_arr))
        Tlist.append(T)
        T += Tstep
        #print "energy values = ", energy
    
    specificHeat = []    
    for i in range(len(lattice_energy_var)):
        specificHeat.append(lattice_energy_var[i] / (Tlist[i] ** 2))

    magneticSuscep = []
    
    for i in range(len(lattice_mag_var)):
        magneticSuscep.append(lattice_mag_var[i] / Tlist[i])
    
    plt.figure(1)
    plt.xlabel("Temperature(Kelvin)")
    plt.ylabel("Average Lattice Energies")
    plt.title("Average Lattice Energy vs Temperature(30x30 lattice)")
    plt.plot(Tlist, lattice_energies, 'b--')
    
    plt.figure(2)
    plt.xlabel("Temperature(Kelvin)")
    plt.ylabel("Average Magnestism")
    plt.title("Average Lattice Magnetism vs Temperature(30x30 lattice)")
    plt.plot(Tlist, lattice_mag, 'b--')
        
    plt.figure(3)
    plt.plot(Tlist,specificHeat, 'b--')
    plt.xlabel("Temperature(Kelvin)")
    plt.title("Specific Heat vs Temperature(30x30 lattice)")
    plt.ylabel("Specific Heat Capacity")
    
    plt.figure(4)
    plt.plot(Tlist, magneticSuscep, 'b--')
    plt.xlabel("Temperature(Kelvin)")
    plt.title("Magnetic Susceptability vs Temperature(30x30 lattice)")
    plt.ylabel("Magnetic Susceptability")
    plt.show()
        
        
def variance(valuelist):
    value = 0
    value_square = 0
    i = 0
    for n in valuelist:
        i += 1
        value += n
        value_square += n*n
    return (value_square - ((value**2)/i )) / i
    
    
    
monte_carlo()
