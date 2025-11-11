import random
import math
import matplotlib.pyplot as plt
import time

def f(x):
    if abs(x) < 1e-12:  #lim ošetření
        return math.e
    return math.exp(math.sin(x) / x)

#parametry pro "hezký" histogram
a, b = -15, 15
n_bins = (b-a)*10
n_samples = n_bins*1000
f_max = math.e

def von_neumann_sampling(f, a, b, f_max, n_samples):
    samples_x = []
    while len(samples_x) < n_samples:
        x = random.uniform(a, b)
        y = random.uniform(0, f_max)
        if y <= f(x):
            samples_x.append(x)
    return samples_x

start_time = time.time()

samples_x = von_neumann_sampling(f, a, b, f_max, n_samples)

plt.figure(figsize=(10,5))
counts, bins, _ = plt.hist(samples_x, bins=n_bins, density=True, color='blue', alpha=0.7,
                            label=f'Odhad hustoty pravděpodobnosti ({n_samples} bodů, {n_bins} binů)')

#true f(x) normalizovaná
xs = [min(samples_x) + i*(max(samples_x)-min(samples_x))/1000 for i in range(1001)]
f_vals = [f(x) for x in xs]
area = sum(f_vals) * (max(samples_x)-min(samples_x))/1000
f_norm = [v/area for v in f_vals]
plt.plot(xs, f_norm, 'r-', linewidth=2, label='f(x) normalizované na hustotu')

plt.title("Von Neumannova metoda – odhad hustoty pravděpodobnosti")
plt.xlabel("x")
plt.ylabel("Hustota pravděpodobnosti")
plt.legend()
plt.grid(alpha=0.3)

end_time = time.time()
print(f"Celková doba běhu (včetně vykreslení) byla {end_time - start_time:.2f} sekund")

plt.show()
