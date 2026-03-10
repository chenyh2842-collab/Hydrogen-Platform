import numpy as np


# --- UPSTREAM: GREEN HYDROGEN PRODUCTION ---
def simulate_electrolysis(power_mw, tech_type, temp_c):
    """
    Mechanics: Efficiency varies with temperature and technology.
    ALK: Alkaline, PEM: Proton Exchange Membrane
    """
    # Efficiency curve: Peak at 65°C
    efficiency_base = 0.68 if tech_type == "ALK" else 0.82
    temp_effect = -0.00015 * (temp_c - 65) ** 2
    final_eff = max(0.4, efficiency_base + temp_effect)

    # Energy to Mass: 33.3 kWh per kg H2 (Ideal)
    h2_output_kg_h = (power_mw * 1000 * final_eff) / 33.3
    return round(final_eff * 100, 2), round(h2_output_kg_h, 2)


# --- MIDSTREAM: UNDERGROUND HYDROGEN STORAGE (UHS) ---
def get_uhs_physics(depth_m):
    """
    Mechanics: Hydrostatic pressure and Geothermal gradient
    """
    pressure_mpa = depth_m * 0.0105  # Standard hydrostatic
    temp_c = 15 + (depth_m / 100) * 3  # Geothermal gradient
    density_kg_m3 = (pressure_mpa * 1e6) / (412.4 * (temp_c + 273.15))  # Simplified gas law
    return round(pressure_mpa, 2), round(temp_c, 2), round(density_kg_m3, 2)


def generate_3d_cavern_mesh():
    """
    Mechanics: Generates a professional Pear-shaped salt cavern geometry
    """
    z = np.linspace(-120, 0, 60)
    theta = np.linspace(0, 2 * np.pi, 60)
    theta_grid, z_grid = np.meshgrid(theta, z)

    # Pear-shape mathematical model
    # Radius expands at bottom and narrows at the neck
    radius = (z_grid + 125) * np.exp(z_grid / 40) * 0.55

    x = radius * np.cos(theta_grid)
    y = radius * np.sin(theta_grid)
    return x, y, z


# --- DOWNSTREAM: LOGISTICS & RISK ---
def calculate_pipe_flow(inlet_p, length_km, diameter_mm):
    """
    Mechanics: Pressure drop in hydrogen pipelines
    """
    drop = (length_km * 0.08) / (diameter_mm / 150)
    outlet_p = max(0.1, inlet_p - drop)
    risk_score = (inlet_p * 1.5) + (length_km * 0.1)
    return round(outlet_p, 2), min(100, round(risk_score, 1))


# --- ECONOMICS: CAPEX & ROI ---
def get_financial_metrics(capacity_tons, depth):
    """
    Mechanics: Comparison between Salt Cavern and Surface Tanks
    """
    # Cavern cost decreases with depth-to-volume efficiency
    cavern_capex = (capacity_tons * 2500) / (depth ** 0.1)
    tank_capex = capacity_tons * 12000  # Surface tanks are much pricier

    savings = (tank_capex - cavern_capex) / 1e6  # Million USD
    roi_years = cavern_capex / (capacity_tons * 800)  # Simple ROI based on storage fees
    return round(cavern_capex / 1e6, 2), round(savings, 2), round(roi_years, 1)