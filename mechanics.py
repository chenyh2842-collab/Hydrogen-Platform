# 这是一个简单的物理机理：计算不同深度的地层压力
def get_pressure(depth):
    # 压力 (MPa) ≈ 深度 (m) * 0.01 (这是一个粗略的地球物理常数)
    return depth * 0.01

# 计算在该压力下的氢气理论体积（简化版）
def get_volume(p, initial_v):
    return initial_v / p