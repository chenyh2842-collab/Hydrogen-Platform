import streamlit as st
import mechanics
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import time

# 1. 顶级页面配置：深色模式、全屏布局、隐藏侧边栏
st.set_page_config(page_title="H2 NEBULA | INTERSTELLAR COMMAND v6.0", layout="wide", initial_sidebar_state="collapsed")

# 2. 注入“星际指挥中心”CSS (极致视觉核心)
st.markdown("""
    <style>
    /* 全局深空背景，加入微弱的星空粒子纹理 */
    .main {
        background-color: #000205;
        background-image: 
            radial-gradient(circle at center, #001529 0%, #000205 100%),
            radial-gradient(1px 1px at 20px 30px, #fff, rgba(0,0,0,0)),
            radial-gradient(1px 1px at 40px 70px, #fff, rgba(0,0,0,0));
        background-size: 100% 100%, 200px 200px, 150px 150px;
        color: #e6f7ff;
    }

    /* 顶部 Glitch 霓虹标题动画 */
    .hero-title {
        font-family: 'Orbitron', 'Segoe UI Light', 'Courier New', monospace;
        font-size: 3.5rem;
        font-weight: 900;
        text-align: center;
        letter-spacing: 15px;
        color: rgba(0, 242, 255, 0.9);
        text-shadow: 
            0 0 15px #00f2ff, 
            0 0 30px #00a2ff,
            -3px 0 #ff00de, 
            3px 0 #00ff00;
        animation: glitch 1s infinite linear;
        margin-top: 30px;
        margin-bottom: 5px;
        text-transform: uppercase;
    }
    @keyframes glitch {
        0% { transform: skew(0deg); }
        20% { transform: skew(2deg); }
        60% { transform: skew(-1deg); }
        100% { transform: skew(0deg); }
    }

    /* 玻璃拟态卡片 3.0：呼吸边框 + 全息模糊 + 悬浮动效 */
    [data-testid="stMetric"], .stPlotlyChart {
        background: rgba(0, 242, 255, 0.04) !important;
        border: 1px solid rgba(0, 242, 255, 0.3) !important;
        backdrop-filter: blur(15px);
        border-radius: 20px !important;
        box-shadow: 0 0 20px rgba(0, 242, 255, 0.1);
        transition: 0.4s ease;
    }
    [data-testid="stMetric"]:hover, .stPlotlyChart:hover {
        transform: translateY(-8px);
        border: 1px solid #00f2ff !important;
        box-shadow: 0 0 50px rgba(0, 242, 255, 0.4);
    }

    /* 系统控制面板全透明 */
    [data-testid="stSidebar"] {
        background-color: rgba(0, 5, 15, 0.95) !important;
        border-right: 1px solid rgba(0, 242, 255, 0.4);
    }

    /* 标题前加科技图标 */
    .css-1offfwp {
        padding-top: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)


# 3. 辅助函数：渲染全球全息能源地图
def render_cyber_world_map():
    locations = pd.DataFrame({
        'City': ['Beijing', 'Houston', 'London', 'Dubai', 'Singapore', 'Berlin', 'São Paulo', 'Sydney'],
        'lat': [39.9, 29.7, 51.5, 25.2, 1.3, 52.5, -23.5, -33.8],
        'lon': [116.4, -95.3, -0.1, 55.3, 103.8, 13.4, -46.6, 151.2],
        'Output_GW': [1.4, 0.9, 0.7, 1.2, 0.5, 0.8, 0.6, 0.7]
    })

    fig = go.Figure()

    # 全球连接流线 (模拟氢能输送网络)
    for i in range(len(locations) - 1):
        for j in range(i + 1, len(locations)):
            if np.random.rand() > 0.6:  # 随机生成连接
                fig.add_trace(go.Scattergeo(
                    locationmode='ISO-3',
                    lon=[locations['lon'][i], locations['lon'][j]],
                    lat=[locations['lat'][i], locations['lat'][j]],
                    mode='lines',
                    line=dict(width=1.2, color='#00f2ff'),
                    opacity=0.25,
                ))

    # 能源节点发光点 (根据 Output 大小)
    fig.add_trace(go.Scattergeo(
        lon=locations['lon'],
        lat=locations['lat'],
        text=locations['City'],
        mode='markers',
        marker=dict(
            size=locations['Output_GW'] * 15,
            color='#ff00de',
            symbol='circle',
            line=dict(width=2, color='#00f2ff'),
            opacity=0.8
        )
    ))

    # 地图视觉样式 (正交投影球体 + 赛博朋克深蓝海洋)
    fig.update_geos(
        projection_type="orthographic",
        showcoastlines=True, coastlinecolor="rgba(0, 242, 255, 0.25)",
        showland=True, landcolor="#000811",
        showocean=True, oceancolor="#000206",
        showcountries=True, countrycolor="rgba(0, 242, 255, 0.15)",
        bgcolor='rgba(0,0,0,0)'
    )

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0, r=0, b=0, t=0),
        showlegend=False
    )
    return fig


# 4. 初始化状态
if 'lang' not in st.session_state: st.session_state.lang = "English"
lang = st.session_state.lang

# 5. 侧边栏：系统控制中心
with st.sidebar:
    st.markdown("### `COMMAND CONTROL v6.0`")
    if st.button("🌐 SWITCH LANGUAGE"):
        st.session_state.lang = "中文" if lang == "English" else "English"
        st.experimental_rerun()

    st.divider()
    # 模拟系统日志瀑布流
    st.code(">> INITIALIZING QUANTUM LINK\n>> SCANNING GEO-STORAGE\n>> ID: CNPC-ULTRA-2050\n>> SYNCING NODES...",
            language="bash")
    st.caption("NEURAL-NET STATUS: ONLINE")
    st.divider()
    st.info("System is monitoring global hydrogen network. Secure links active.")

# 6. 主页面：星际指挥中心全景

# 顶部 Glitch 大标题
title_text = "H2 NEBULA GLOBAL COMMAND" if lang == "English" else "氢能全球指挥终端"
st.markdown(f'<p class="hero-title">{title_text}</p>', unsafe_allow_html=True)
st.caption(
    "<p style='text-align: center; color: #00f2ff; opacity: 0.6;'>System ID: NX-Series Terminal | Quantum Simulation Active</p>",
    unsafe_allow_html=True)

# 核心布局：3x2 矩阵 (顶部是地图，周围包围板块)

st.write("---")

# **第1行：全球地图 + 核心监控**
# 采用 1:2:1 布局，地图占大头，两边放指标
c_map_l, c_map_c, c_map_r = st.columns([1, 2.5, 1])

with c_map_l:
    # 板块 1: 全球纯度 & 实时储量
    st.write("#### 🛡️ Global Nexus Stats")
    m1, m2 = st.columns(2)
    m1.metric("NETWORK STATUS", "ENCRYPTED", "STABLE")
    m2.metric("SYNC RATE", "99.8%", "LIVE")
    m3, m4 = st.columns(2)
    m3.metric("CORE TEMP", "1.2 MK", "OPTIMAL")
    m4.metric("PURITY", "99.9998%", "MAX")

with c_map_c:
    # 核心：全息旋转地球地图 (视觉重心)
    st.plotly_chart(render_cyber_world_map(), use_container_width=True, config={'displayModeBar': False})

with c_map_r:
    # 板块 2: 能源输出 & 系统负载
    st.write("#### ⚡ Infrastructure Pulse")
    col_r1, col_r2 = st.columns(2)
    col_r1.metric("GLOBAL OUTPUT", "14.2 GW", "+2.4%")
    col_r2.metric("ACTIVE STORAGE", "1.28M TONS", "+3.2%")
    col_r3, col_r4 = st.columns(2)
    col_r3.metric("RISK LEVEL", "0.02%", "inverse", "-0.01%")
    col_r4.metric("SYSTEM VIBE", "ELITE", "MAX")

st.write("---")

# **第2行：上中下游可视化板块 (充实空间的核心)**
c_up, c_mid, c_down, c_econ = st.columns([1.5, 2, 1.5, 1.5])

with c_up:
    st.write("#### ⚡ Upstream: Production Core")
    l_up, r_up = st.columns([1, 1.5])
    with l_up:
        tech = st.selectbox("Tech", ["ALK", "PEM", "SOEC"])
        pw = st.slider("Power (MW)", 1, 100, 20)
        tm = st.slider("Temp (°C)", 20, 100, 65)
    with r_up:
        eff, flow = mechanics.simulate_electrolysis(pw, tech, tm)
        st.metric("Efficiency", f"{eff}%")
        st.metric("H2 Flow", f"{flow} kg/h")

with c_mid:
    st.write("#### 🛡️ Midstream: Geo-UHS Study")
    l_mid, r_mid = st.columns([1, 2])
    with l_mid:
        depth = st.slider("Target Depth (m)", 500, 3000, 1200)
        p, t, d = mechanics.get_uhs_physics(depth)
        st.metric("Pressure", f"{p} MPa")
        st.metric("Density", f"{d} kg/m³")
    with r_mid:
        # 梨形盐穴
        X, Y, Z = mechanics.generate_3d_cavern_mesh()
        fig_cavern = go.Figure(data=[go.Surface(x=X, y=Y, z=Z, colorscale='Electric', showscale=False)])
        fig_cavern.update_layout(scene=dict(xaxis_visible=False, yaxis_visible=False, zaxis_title='DEPTH'),
                                 paper_bgcolor='rgba(0,0,0,0)', margin=dict(l=0, r=0, b=0, t=0))
        st.plotly_chart(fig_cavern, use_container_width=True)

with c_down:
    st.write("#### 🛰️ Downstream: Logistics Pipeline")
    p_len = st.number_input("Pipeline Len (km)", value=150)
    out_p, risk = mechanics.calculate_pipe_flow(5.0, p_len, 200)
    st.metric("Outlet Pressure", f"{out_p} MPa")
    st.error("Extreme Risk Zone" if risk > 80 else "Safe Operation")

with c_econ:
    st.write("#### 💰 Economics: Strategic Feasibility")
    capex, ro_y = mechanics.get_financial_metrics(10000, 1200)
    st.metric("Estimated CAPEX", f"${capex}M")
    st.metric("Simple ROI Period", f"{ro_y} Years")

st.markdown("---")
st.caption(f"© 2026 FUTURE ENERGY LAB | COMMAND ID: NX-ULTRA-SECURE | {lang} VERSION")