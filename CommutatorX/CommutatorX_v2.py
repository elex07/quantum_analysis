import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Symbol
x = sp.symbols('x', real=True)
hbar = 1

# Wavefunction
psi = sp.sin(x)

# Operators
def position_op(f):
    return x * f

def momentum_op(f):
    return -sp.I * hbar * sp.diff(f, x)

# Apply operators
psi_x = position_op(psi)
psi_p = momentum_op(psi)

# Convert to numerical functions
f_psi = sp.lambdify(x, psi, 'numpy')
f_x = sp.lambdify(x, psi_x, 'numpy')

# Momentum is imaginary -> use imaginary part
f_p = sp.lambdify(x, sp.im(psi_p), 'numpy')

# Domain
x_vals = np.linspace(-5, 5, 400)

# Plot
plt.figure(figsize=(10,6))

plt.plot(x_vals, f_psi(x_vals), label="ψ(x) = sin(x)")
plt.plot(x_vals, f_x(x_vals), label="x·ψ(x)")
plt.plot(x_vals, f_p(x_vals), label="Im[pψ(x)]")

plt.legend()
plt.xlabel("x")
plt.ylabel("Value")
plt.title("Effect of Operators on Wavefunction")

plt.grid(True)

plt.show()