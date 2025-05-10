import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def exp_fit(x, a, b, c):
    return a * np.exp(-b * x) + c

def analyze_data(directory):
    for file_name in ['barium_pure', 'barium_cesium']:
        path = os.path.join(directory, file_name)

        if not os.path.exists(path):
            print(f"ERROR: File {file_name} not found in {directory}.")
            continue

        with open(path, 'r') as file:
            data = []
            for line in file:
                try:
                    data.append(int(line))
                except ValueError:
                    continue

        x_data = np.arange(len(data))
        y_data = np.array(data)

        try:
            (a, b, c), _ = curve_fit(exp_fit, x_data, y_data, p0=(max(y_data), 0.01, min(y_data)))
            halflife = np.log(2) / b
            error_halflife = np.sqrt(halflife)
        except Exception as e:
            print(f"ERROR: could not fit exponential function for {file_name}: {e}")
            continue

        print(f"{file_name} half-life: {halflife:.3f} ± {error_halflife:.3f} s")

        plt.figure()
        plt.plot(x_data, y_data, '.', label="Data")
        plt.plot(x_data, exp_fit(x_data, a, b, c), '--', label="Exponential Fit")
        plt.xlabel("Time [s]")
        plt.ylabel("Count")
        plt.title(f"Exponential fit for {file_name}")
        plt.legend()
        plt.grid()
        plt.show()

if __name__ == "__main__":
    analyze_data("data")

