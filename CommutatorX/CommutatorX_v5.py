import sympy as sp

# -----------------------------------
# Symbols
# -----------------------------------

x = sp.symbols('x', real=True)

hbar = 1
m = 1

# Define potential
V = x**2

# Test wavefunction
psi = sp.sin(x)

# -----------------------------------
# Operator Definitions
# -----------------------------------

OPERATORS = {

    "x": lambda f:
        x * f,

    "p": lambda f:
        -sp.I * hbar * sp.diff(f, x),

    "KE": lambda f:
        -(hbar**2 / (2*m)) * sp.diff(f, x, 2),

    "PE": lambda f:
        V * f,

    "H": lambda f:
        -(hbar**2 / (2*m)) * sp.diff(f, x, 2)
        + V * f,

    "F": lambda f:
        (-sp.diff(V, x)) * f
}

# -----------------------------------
# Commutator Function
# -----------------------------------

def commutator(A, B, f):

    AB = A(B(f))
    BA = B(A(f))

    return sp.simplify(AB - BA)

# -----------------------------------
# Show Available Operators
# -----------------------------------

print("\nAvailable Operators:\n")

for name in OPERATORS:
    print("-", name)

# -----------------------------------
# User Input
# -----------------------------------

A_name = input("\nEnter Operator A: ")
B_name = input("Enter Operator B: ")

# -----------------------------------
# Validation
# -----------------------------------

if A_name not in OPERATORS:
    print("\nInvalid Operator A")
    exit()

if B_name not in OPERATORS:
    print("\nInvalid Operator B")
    exit()

# -----------------------------------
# Get Operators
# -----------------------------------

A = OPERATORS[A_name]
B = OPERATORS[B_name]

# -----------------------------------
# Compute Commutator
# -----------------------------------

result = commutator(A, B, psi)

# -----------------------------------
# Display Result
# -----------------------------------

print("\nWavefunction:")
sp.pprint(psi)

print("\nCommutator Result:")
sp.pprint(result)

# -----------------------------------
# Check Commutation
# -----------------------------------

if sp.simplify(result) == 0:

    print("\nOperators COMMUTE")

else:

    print("\nOperators DO NOT commute")