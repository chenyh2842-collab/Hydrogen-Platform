import streamlit as st
import mechanics
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# 1. 顶级页面配置
st.set_page_config(page_title="H2 GLOBAL NEXUS", layout="wide", initial_sidebar_state="collapsed")

# 2. 极致赛博视觉 CSS
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
        margin-top: 30px;
        animation: glitch 1.5s infinite linear;
    }
    @keyframes glitch {
        0% { transform: skew(0deg); }
        20% { transform: skew(1deg); }
        60% { transform: skew(-0.5deg); }
        100% { transform: skew(0deg); }
    }
    [data-testid="stMetric"] {
        background: rgba(0, 242, 255, 0.05) !important;
        border: 1px solid rgba(0, 242, 255, 0.3) !important;
        backdrop-filter: blur(15px);
        border-radius: 15px !important;
    }
    </style>
    """, unsafe_allow_html=True)


# 3. 核心：渲染赛博朋克世界地图 (Fixed NameError)
def render_cyber_world_map():
    # 模拟全球能源中心数据
    locations = pd.DataFrame({
        'City': ['Beijing', 'Houston', 'London', 'Dubai', 'Singapore', 'Berlin'],
        'lat': [39.9, 29.7, 51.5, 25.2, 1.3, 52.5],
        'lon': [116.4, -95.3, -0.1, 55.3, 103.8, 13.4],
        'Output': [95, 88, 72, 91, 65, 78]
    })

    fig = go.Figure()

    # 添加全球连接流线 (模拟氢能输送网络)
    for i in range(len(locations) - 1):
        fig.add_trace(go.Scattergeo(
            locationmode='ISO-3',
            lon=[locations['lon'][i], locations['lon'][i + 1]],
            lat=[locations['lat'][i], locations['lat'][i + 1]],
            mode='lines',
            line=dict(width=1, color='#00f2ff'),
            opacity=0.3,
        ))

    # 添加能源中心发光点
    fig.add_trace(go.Scattergeo(
        lon=locations['lon'],
        lat=locations['lat'],
        text=locations['City'],
        mode='markers',
        marker=dict(
            size=12,
            color='#ff00de',
            symbol='circle',
            line=dict(width=2, color='#00f2ff'),
            opacity=0.8
        )
    ))

    # 地图视觉样式定制 (Dark/Neon Style)
    fig.update_geos(
        projection_type="orthographic",  # 正交投影，球体感
        showcoastlines=True, coastlinecolor="rgba(0, 242, 255, 0.3)",
        showland=True, landcolor="#000811",
        showocean=True, oceancolor="#000206",
        showcountries=True, countrycolor="rgba(0, 242, 255, 0.2)",
        bgcolor='rgba(0,0,0,0)'
    )

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0, r=0, b=0, t=0),
        showlegend=False,
        scene_camera=dict(eye=dict(x=1.25, y=1.25, z=1.25))
    )
    return fig


# 4. 界面逻辑
if 'lang' not in st.session_state: st.session_state.lang = "English"

with st.sidebar:
    st.title("🛡️ COMMAND")
    if st.button("🌐 SWITCH LANGUAGE"):
        st.session_state.lang = "中文" if st.session_state.lang == "English" else "English"
    page = st.radio("SECTOR", ["GLOBAL NEXUS", "RESEARCH", "FINANCE"])

lang = st.session_state.lang
title_text = "H2 GLOBAL COMMAND" if lang == "English" else "氢能全球指挥终端"
st.markdown(f'<p class="hero-title">{title_text}</p>', unsafe_allow_html=True)

if page == "GLOBAL NEXUS":
    # 震撼的世界地图开场
    st.plotly_chart(render_cyber_world_map(), use_container_width=True, config={'displayModeBar': False})

    st.write("---")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("NETWORK", "ENCRYPTED", "GLOBAL")
    c2.metric("H2 SUPPLY", "2.4M TONS", "+5.2%")
    c3.metric("NODES", "154 ACTIVE", "LIVE")
    c4.metric("EFFICIENCY", "94.2%", "OPTIMAL")

elif page == "RESEARCH":
    st.header("🛡️ Subsurface Intelligence Scan")
    # 调用 mechanics 里的 3D 盐穴
    X, Y, Z = mechanics.generate_3d_cavern_mesh()
    fig_cavern = go.Figure(data=[go.Surface(x=X, y=Y, z=Z, colorscale='Electric', showscale=False)])
    fig_cavern.update_layout(scene=dict(xaxis_visible=False, yaxis_visible=False), paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_cavern, use_container_width=True)

st.markdown("---")
st.caption("© 2026 FUTURE ENERGY LAB | ACCESS ID: CNPC-ULTRA-SECURE")