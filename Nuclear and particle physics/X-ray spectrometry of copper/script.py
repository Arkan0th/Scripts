import os
import matplotlib.pyplot as plt
import numpy as np

folder_path = 'data'
files = [f for f in os.listdir(folder_path)]
data_groups = {
    'KBr_35kV': [],
    'LiF_35kV': [],
    'LiF_*': []
}

for file in files:
    if file.startswith('KBr_35kV'):
        data_groups['KBr_35kV'].append(file)
    elif file.startswith('LiF_35kV_full'):
        data_groups['LiF_35kV'].append(file)
    elif file.startswith('LiF_'):
        data_groups['LiF_*'].append(file)

def load_data(file_path):
    try:
        with open(file_path, 'r', encoding='latin1') as f:
            lines = f.readlines()[2:]
        data = []
        for line in lines:
            parts = line.strip().replace(',', '.').split()
            if len(parts) >= 2:
                try:
                    x = float(parts[0])
                    y = float(parts[1])
                    data.append((x, y))
                except ValueError:
                    continue
        return np.array(data)
    except Exception as e:
        print(f"Error while loading {file_path}: {e}")
        return None

def plot_group(group_name, file_list):
    plt.figure(figsize=(10, 6))
    found_data = False
    all_x_vals = []
    for file in file_list:
        path = os.path.join(folder_path, file)
        data = load_data(path)
        if data is not None and data.shape[1] >= 2:
            plt.plot(data[:, 0] / 2, data[:, 1], label=file)    #clarification note: y_vals = data[:, 0] / 2; y_vals = data[:, 1]
            all_x_vals.extend(data[:, 0] / 2)
            found_data = True
        else:
            print(f"File {file} has unrecognized data structure.")
    if found_data:
        plt.title(f'Graph of {group_name}')
        plt.xlabel('Angle [°]')
        plt.ylabel('Radiation intensity')
        plt.xlim(min(all_x_vals), max(all_x_vals))
        if group_name == 'KBr_35kV' or group_name == 'LiF_35kV':
            plt.yscale('log')
        elif group_name == 'LiF_*':
            plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(f'{group_name}.png', dpi=100)
        plt.show()
    else:
        print(f"No valid data in {group_name} data group.")

for group_name, file_list in data_groups.items():
    if file_list:
        plot_group(group_name, file_list)

