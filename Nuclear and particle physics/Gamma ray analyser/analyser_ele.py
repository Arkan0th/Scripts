import os
import matplotlib.pyplot as plt
import numpy as np

# Funkce pro načtení dat ze souboru
def load_data(file_path):
    try:
        data = np.loadtxt(file_path)
        return data
    except Exception as e:
        print(f"Error while loading {file_path}: {e}")
        return None

# Cesta ke složce, kde jsou soubory
folder_path = 'elements'

# Seznam souborů ve složce
files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# Vytvoří graf pro každý soubor
for i, file_name in enumerate(files):
    file_path = os.path.join(folder_path, file_name)
    
    # Načte data ze souboru
    data = load_data(file_path)
    if data is None:
        continue
    
    if "Na-22" in file_name:
        x_values = 4.481 * np.arange(len(data)) + 49.463
        plt.figure(i)
        plt.plot(x_values, data, label='Data')
        plt.title(f'Graph of {file_name}')
        plt.xlabel('Energy [keV]')
        plt.ylabel('Count')

        print("\n### Sodium-22 ###")
        plt.axvline(x=79, color='r', linestyle='--', label='X-ray from lead shielding interaction? (79 keV)')
        print("X-ray from lead shielding interaction?: 79 keV")
        plt.axvline(x=340, color='r', linestyle='--', label='e- e+ annihilation Compton edge (340 keV)')
        print("e- e+ annihilation Compton edge: 340 keV")
        plt.axvline(x=511, color='r', linestyle='--', label='e- e+ annihilation energy peak (511 keV)')
        print("e- e+ Annihilation energy peak: 511 keV")
        plt.axvline(x=1062, color='r', linestyle='--', label='Photopeak Compton edge (1062 keV)')
        print("Photopeak Compton edge: 1062 keV")
        plt.axvline(x=1275, color='r', linestyle='--', label='Photopeak (1275 keV)')
        print("Photopeak: 1275 keV")
        print("(Non distinct energy doublepeaks at ~206 keV and ~640 keV appear to be some kind of energy sum or effect of contamination, possibly backscatter in first case)")
        
        plt.legend()
        plt.yscale('log')
        plt.grid(True)
        plt.savefig('Na-22.png', dpi=300)

    elif "Cs-137" in file_name:
        x_values = 4.961 * np.arange(len(data))
        plt.figure(i)
        plt.plot(x_values, data, label='Data')
        plt.title(f'Graph of {file_name}')
        plt.xlabel('Energy [keV]')
        plt.ylabel('Count')

        print("\n### Cesium-137 ###")
        plt.axvline(x=30, color='r', linestyle='--', label='X-ray decay group (30 keV)')
        print("X-ray decay group: 30 keV")
        plt.axvline(x=191, color='r', linestyle='--', label='Backscatter peak (191 keV)')
        print("Backscatter peak: 191 keV")
        plt.axvline(x=467, color='r', linestyle='--', label='Compton edge (467 keV)')
        print("Compton edge: 467 keV")
        plt.axvline(x=670, color='r', linestyle='--', label='Energy peak (670 keV)')
        print("Energy peak: 670 keV")

        plt.legend()
        plt.yscale('log')
        plt.grid(True)
        plt.savefig('Cs-137.png', dpi=300)

    elif "Eu-152" in file_name:
        x_values = 4.961 * np.arange(len(data))
        plt.figure(i)
        plt.plot(x_values, data, label='Data')
        plt.title(f'Graph of {file_name}')
        plt.xlabel('Energy [keV]')
        plt.ylabel('Count')

        print("\n### Europium-152 ###")
        plt.axvline(x=35, color='r', linestyle='--', label='X-ray decay group (35 keV)')
        print("X-ray decay group: 35 keV")
        plt.axvline(x=119, color='r', linestyle='--', label='Energy peak (119 keV)')
        print("Energy peak: 119 keV")
        plt.axvline(x=243, color='r', linestyle='--', label='Energy peak (243 keV)')
        print("Energy peak: 243 keV")
        plt.axvline(x=342, color='r', linestyle='--', label='Energy peak (342 keV)')
        print("Energy peak: 342 keV")
        print("Other higher energy peaks are visible, however not as distinct")
        
        plt.legend()
        plt.yscale('log')
        plt.grid(True)
        plt.savefig('Eu-152.png', dpi=300)

plt.show()

