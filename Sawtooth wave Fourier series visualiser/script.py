import numpy as np
import matplotlib.pyplot as plt

k = 10
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

def f_per(x):
    return ((x + np.pi) % (2 * np.pi)) - np.pi

def fourier(x, k):
    terms = []
    for n in range(1, k + 1):
        bn = 2 * (-1) ** (n + 1) / n
        term = bn * np.sin(n * x)
        terms.append((n, term))
    return terms

def fourier_suma(terms):
    return np.sum([term for _, term in terms], axis=0)

f_true = f_per(x)
terms = fourier(x, k)
f_approx = fourier_suma(terms)

plt.figure(figsize=(16, 9), dpi=100)
plt.plot(x, f_true, label='f(x) = x', color='black', linewidth=2)
for n, term in terms:
    plt.plot(x, term, linestyle=':', label=f'Term {n}: $\\frac{{2(-1)^{{{n+1}}}}}{{{n}}} \\sin({n}x)$')
plt.plot(x, f_approx, label=f'Sum of {k} terms', color='blue', linestyle='--', linewidth=2)

plt.xticks(ticks=np.pi * np.arange(-2, 3), labels=[r'$-2\pi$', r'$-\pi$', r'$0$', r'$\pi$', r'$2\pi$'])
plt.yticks(ticks=np.pi * np.arange(-1, 2), labels=[r'$-\pi$', r'$0$', r'$\pi$'])
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title(f'Fourier series of f(x) = x, k = {k}')
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.grid(True)
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig("Fourier_plot.png", dpi=100)
plt.show()
