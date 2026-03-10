import numpy as np


# --- 上游：制氢机理 ---
def calculate_h2_production(power_mw, tech_type):
    # tech_type: 0 为碱性电解 (ALK), 1 为质子交换膜 (PEM)
    eff = 0.65 if tech_type == 0 else 0.80
    # 1MW 约产生多少 kg/h 氢气 (低热值计算)
    production = (power_mw * 1000 * eff) / 33.3
    return round(production, 2)


# --- 中游：地下储氢 (UHS) 核心机理 ---
def get_storage_mechanics(depth):
    # 1. 地层静压 (MPa)
    pressure = depth * 0.0105
    # 2. 地层温度 (假设地表15度，每百米增温3度)
    temp = 15 + (depth / 100) * 3
    # 3. 理想容量系数 (简化版)
    capacity_factor = pressure / (temp + 273.15)
    return round(pressure, 2), round(temp, 2), round(capacity_factor, 4)


def generate_3d_cavern_data():
    """生成一个专业梨形盐穴的3D网格数据"""
    z = np.linspace(-100, 0, 40)
    theta = np.linspace(0, 2 * np.pi, 40)
    z_grid, theta_grid = np.meshgrid(z, theta)

    # 梨形方程: 半径随深度变化
    r = (z_grid + 100) * np.exp(z_grid / 40) * 0.6
    x = r * np.cos(theta_grid)
    y = r * np.sin(theta_grid)
    return x, y, z


# --- 下游：储运损耗机理 ---
def transport_loss(distance, method):
    # method: 0 为长管拖车, 1 为管道
    rate = 0.005 if method == 0 else 0.001  # 每公里的损耗率
    total_loss = distance * rate
    return round(total_loss, 3)