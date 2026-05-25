import sympy as sp

# Define symbol
x = sp.symbols('x', real=True)
hbar = 1  # set ħ = 1 for simplicity

# Define wavefunction
psi = sp.sin(x)

# Define operators
def position_op(f):
    return x * f

def momentum_op(f):
    return -sp.I * hbar * sp.diff(f, x)

# Apply operators
xp_psi = position_op(momentum_op(psi))
px_psi = momentum_op(position_op(psi))

# Compute commutator
commutator = xp_psi - px_psi

# Simplify results
xp_psi_s = sp.simplify(xp_psi)
px_psi_s = sp.simplify(px_psi)
comm_s = sp.simplify(commutator)

# Print results
print("ψ(x) =", psi)
print("\nxp ψ =", xp_psi_s)
print("\npx ψ =", px_psi_s)
print("\n[x, p] ψ =", comm_s)