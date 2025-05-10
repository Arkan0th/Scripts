import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import norm

def gauss(x, a, x0, sigma):
    return a * np.exp(-(x - x0) ** 2 / (2 * sigma ** 2))

def load_data(file_path):
    try:
        return np.loadtxt(file_path)
    except Exception as e:
        print(f"Error while loading {file_path}: {e}")
        return None

folder_path = 'clicks'
files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

for i, file_name in enumerate(files):
    file_path = os.path.join(folder_path, file_name)
    data = load_data(file_path)
    if data is None:
        continue

    # --- Filter data for "100 clicks" files ---
    if "100 clicks" in file_name.lower():
        data = data[50 <= data]
        data = data[data <= 150]

    counts, bin_edges = np.histogram(data, bins='auto', density=False)
    bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])
    mean_val = np.mean(data)

    plt.figure(i)
    plt.hist(data, bins='auto', density=False, alpha=0.5, edgecolor='black', label='Histogram')

    if "100 clicks" in file_name.lower():
        mu_init, std_init = norm.fit(data)
        a_init = np.max(counts)
        try:
            popt, _ = curve_fit(gauss, bin_centers, counts, p0=[a_init, mu_init, std_init])
            fitted = gauss(bin_centers, *popt)
            plt.plot(bin_centers, fitted, 'r-', lw=2, label=f'Gaussian Fit\nμ={popt[1]:.2f}, σ={popt[2]:.2f}')
        except RuntimeError as e:
            print(f"Fit failed for {file_name}: {e}")

    plt.axvline(mean_val, color='g', linestyle='--', label=f'Mean = {mean_val:.2f}')

    plt.title(f'Histogram - {file_name}')
    plt.xlabel('Value')
    plt.ylabel('Count')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()

plt.show()

