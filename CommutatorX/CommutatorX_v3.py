import sympy as sp

# Symbol
x = sp.symbols('x', real=True)
hbar = 1

# Define operators
def position_op(f):
    return x * f

def momentum_op(f):
    return -sp.I * hbar * sp.diff(f, x)

# Generic commutator checker
def check_commutator(A, B, f):
    AB = A(B(f))
    BA = B(A(f))
    comm = sp.simplify(AB - BA)
    return comm

# Test function
psi = sp.sin(x)

# Check [x, p]
result = check_commutator(position_op, momentum_op, psi)

print("Commutator result:", result)

if result == 0:
    print("Operators commute")
else:
    print("Operators do NOT commute")