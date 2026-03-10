import streamlit as st
import mechanics
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# 1. 顶级页面配置
st.set_page_config(page_title="H2 NEBULA | COMMAND v6.0", layout="wide", initial_sidebar_state="collapsed")

# 2. 注入极致赛博 UI (全息投影风格)
st.markdown("""
    <style>
    .main {
        background: radial-gradient(circle at center, #001529 0%, #000206 100%);
        color: #e6f7ff;
    }
    .hero-title {
        font-family: 'Courier New', monospace;
        font-size: 3.5rem;
        font-weight: 900;
        text-align: center;
        letter-spacing: 15px;
        color: #00f2ff;
        text-shadow: 0 0 15px #00f2ff, 0 0 30px #0055ff, -2px 0 #ff00de, 2px 0 #00ff00;
        margin-top: 20px;
        animation: glitch 1.5s infinite linear;
    }
    @keyframes glitch {
        0% { transform: skew(0deg); }
        20% { transform: skew(1deg); }
        60% { transform: skew(-0.5deg); }
        100% { transform: skew(0deg); }
    }
    [data-testid="stMetric"], .stPlotlyChart {
        background: rgba(0, 242, 255, 0.05) !important;
        border: 1px solid rgba(0, 242, 255, 0.3) !important;
        backdrop-filter: blur(15px);
        border-radius: 15px !important;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 稳健的 3D 全球能源地图
def render_cyber_world_map():
    locations = pd.DataFrame({
        'City': ['Beijing', 'Houston', 'London', 'Dubai', 'Singapore', 'Berlin'],
        'lat': [39.9, 29.7, 51.5, 25.2, 1.3, 52.5],
        'lon': [116.4, -95.3, -0.1, 55.3, 103.8, 13.4]
    })
    fig = go.Figure()
    # 添加能源节点
    fig.add_trace(go.Scattergeo(
        lon = locations['lon'], lat = locations['lat'],
        mode = 'markers+lines',
        marker = dict(size = 10, color = '#ff00de', line=dict(width=2, color='#00f2ff')),
        line = dict(width = 1, color = 'rgba(0, 242, 255, 0.2)')
    ))
    fig.update_geos(
        projection_type="orthographic",
        showcoastlines=True, coastlinecolor="rgba(0, 242, 255, 0.3)",
        showland=True, landcolor="#000811",
        bgcolor='rgba(0,0,0,0)'
    )
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', margin=dict(l=0, r=0, b=0, t=0), showlegend=False)
    return fig

# 4. 主界面逻辑
if 'lang' not in st.session_state: st.session_state.lang = "English"
lang = st.session_state.lang

# 侧边栏
with st.sidebar:
    st.title("🛡️ COMMAND")
    if st.button("🌐 SWITCH LANGUAGE"):
        st.session_state.lang = "中文" if lang == "English" else "English"
        st.rerun() # 修正：使用 st.rerun() 替代旧版
    st.code(">> SYSTEM ONLINE\n>> NODES SYNCED", language="bash")

# 标题区
title_text = "H2 GLOBAL COMMAND" if lang == "English" else "氢能全球指挥终端"
st.markdown(f'<p class="hero-title">{title_text}</p>', unsafe_allow_html=True)

# 布局：大屏大矩阵
st.write("---")

# 第一行：全球视野 + 核心监控
c_left, c_mid, c_right = st.columns([1, 2, 1])

with c_left:
    st.markdown("### 💠 Network")
    st.metric("SYNC STATUS", "ACTIVE", "GLOBAL")
    st.metric("CORE TEMP", "1.2 MK", "STABLE")

with c_mid:
    # 核心 3D 地球
    st.plotly_chart(render_cyber_world_map(), use_container_width=True, config={'displayModeBar': False})

with c_right:
    st.markdown("### ⚡ Pulse")
    st.metric("H2 SUPPLY", "2.4M TONS", "+5.2%")
    st.metric("NODES", "154 ACTIVE", "LIVE")

# 第二行：机理模拟 (填充空位)
st.write("---")
c_up, c_mid_sub, c_econ = st.columns(3)

with c_up:
    st.markdown("#### 🧪 Production")
    pw = st.slider("Power (MW)", 1, 100, 25)
    eff, flow = mechanics.simulate_electrolysis(pw, 65) # 适配 mechanics 接口
    st.metric("Efficiency", f"{eff}%")
    st.write(f"Flow Rate: `{flow} kg/h`")

with c_mid_sub:
    st.markdown("#### 🛡️ Storage Scan")
    depth = st.slider("Depth (m)", 500, 3000, 1200)
    p, t, d = mechanics.get_uhs_physics(depth)
    st.write(f"Pressure: `{p} MPa` | Density: `{d} kg/m³`")
    # 迷你 3D 盐穴
    X, Y, Z = mechanics.generate_3d_cavern_mesh()
    fig_c = go.Figure(data=[go.Surface(x=X, y=Y, z=Z, colorscale='Electric', showscale=False)])
    fig_c.update_layout(height=200, margin=dict(l=0,r=0,b=0,t=0), paper_bgcolor='rgba(0,0,0,0)', scene=dict(xaxis_visible=False, yaxis_visible=False))
    st.plotly_chart(fig_c, use_container_width=True)

with c_econ:
    st.markdown("#### 💰 Strategic")
    capex, savings = mechanics.get_financial_metrics(10000, 1200)
    st.metric("CAPEX", f"${capex}M")
    st.progress(85)
    st.caption("Feasibility: HIGH")

st.markdown("---")
st.caption("© 2026 FUTURE ENERGY LAB | ACCESS ID: CNPC-ULTRA-SECURE")