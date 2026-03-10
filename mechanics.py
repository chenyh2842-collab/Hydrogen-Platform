import numpy as np


# --- 1. 上游：制氢机理仿真 ---
def simulate_electrolysis(power_mw, tech_type, temp_c):
    # ALK: Alkaline, PEM: Proton Exchange Membrane, SOEC: Solid Oxide Electrolyzer Cell
    efficiency_base = 0.68 if tech_type == "ALK" else 0.82 if tech_type == "PEM" else 0.90

    # Efficiency curve: Peak at 65°C for ALK/PEM
    temp_effect = -0.00015 * (temp_c - 65) ** 2

    final_eff = max(0.4, efficiency_base + temp_effect)

    # Ideal to Mass: 33.3 kWh per kg H2
    h2_output_kg_h = (power_mw * 1000 * final_eff) / 33.3

    return round(final_eff * 100, 2), round(h2_output_kg_h, 2)


# --- 2. 中游：地下储氢 (UHS) 物理 ---
def get_uhs_physics(depth_m):
    # Hydrostatic pressure and Geothermal gradient simulation
    pressure_mpa = depth_m * 0.0105
    temp_c = 15 + (depth_m / 100) * 3
    # Hydrogen gas density (simplified)
    density_kg_m3 = (pressure_mpa * 1e6) / (412.4 * (temp_c + 273.15))

    return round(pressure_mpa, 2), round(temp_c, 2), round(density_kg_m3, 2)


# --- 3. 3D 储层几何建模 (梨形网格) ---
def generate_3d_cavern_mesh():
    z = np.linspace(-120, 0, 50)
    theta = np.linspace(0, 2 * np.pi, 50)
    theta_grid, z_grid = np.meshgrid(theta, z)

    # Professional Pear-shape mathematical model
    # Radius expands at bottom and narrows at the neck
    radius = (z_grid + 125) * np.exp(z_grid / 45) * 0.6

    x = radius * np.cos(theta_grid)
    y = radius * np.sin(theta_grid)
    return x, y, z


# --- 4. 下游：管道输配物理 ---
def calculate_pipe_flow(inlet_p_mpa, length_km, diameter_mm):
    # Simplified pressure drop simulation
    p_drop = (length_km * 0.08) / (diameter_mm / 150)
    outlet_p = max(0.1, inlet_p_mpa - p_drop)
    # Risk score mechanism based on pressure and distance
    risk_score = (inlet_p_mpa * 1.5) + (length_km * 0.1)
    return round(outlet_p, 2), min(100, round(risk_score, 1))


# --- 5. 经济性与财务评估模型 ---
def get_financial_metrics(capacity_tons, depth_m):
    # Mechanics: UHS capex calculation (Cavern vs Surface Tank)
    # UHS capex decreases with burial depth efficiency
    cavern_capex = (capacity_tons * 2500) / (depth_m ** 0.1)
    # Tank capex is standard and higher for large capacity
    tank_capex = capacity_tons * 12000

    roi_years = cavern_capex / (capacity_tons * 800)  # Simple ROI based on storage fees
    return round(cavern_capex / 1e6, 2), round(roi_years, 1)