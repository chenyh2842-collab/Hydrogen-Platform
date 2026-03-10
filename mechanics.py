import numpy as np

def simulate_electrolysis(power_mw, temp_c):
    eff = 82.5 - (0.005 * (temp_c - 65)**2)
    flow = (power_mw * 1000 * (eff/100)) / 33.3
    return round(eff, 2), round(flow, 2)

def get_uhs_physics(depth_m):
    p = depth_m * 0.0105
    t = 15 + (depth_m / 100) * 3
    d = (p * 1e6) / (412.4 * (t + 273.15))
    return round(p, 2), round(t, 2), round(d, 2)

def generate_3d_cavern_mesh():
    z = np.linspace(-120, 0, 40)
    theta = np.linspace(0, 2 * np.pi, 40)
    theta_grid, z_grid = np.meshgrid(theta, z)
    radius = (z_grid + 130) * np.exp(z_grid / 45) * 0.5
    x = radius * np.cos(theta_grid)
    y = radius * np.sin(theta_grid)
    return x, y, z

def get_financial_metrics(capacity, depth):
    # 模拟 CAPEX 随深度和容量的变化
    capex = (capacity * 0.012) + (depth * 0.005)
    savings = capex * 0.35
    return round(capex, 2), round(savings, 2)