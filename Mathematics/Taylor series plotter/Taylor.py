import numpy as np
import matplotlib.pyplot as plt

def Taylor_exp(x, n):
    soucet = 0
    hodnoty = []
    for i in range(n + 1):
        soucet += x**i / np.math.factorial(i)
        hodnoty.append(soucet)
    return hodnoty

def Taylor_sin(x, n):
    soucet = 0
    hodnoty = []
    for i in range(n + 1):
        soucet += ((-1)**i * x**(2*i + 1)) / np.math.factorial(2*i + 1)
        hodnoty.append(soucet)
    return hodnoty

def Taylor_sinh(x, n):
    soucet = 0
    hodnoty = []
    for i in range(n + 1):
        soucet += (1/np.math.factorial(2*i + 1)) * (x**(2*i + 1))
        hodnoty.append(soucet)
    return hodnoty

def Taylor_cosh(x, n):
    soucet = 0
    hodnoty = []
    for i in range(n + 1):
        soucet += (1/np.math.factorial(2*i)) * (x**(2*i))
        hodnoty.append(soucet)
    return hodnoty

def Taylor_sqrt_1_minus_x(x, n):
    soucet = 0
    hodnoty = []
    for i in range(n + 1):
        soucet += ((np.math.factorial(1/2))/((np.math.factorial(i))*(np.math.factorial(1/2 - i))))*((-x)**i)
        hodnoty.append(soucet)
    return hodnoty

x_exp = np.linspace(-1.5, 1.5, 100)
x_sin = np.linspace(-np.pi, np.pi, 100)
x_sinh = np.linspace(-5, 5, 100)
x_cosh = np.linspace(-5, 5, 100)
x_sqrt_1_minus_x = np.linspace(-0.5, 1, 100)

n_max = 4
barvy = ['red', 'blue', 'green', 'orange', 'purple', 'brown']

"""
#e^x
plt.figure()
for n in range(n_max + 1):
    hodnoty_taylor = np.array([Taylor_exp(xi, n)[-1] for xi in x_exp])
    plt.plot(x_exp, hodnoty_taylor, label=f'Taylor exp {n}. řád', color=barvy[n % len(barvy)], linewidth=2)
plt.plot(x_exp, np.exp(x_exp), label='e^x', color='black', linewidth=3)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Taylorova řada pro e^x')
plt.legend()
plt.grid()
plt.savefig('Taylor_funkce_exp.png')

#sin(x)
plt.figure()
for n in range(n_max + 1):
    hodnoty_taylor = np.array([Taylor_sin(xi, n)[-1] for xi in x_sin])
    plt.plot(x_sin, hodnoty_taylor, label=f'Taylor sin {n}. řád', color=barvy[n % len(barvy)], linewidth=2)
plt.plot(x_sin, np.sin(x_sin), label='sin(x)', color='black', linewidth=3)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Taylorova řada pro sin(x)')
plt.legend()
plt.grid()
plt.savefig('Taylor_funkce_sin.png')

#sin(1/x)
plt.figure()
for n in range(n_max + 1):
    hodnoty_taylor = np.array([Taylor_sin(1/xi, n)[-1] if xi != 0 else 0 for xi in x_sin_inv])
    plt.plot(x_sin_inv, hodnoty_taylor, label=f'Taylor sin(1/x) {n}. řád', color=barvy[n % len(barvy)], linewidth=1)
plt.plot(x_sin_inv, np.sin(1/x_sin_inv), label='sin(1/x)', color='black', linewidth=2)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Taylorova řada pro sin(1/x)')
plt.legend()
plt.grid()
plt.savefig('Taylor_funkce_sin_inv.png')

#sin(x)/x
plt.figure()
for n in range(n_max + 1):
    hodnoty_taylor = np.array([Taylor_sin(xi, n)[-1] / xi if xi != 0 else 1 for xi in x_sin_div_x])
    plt.plot(x_sin_div_x, hodnoty_taylor, label=f'Taylor sin(x)/x {n}. řád', color=barvy[n % len(barvy)], linewidth=2)
plt.plot(x_sin_div_x, np.sinc(x_sin_div_x/np.pi), label='sin(x)/x', color='black', linewidth=3)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Taylorova řada pro sin(x)/x')
plt.legend()
plt.grid()
plt.savefig('Taylor_funkce_sin_div_x.png')
"""

# sinh(x)
plt.figure()
for n in range(n_max + 1):
    hodnoty_taylor = np.array([Taylor_sinh(xi, n)[-1] for xi in x_sinh])
    plt.plot(x_sinh, hodnoty_taylor, label=f'Taylor sinh {n}. řád', color=barvy[n % len(barvy)], linewidth=2)
plt.plot(x_sinh, np.sinh(x_sinh), label='sinh(x)', color='black', linewidth=3)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Taylorova řada pro sinh(x)')
plt.legend()
plt.grid()
plt.savefig('Taylor_funkce_sinh.png')

# cosh(x)
plt.figure()
for n in range(n_max + 1):
    hodnoty_taylor = np.array([Taylor_cosh(xi, n)[-1] for xi in x_cosh])
    plt.plot(x_cosh, hodnoty_taylor, label=f'Taylor cosh {n}. řád', color=barvy[n % len(barvy)], linewidth=2)
plt.plot(x_cosh, np.cosh(x_cosh), label='cosh(x)', color='black', linewidth=3)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Taylorova řada pro cosh(x)')
plt.legend()
plt.grid()
plt.savefig('Taylor_funkce_cosh.png')

# sqrt(1 - x)
plt.figure()
for n in range(n_max + 1):
    hodnoty_taylor = np.array([Taylor_sqrt_1_minus_x(xi, n)[-1] for xi in x_sqrt_1_minus_x])
    plt.plot(x_sqrt_1_minus_x, hodnoty_taylor, label=f'Taylor sqrt(1-x) {n}. řád', color=barvy[n % len(barvy)], linewidth=2)
plt.plot(x_sqrt_1_minus_x, np.sqrt(1 - x_sqrt_1_minus_x), label='sqrt(1-x)', color='black', linewidth=3)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Taylorova řada pro sqrt(1-x)')
plt.legend()
plt.grid()
plt.savefig('Taylor_funkce_sqrt_1_minus_x.png')

plt.show()

