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
    
    # Předpokládáme, že data jsou ve dvou sloupcích: x a y
    x_values = np.arange(len(data)) * 4.96  # Úprava x-ové osy
    
    # Vytvoří nový canvas (graf)
    plt.figure(i)
    plt.plot(x_values, data, label='Data')
    plt.title(f'Graph of {file_name}')
    plt.xlabel('Energy [keV]')
    plt.ylabel('Count')
    
        # Přidání asymptotické čáry pro odpovídající prvky
    if "Cesium" in file_name:
        plt.axvline(x=670, color='r', linestyle='--', label='Cesium energy peak (670 keV)')
        print("Cesium found energy peak: 670 keV")
        plt.axvline(x=191, color='r', linestyle=':', label='Cesium backscatter peak (191 keV)')
        print("Sodium found backscatter: 191 keV")
        plt.axvline(x=453, color='r', linestyle=':', label='Cesium Compton edge (453 keV)')
        print("Sodium found Compton edge: 453 keV")
    elif "Sodium" in file_name:
        plt.axvline(x=511, color='r', linestyle='--', label='Sodium annihilation energy peak (511 keV)')
        print("Sodium found e- e+ annihilation energy peak: 511 keV")
        plt.axvline(x=1355, color='r', linestyle='--', label='Sodium photopeak (1355 keV)')
        print("Sodium found energy photopeak: 1355 keV")
        plt.axvline(x=174, color='r', linestyle=':', label='Sodium Compton edge (174 keV)')
        print("Sodium found Compton edge: 174 keV")
    elif "Europium" in file_name:
        plt.axvline(x=119, color='r', linestyle='--', label='Europium energy peak (119 keV)')
        print("Europium found energy peak: 119 keV")
        plt.axvline(x=342, color='r', linestyle='--', label='Europium energy peak (342 keV)')
        print("Europium found energy peak: 342 keV")

    plt.legend()
    plt.grid(True)

plt.show()

