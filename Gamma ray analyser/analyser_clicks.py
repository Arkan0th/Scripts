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
folder_path = 'clicks'

# Seznam souborů ve složce
files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# Vytvoří graf pro každý soubor
for i, file_name in enumerate(files):
    file_path = os.path.join(folder_path, file_name)
    
    # Načte data ze souboru
    data = load_data(file_path)
    if data is None:
        continue
    
    x_values = np.arange(len(data))
    
    # Vytvoří nový canvas (graf)
    plt.figure(i)
    plt.plot(x_values, data, label='Data')
    plt.title(f'Graph of {file_name}')
    plt.xlabel('X')
    plt.ylabel('Y')
    

    plt.grid(True)

plt.show()

