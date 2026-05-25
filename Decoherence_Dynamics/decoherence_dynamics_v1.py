import numpy as np
import matplotlib.pyplot as plt

def simulate_accurate_coherence():
    # --- Constants (SI Units) ---
    c = 299792458              # Speed of light
    h_bar = 1.0545718e-34      # Reduced Planck constant
    e_charge = 1.6021766e-19   # Elementary charge
    m_e = 9.1093835e-31        # Mass of electron
    sigma_th = 6.652e-29       # Thomson cross-section (m^2)
    kb = 1.380649e-23          # Boltzmann constant
    T_cmb = 2.725              # CMB Temperature (K)
    
    # --- Interstellar Medium (ISM) Density ---
    n_ism = 1.0e6              # 1 atom per cm^3 -> 1e6 per m^3
    
    # --- Distance Scale: 100,000 Light Years ---
    distance_ly = 100000
    total_distance = distance_ly * 9.461e15 
    num_steps = 1000
    x = np.linspace(0, total_distance, num_steps)
    x_ly = x / 9.461e15        # Convert to Light Years for plotting
    
    # --- 1. Accurate Photon Decoherence ---
    # Optical photons have an incredibly tiny scattering cross-section in ISM
    sigma_photon = 1e-35       
    gamma_photon = n_ism * sigma_photon * c
    coherence_photon = np.exp(-gamma_photon * (x / c))

    # --- 2. Accurate Electron Decoherence ---
    v_e = 0.1 * c              # Speed of electron
    # CMB interaction rate
    gamma_cmb = (sigma_th * (kb * T_cmb)**4) / (h_bar**3 * c**2) 
    # Coulomb interaction with background plasma ions
    gamma_coulomb = n_ism * (e_charge**2 / (m_e * v_e)) 
    
    gamma_electron = gamma_cmb + gamma_coulomb
    coherence_electron = np.exp(-gamma_electron * (x / v_e))
    
    # Force absolute zero values to a tiny floor for clean log plotting
    coherence_electron = np.clip(coherence_electron, 1e-20, 1.0)

    # --- Plotting ---
    plt.figure(figsize=(10, 6))
    plt.plot(x_ly, coherence_photon, label='Photon (Massless / Neutral)', color='#FFD700', lw=3)
    plt.plot(x_ly, coherence_electron, label='Electron (Massive / Charged)', color='#00CED1', lw=3, linestyle='--')
    
    # Formatting
    plt.yscale('log')
    plt.ylim(1e-20, 2.0) # Set limits to clearly show top and bottom bounds
    plt.xlabel('Distance Traveled (Light Years)', fontsize=12)
    plt.ylabel('Quantum Coherence Probability (Log Scale)', fontsize=12)
    plt.title('Quantum Coherence Over Cosmic Distances', fontsize=14, fontweight='bold')
    
    # Annotations for clarity
    plt.text(50000, 1.2, 'Photon: Coherence remains perfectly intact (~1.0)', color='#B8860B', fontsize=10, weight='bold')
    plt.text(5000, 1e-18, 'Electron: Instant collapse to 0 due to CMB & Charge', color='#008B8B', fontsize=10, weight='bold')
    
    plt.legend(loc='center right', fontsize=11)
    plt.grid(True, which="both", ls=":", alpha=0.6)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    simulate_accurate_coherence()
