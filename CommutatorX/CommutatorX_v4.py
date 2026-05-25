import sympy as sp

x = sp.symbols('x', real=True)
hbar = 1
m = 1

# Generic operator wrapper
class Operator:
    def __init__(self, func, name=""):
        self.func = func
        self.name = name

    def __call__(self, f):
        return self.func(f)

# Define operators
X = Operator(lambda f: x * f, "x")
P = Operator(lambda f: -sp.I * hbar * sp.diff(f, x), "p")

# Example potential
V = x**2  # harmonic oscillator

H = Operator(lambda f: -(hbar**2/(2*m)) * sp.diff(f, x, 2) + V*f, "H")

# Commutator function
def commutator(A, B, f):
    return sp.simplify(A(B(f)) - B(A(f)))

# Test function
psi = sp.sin(x)

# Test different pairs
print("[x, p]:", commutator(X, P, psi))
print("[H, x]:", commutator(H, X, psi))
print("[H, p]:", commutator(H, P, psi))