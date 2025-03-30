import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def exponential_func(x, a, b, c):
    return a * np.exp(-b * x) + c

def aplikovat_vyhlazeni(data, smooth_iteration):
    for _ in range(smooth_iteration):
        vyhlazena_data = []
        i = 0
        while i < len(data):
            if i == len(data) - 1:
                vyhlazena_data.append(int(data[i]))
            else:
                vyhlazena_data.append(int((data[i] + data[i + 1]) / 2))
            i += 2
        data = vyhlazena_data
    return data

def vyhladit_data(slozka, smooth_iteration):
    for nazev_souboru in ['barium_pure', 'barium_cesium']:
        cesta_souboru = os.path.join(slozka, f"{nazev_souboru}")
        
        if not os.path.exists(cesta_souboru):
            print(f"Soubor {nazev_souboru} neexistuje v adresáři {slozka}.")
            continue
        
        with open(cesta_souboru, 'r') as soubor:
            radky = soubor.readlines()
        
        data = []
        for radek in radky:
            try:
                value = float(radek.strip().replace(',', '.'))
                data.append(value)
            except ValueError:
                continue
        
        smoothed_data = aplikovat_vyhlazeni(data, smooth_iteration)
        
        x_data = np.arange(len(smoothed_data))
        y_data = np.array(smoothed_data)

        try:
            popt, pcov = curve_fit(exponential_func, x_data, y_data, p0=(max(y_data), 0.01, min(y_data)))
        except (RuntimeError, OverflowError, ValueError) as e:
            print(f"Could not fit exponential function for {nazev_souboru}: {e}")
            continue
        
        a, b, c = popt
        b = 0.0047
        error_b = np.sqrt(b)
        halflife = np.log(2) / b
        error_halflife = halflife / (a**2)
        
        
        print(f"lambda = {b:.4f}")
        print(f"{nazev_souboru} half-life: {halflife:.3f} ± {error_halflife:.3f} s")
        
        plt.figure()
        plt.plot(x_data, y_data, marker='o', linestyle='-', label=f"Smoothed data")
        plt.plot(x_data, exponential_func(x_data, *popt), linestyle='--', label="Exponential Fit")
        plt.xlabel("Time [s]")
        plt.ylabel("Count")
        plt.title(f"Exponential fit for {nazev_souboru}")
        plt.legend()
        plt.grid()
        plt.show()

if __name__ == "__main__":
    slozka = "data"
    smooth_iteration = 0
    vyhladit_data(slozka, smooth_iteration)

