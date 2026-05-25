import numpy as np
import matplotlib.pyplot as plt

def simulate_decoherence():
    # --- Constants (SI Units) ---
    c = 299792458              # Speed of light
    h_bar = 1.0545718e-34      # Reduced Planck constant
    e_charge = 1.6021766e-19   # Elementary charge
    m_e = 9.1093835e-31        # Mass of electron
    sigma_th = 6.652e-29       # Thomson cross-section (m^2)
    kb = 1.380649e-23          # Boltzmann constant
    T_cmb = 2.725              # CMB Temperature (K)
    
    # --- Interstellar Medium (ISM) Properties ---
    # Average density: 1 atom per cm^3 -> 1e6 per m^3
    n_ism = 1.0e6              
    # Cross section for photon-atom scattering (Rayleigh/Thomson approx)
    sigma_photon = 1e-30       
    
    # --- Time and Distance Scale ---
    # 100,000 light years (Galaxy width)
    distance_ly = 100000
    total_distance = distance_ly * 9.461e15 
    num_steps = 1000
    x = np.linspace(0, total_distance, num_steps)
    
    # --- 1. Photon Decoherence ---
    # Rate Gamma = n * sigma * c
    gamma_photon = n_ism * sigma_photon * c
    # Coherence P(t) = exp(-gamma * t)
    coherence_photon = np.exp(-gamma_photon * (x / c))

    # --- 2. Electron Decoherence ---
    # Electron velocity (assume 0.1c for high speed but non-relativistic)
    v_e = 0.1 * c
    
    # Gamma_e = Gamma_CMB + Gamma_ISM_Collisions
    # CMB interaction is a massive factor for charged particles
    gamma_cmb = (sigma_th * (kb * T_cmb)**4) / (h_bar**3 * c**2) 
    # Interaction with ions in ISM (Coulomb decoherence)
    gamma_coulomb = n_ism * (e_charge**2 / (m_e * v_e)) # Simplified scaling
    
    gamma_electron = gamma_cmb + gamma_coulomb
    coherence_electron = np.exp(-gamma_electron * (x / v_e))

    # --- Plotting ---
    plt.figure(figsize=(10, 6))
    plt.plot(x / 9.461e15, coherence_photon, label='Photon (Massless/Neutral)', color='gold', lw=2)
    plt.plot(x / 9.461e15, coherence_electron, label='Electron (Massive/Charged)', color='cyan', lw=2)
    
    plt.yscale('log')
    plt.xlabel('Distance (Light Years)')
    plt.ylabel('Coherence Probability (Log Scale)')
    plt.title('Decoherence: Photon vs. Electron across the Galaxy')
    plt.legend()
    plt.grid(True, which="both", ls="-", alpha=0.5)
    
    print(f"Final Photon Coherence: {coherence_photon[-1]:.4f}")
    print(f"Final Electron Coherence: {coherence_electron[-1]:.4e}")
    plt.show()

if __name__ == "__main__":
    simulate_decoherence()