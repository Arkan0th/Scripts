import numpy as np
import matplotlib.pyplot as plt
import os
import sys

def f_per(x):
    return ((x + np.pi) % (2 * np.pi)) - np.pi

def fourier_terms(x, k):
    terms = []
    for n in range(1, k + 1):
        bn = 2 * (-1) ** (n + 1) / n
        term = bn * np.sin(n * x)
        terms.append((n, term))
    return terms

def fourier_sum(terms):
    return np.sum([term for _, term in terms], axis=0)

def plot_fourier_series(k, points=1000, save_path=None):
    x = np.linspace(-2 * np.pi, 2 * np.pi, points)
    f_true = f_per(x)
    terms = fourier_terms(x, k)
    f_approx = fourier_sum(terms)

    plt.figure(figsize=(16, 9), dpi=50)  # Set figure size to 16:9 ratio and dpi for 800x450 resolution
    plt.plot(x, f_true, label='f(x) = x', color='black', linewidth=2)
    
    for n, term in terms:
        plt.plot(x, term, linestyle=':', alpha=0.5)
    
    plt.plot(x, f_approx, label=f'Součet {k} členů', color='blue', linestyle='--', linewidth=2)
    
    plt.xticks(ticks=np.pi * np.arange(-2, 3), labels=[r'$-2\pi$', r'$-\pi$', r'$0$', r'$\pi$', r'$2\pi$'], fontsize=20)
    plt.yticks(ticks=np.pi * np.arange(-1, 2), labels=[r'$-\pi$', r'$0$', r'$\pi$'], fontsize=20)

    plt.xlabel('x', fontsize=24)
    plt.ylabel('f(x)', fontsize=24)
    plt.title(f'Fourierova řada f(x) = x, k = {k}', fontsize=26)
    plt.grid(True)
    plt.axhline(0, color='gray', linewidth=0.5)
    plt.axvline(0, color='gray', linewidth=0.5)
    plt.legend(loc='upper left', fontsize=20)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=50)  # Ensure saved image is 800x450 resolution
        plt.close()
    else:
        plt.show()

def print_progress_bar(iteration, total, prefix='', length=10):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = '█' * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% Complete')
    sys.stdout.flush()
    if iteration == total:
        sys.stdout.write(f'\r{prefix} |{bar}| {percent}% Complete\n')
        sys.stdout.flush()

def generate_fourier_animation(max_k=50, step=1, save_dir="frames_fourier"):
    os.makedirs(save_dir, exist_ok=True)
    total_steps = (max_k - 1) // step + 1
    
    for i, k in enumerate(range(1, max_k + 1, step), start=1):
        save_path = os.path.join(save_dir, f"fourier_k{k:03d}.jpg")
        plot_fourier_series(k, save_path=save_path)
        print_progress_bar(i, total_steps, prefix="Generating Fourier frames")

if __name__ == "__main__":
    max_k = int(input("Enter max number of Fourier terms k: "))
    step = 1
    generate_fourier_animation(max_k=max_k, step=step)

