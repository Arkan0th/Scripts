import os
import matplotlib.pyplot as plt
import numpy as np

# Function to load data from a file
def load_data(file_path):
    try:
        data = np.loadtxt(file_path)
        return data
    except Exception as e:
        print(f"Error while loading {file_path}: {e}")
        return None

# Path to the folder containing files
folder_path = 'clicks'

# List of files in the folder
files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# Create a histogram for each file
for i, file_name in enumerate(files):
    file_path = os.path.join(folder_path, file_name)
    
    # Load data from file
    data = load_data(file_path)
    if data is None:
        continue
    
    # Create a new figure for the histogram
    plt.figure(i)
    plt.hist(data, bins=50, edgecolor='black', alpha=0.75)  # Histogram with 20 bins
    plt.title(f'Histogram of {file_name}')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid(True, linestyle='--', alpha=0.6)

plt.show()

