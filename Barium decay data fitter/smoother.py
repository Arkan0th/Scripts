import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def exponential_func(x, a, b, c):
    return a * np.exp(b * x) + c

def aplikovat_vyhlazeni(data, smooth_iteration):
    for _ in range(smooth_iteration):
        vyhlazena_data = []
        i = 0
        while i < len(data):
            if i == len(data) - 1:
                vyhlazena_data.append(int(data[i]))  # Keep single last point as is
            else:
                vyhlazena_data.append(int(data[i + 1]))  # Take the second value in the pair
            i += 2  # Move in steps of 2
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
                continue  # Skip invalid lines
        
        if not data:
            print(f"Přeskakuji {nazev_souboru}, nedostatek datových bodů.")
            continue
        
        smoothed_data = aplikovat_vyhlazeni(data, smooth_iteration)
        
        novy_nazev = f"{nazev_souboru}_smooth"
        nova_cesta = os.path.join(slozka, novy_nazev)
        
        with open(nova_cesta, 'w') as novy_soubor:
            for value in smoothed_data:
                novy_soubor.write(f"{str(value)}\n")
        
        print(f"Zpracováno {nazev_souboru} -> {novy_nazev}")
        
        x_data = np.arange(len(smoothed_data))
        y_data = np.array(smoothed_data)
        
        try:
            # Set parameter bounds to avoid overflow issues
            popt, _ = curve_fit(exponential_func, x_data, y_data, p0=(1, -0.1, 1), bounds=([0, -np.inf, -np.inf], [np.inf, 0, np.inf]))
            print(f"{nazev_souboru} exponential fit parameters: a={popt[0]:.4f}, b={popt[1]:.4f}, c={popt[2]:.4f}")
            
            plt.figure()
            plt.plot(x_data, smoothed_data, marker='o', linestyle='-', label=f"Smoothed data")
            plt.plot(x_data, exponential_func(x_data, *popt), linestyle='--', label="Exponential Fit")
            plt.xlabel("Time/smooth_iteration")
            plt.ylabel("Count")
            plt.title(f"Smoothing and exponential fit for {nazev_souboru}")
            plt.legend()
            plt.grid()
            plt.show()
        except (RuntimeError, OverflowError, ValueError) as e:
            print(f"Could not fit exponential function for {nazev_souboru}: {e}")

if __name__ == "__main__":
    slozka = "data"  # Ensure this is relative to the current working directory
    smooth_iteration = 2  # Number of times to apply smoothing
    vyhladit_data(slozka, smooth_iteration)

