import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import time

def wave_function(x, t, m=1, hbar=1):
    prefaktor = ((2 / np.pi)**(1/4)) * (np.sqrt(m / (2j * hbar * t + m)))
    exponent = np.exp((-m * x**2) / (2j * hbar * t + m))
    return prefaktor * exponent

def plot_wave_function(t, points=1000, m=1, hbar=1, save_path=None):
    x_range = (-4 * t - 3, 4 * t + 3)  # Dynamic x_range based on t
    x = np.linspace(x_range[0], x_range[1], points)
    psi = wave_function(x, t, m, hbar)
    
    plt.figure(figsize=(8, 5))
    plt.plot(x, np.real(psi), label='Re(Ψ)')
    plt.plot(x, np.imag(psi), label='Im(Ψ)')
    plt.plot(x, np.abs(psi), label='Amplitude', linestyle='dashed')
    
    plt.ylim(-0.5, 1)  # Set Y-axis range
    
    plt.title(f'Wave function Ψ(x, t={t})')
    plt.xlabel('x')
    plt.ylabel('Ψ(x, t)')
    plt.legend()
    plt.grid()
    
    plt.savefig(save_path)
    plt.close()

def print_progress_bar(iteration, total, prefix='', length=10):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = '█' * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% Complete')
    sys.stdout.flush()
    
    # When complete, print a new line to signal completion
    if iteration == total:
        sys.stdout.write(f'\r{prefix} |{bar}| {percent}% Complete\n')
        sys.stdout.flush()


def generate_wave_animation_soft(max_t_soft, save_dir="frames"):
    os.makedirs(save_dir, exist_ok=True)
    for i in range(max_t_soft):
        t = (i / max_t_soft) * 2  # Scale t from 0 to 2
        save_path = os.path.join(save_dir, f"wave_t{t:.2f}.png")
        plot_wave_function(t, save_path=save_path)
        
        print_progress_bar(i + 1, max_t_soft, prefix="Generating soft wave functions")


def generate_wave_animation(max_t, step=1, save_dir="frames"):
    os.makedirs(save_dir, exist_ok=True)
    for t in range(2, max_t + 1, step):
        save_path = os.path.join(save_dir, f"wave_t{t}.png")
        plot_wave_function(t, save_path=save_path)
        
        print_progress_bar(t, max_t, prefix="Generating full wave functions")

# User input for max time values
max_t_soft = int(input("Enter max time soft value (number of frames from t=0 to t=2): "))
max_t = int(input("Enter max time value: "))

generate_wave_animation_soft(max_t_soft)
generate_wave_animation(max_t)

