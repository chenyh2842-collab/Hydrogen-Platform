import streamlit as st
import mechanics
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import time

# 1. 顶级配置
st.set_page_config(page_title="H2 NEBULA COMMAND", layout="wide", initial_sidebar_state="collapsed")

# 2. 核心视觉：注入红外扫描与数字翻滚 CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&display=swap');

    .main { background: radial-gradient(circle at center, #001529 0%, #000206 100%); color: #e6f7ff; }

    /* 霓虹大标题 */
    .hero-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 3.5rem; text-align: center; letter-spacing: 15px;
        color: #00f2ff; text-shadow: 0 0 20px #00f2ff;
        animation: glitch 2s infinite;
    }

    /* 动态数字翻滚效果 */
    .rolling-number {
        font-family: 'Orbitron', sans-serif;
        font-size: 2.8rem; font-weight: 900;
        color: #ff00de; text-shadow: 0 0 15px #ff00de;
        animation: slideUp 0.8s cubic-bezier(0.18, 0.89, 0.32, 1.28);
    }

    @keyframes slideUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* 全息卡片 */
    [data-testid="stMetric"], .stPlotlyChart {
        background: rgba(0, 242, 255, 0.04) !important;
        border: 1px solid rgba(0, 242, 255, 0.3) !important;
        backdrop-filter: blur(10px); border-radius: 15px !important;
    }
    </style>
    """, unsafe_allow_html=True)


# 3. 动态扫描渲染引擎
def render_scanned_map():
    locations = pd.DataFrame({
        'City': ['Beijing', 'Houston', 'London', 'Dubai', 'Singapore'],
        'lat': [39.9, 29.7, 51.5, 25.2, 1.3], 'lon': [116.4, -95.3, -0.1, 55.3, 103.8]
    })
    fig = go.Figure()
    # 呼吸感的脉动点
    pulse_size = 12 + 4 * np.sin(time.time() * 2)
    fig.add_trace(go.Scattergeo(
        lon=locations['lon'], lat=locations['lat'],
        mode='markers',
        marker=dict(size=pulse_size, color='#00f2ff', opacity=0.7,
                    line=dict(width=2, color='#ffffff'))
    ))
    fig.update_geos(projection_type="orthographic", showland=True, landcolor="#000811",
                    showocean=True, oceancolor="#000206", bgcolor='rgba(0,0,0,0)')
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', margin=dict(l=0, r=0, b=0, t=0))
    return fig


def render_infrared_cavern():
    X, Y, Z = mechanics.generate_3d_cavern_mesh()
    # 基础全息网格
    fig = go.Figure(data=[go.Surface(x=X, y=Y, z=Z, colorscale='Blues', opacity=0.4, showscale=False)])

    # 动态红外扫描线 (随时间循环移动)
    scan_z = -60 + 60 * np.sin(time.time() * 1.5)
    # 抽取对应高度的截面圆
    fig.add_trace(go.Scatter3d(
        x=X[20], y=Y[20], z=[scan_z] * len(X[20]),
        mode='lines', line=dict(color='#ff00de', width=8)
    ))

    fig.update_layout(scene=dict(xaxis_visible=False, yaxis_visible=False, zaxis_visible=False),
                      paper_bgcolor='rgba(0,0,0,0)', margin=dict(l=0, r=0, b=0, t=0))
    return fig


# 4. 主界面布局
st.markdown('<p class="hero-title">H2 GLOBAL COMMAND</p>', unsafe_allow_html=True)

st.write("---")
c1, c2, c3 = st.columns([1, 2, 1])

with c1:
    st.markdown("### 💠 Infrastructure")
    st.metric("SYNC STATUS", "ACTIVE", "SECURE")
    st.metric("CORE TEMP", "1.2 MK", "STABLE")

with c2:
    st.plotly_chart(render_scanned_map(), use_container_width=True)

with c3:
    st.markdown("### ⚡ Pulse")
    st.metric("GLOBAL OUTPUT", "14.2 GW", "+2.4%")
    st.metric("NETWORK ID", "NX-2050", "ELITE")

st.write("---")
c_left, c_right = st.columns([1.5, 1])

with c_left:
    st.markdown("#### 🛡️ Subsurface Infrared Scanning")
    col_a, col_b = st.columns([1, 2])
    with col_a:
        d_val = st.slider("Scanning Depth (m)", 500, 3000, 1500)
        p, t, dens = mechanics.get_uhs_physics(d_val)
        st.write(f"Pressure: `{p} MPa`")
        st.write(f"Temp: `{t} °C`")
    with col_b:
        # 这里就是那个带红外扫描线的 3D 盐穴
        st.plotly_chart(render_infrared_cavern(), use_container_width=True)

with c_right:
    st.markdown("#### 💰 Financial Feasibility")
    cap, sav = mechanics.get_financial_metrics(10000, d_val)
    # 数字翻滚动画展示
    st.markdown(f'<div class="rolling-number">${cap}M</div>', unsafe_allow_html=True)
    st.caption("ESTIMATED TOTAL CAPEX (CAPITAL EXPENDITURE)")
    st.progress(85)
    st.info(">> ROI ANALYSIS: HIGH FEASIBILITY")

st.markdown("---")
if st.button("🔄 REFRESH COMMAND SENSORS"):
    st.rerun()