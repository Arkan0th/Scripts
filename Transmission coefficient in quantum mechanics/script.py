import numpy as np
import matplotlib.pyplot as plt

hbar = 1.0
m = 1.0
E = np.linspace(0.01, 4.0, 1000)

#λ = sqrt(2mU0)*a/ħ
lambdas = [1, 2, 3, 4, 5]

plt.figure(figsize=(8, 5))

for lam in lambdas:
    T = []
    for Ei in E:
        if Ei < 1:  # E < U0
            kappa_a = lam * np.sqrt(1 - Ei)
            T_val = 1 / (1 + np.sinh(kappa_a)**2 / (4 * Ei * (1 - Ei)))
        else:       # E > U0
            k2a = lam * np.sqrt(Ei - 1)
            T_val = 1 / (1 + np.sin(k2a)**2 / (4 * Ei * (Ei - 1)))
        T.append(T_val)
    
    plt.plot(E, T, label=f'$\\sqrt{{2mU_0}}a/\\hbar = {lam}$')

plt.axvline(x=1, color='gray', linestyle='--', label='$E = U_0$')
plt.xlabel('Energy $E/U_0$')
plt.ylabel('Transmission ceofficient $T$')
plt.title('Probability of the wave transmitting through the potential barrier')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("Transmission ceofficient.png", dpi=300)
plt.show()

