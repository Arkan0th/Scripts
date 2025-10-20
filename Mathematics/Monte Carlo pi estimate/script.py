import numpy as np
import matplotlib.pyplot as plt
import time

#funkce
def monte_carlo_pi(N):
    x = np.random.random(N)
    y = np.random.random(N)
    inside_circle = x**2 + y**2 <= 1
    return 4 * np.sum(inside_circle) / N

#parametry
k = 100  #opakování
interval_start = 0  #start 10^n
interval_end = 6    #konec 10^n
points_per_interval = 10    #body na intervalu

#generace N
N_values = []
for n in range(interval_start, interval_end):
    Ns = np.logspace(n, n + 1, points_per_interval, endpoint=False, base=10)
    N_values.extend(Ns.astype(int))
N_values = sorted(set(N_values))

#čas start
start_time = time.time()

#calc
pi_estimates_k = []
pi_means = []
u_Cs = []
summary_results = []

for N in N_values:
    estimates = [monte_carlo_pi(N) for _ in range(k)]
    pi_estimates_k.append(estimates)
    mean_est = np.mean(estimates)

    if k > 1:
        std_dev = np.std(estimates, ddof=1)
    else:
        std_dev = 0.0

    #uC pro 95% gauss
    uc = 2*np.sqrt(std_dev**2 + (4/np.sqrt(N))**2)
    u_Cs.append(uc)
    pi_means.append(mean_est)
    summary_results.append((N, mean_est, uc))

#čas konec
end_time = time.time()
elapsed_time = end_time - start_time

#tabulka v terminálu
print(f"{'N':<15} | {'Odhad π':<15} | {'Kombinovaná nejistota':<25}")
print("-" * 60)
for N, mean_est, uc in summary_results:
    print(f"{N:<15} | {mean_est:<15.6f} | {uc:<25.6f}")

print(f"\nCelkový čas výpočtu: {elapsed_time:.2f} sekund\n")

#plot
plt.figure(figsize=(10, 6))
plt.scatter(N_values, pi_means, color='blue', label='Odhad π')
plt.errorbar(N_values, pi_means, yerr=u_Cs, fmt='o',
             ecolor='red', capsize=3, label='Kombinovaná nejistota')
plt.axhline(np.pi, color='green', linestyle='--', label=f'Skutečná π ≈ {np.pi:.5f}')
plt.xscale('log')
plt.xlabel('Počet náhodných bodů (N)')
plt.ylabel('Odhad π')
plt.title('Monte Carlo simulace odhadu π s kombinovanou nejistotou')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.tight_layout()

plt.savefig("monte_carlo_pi.png", dpi=300)
print("Graf byl uložen jako 'monte_carlo_pi.png'")
plt.show()

#txt data soubor
output_file = "monte_carlo_pi_data.txt"

with open(output_file, 'w') as f:
    f.write(f"# Počet opakování k = {k}\n")
    f.write(f"# Celkový čas výpočtů: {elapsed_time:.2f} sekund\n")
    f.write(f"{'N (počet bodů)':<20}\t{'pi (odhad)':<20}\t{'Kombinovaná nejistota uC':<25}\n")
    for i in range(len(N_values)):
        N = N_values[i]
        mean_est = pi_means[i]
        uc = u_Cs[i]
        f.write(f"{N:<20}\t{mean_est:<20.10f}\t{uc:<25.10f}\n")

    f.write("\n" + "="*50 + "\n")
    f.write("# Odhady π pro jednotlivá opakování\n")

    for i in range(k):
        f.write(f"\nk = {i+1}\n")
        f.write(f"{'N':<20}\t{'pi odhad':<20}\n")
        for j, N in enumerate(N_values):
            f.write(f"{N:<20}\t{pi_estimates_k[j][i]:<20.10f}\n")

print(f"Data byla uložena do souboru: {output_file}")

