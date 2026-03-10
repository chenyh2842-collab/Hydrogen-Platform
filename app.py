import streamlit as st
import mechanics
import plotly.graph_objects as go
import numpy as np

st.markdown("""
    <video autoplay loop muted playsinline style="position: fixed; right: 0; bottom: 0; min-width: 100%; min-height: 100%; z-index: -1; opacity: 0.2;">
        <source src="https://assets.mixkit.co/videos/preview/mixkit-abstract-technology-screen-with-blue-lights-22262-large.mp4" type="video/mp4">
    </video>
""", unsafe_allow_html=True)

# 1. 顶级视觉配置
st.set_page_config(page_title="H2 NEBULA | COMMAND", layout="wide", initial_sidebar_state="expanded")

# 2. 注入“星际座舱”CSS (这一段是视觉核心)
st.markdown("""
    <style>
    /* 全局深空背景 */
    .main {
        background: #000408;
        color: #00f2ff;
        background-image: 
            radial-gradient(1px 1px at 20px 30px, #fff, rgba(0,0,0,0)),
            radial-gradient(1px 1px at 40px 70px, #fff, rgba(0,0,0,0)),
            radial-gradient(2px 2px at 50% 50%, #001f3f, #000408);
        background-size: 200px 200px, 150px 150px, 100% 100%;
    }

    /* 顶部流光 Banner */
    .hero-banner {
        height: 300px;
        background: linear-gradient(45deg, #001529, #003366);
        border: 2px solid #00f2ff;
        border-radius: 15px;
        box-shadow: 0 0 50px rgba(0, 242, 255, 0.2);
        display: flex;
        justify-content: center;
        align-items: center;
        overflow: hidden;
        position: relative;
    }

    /* 全息文字效果 */
    .hologram-text {
        font-family: 'Courier New', Courier, monospace;
        font-size: 3rem;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 15px;
        color: rgba(0, 242, 255, 0.8);
        text-shadow: 
            0 0 10px #00f2ff,
            0 0 20px #00f2ff,
            -2px 0 #ff00de,
            2px 0 #00ff00;
        animation: glitch 1s infinite;
    }

    @keyframes glitch {
        0% { transform: skew(0deg); }
        20% { transform: skew(2deg); }
        60% { transform: skew(-1deg); }
        100% { transform: skew(0deg); }
    }

    /* 模块卡片 - 玻璃拟态 2.0 */
    .stMetric {
        background: rgba(0, 242, 255, 0.05) !important;
        border: 1px solid rgba(0, 242, 255, 0.4) !important;
        backdrop-filter: blur(10px);
        box-shadow: inset 0 0 20px rgba(0, 242, 255, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 页面布局：震撼开场
st.markdown("""
    <div class="hero-banner">
        <div class="hologram-text">H2 NEXUS</div>
    </div>
    """, unsafe_allow_html=True)

# 4. 侧边栏控制
with st.sidebar:
    st.title("🛡️ COMMAND CENTER")
    lang = st.radio("INTERFACE LANG", ["ENG", "CHN"])
    st.markdown("---")
    st.write("### SYSTEM LOGS")
    st.code(">> INITIALIZING QUANTUM LINK\n>> SCANNING UHS CAVERN\n>> SYNCING DATA NODES...", language="bash")
    st.divider()
    page = st.selectbox("MODULE", ["CORE OVERVIEW", "MIDSTREAM UHS", "FINANCIAL MATRIX"])

# 5. 内容分流
if page == "CORE OVERVIEW":
    st.write("### 💠 REAL-TIME ENERGY PULSE")

    # 震撼的数据面板
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("NETWORK STATUS", "ENCRYPTED", "STABLE")
    m2.metric("ENERGY SYNC", "94.2%", "UP")
    m3.metric("CORE TEMP", "1200 K", "OPTIMAL")
    m4.metric("SYSTEM VIBE", "ELITE", "MAX")

    # 3D 视觉展示 (改进版)
    st.write("---")
    c1, c2 = st.columns([1, 1])
    with c1:
        st.subheader("Hydrogen Flow Simulation")
        # 建立一个带有流光效果的折线图
        chart_data = np.random.randn(20, 3)
        st.line_chart(chart_data)

    with c2:
        st.subheader("Global Storage Nodes")
        # 粒子球增强
        n = 500
        fig = go.Figure(data=[go.Scatter3d(
            x=np.random.standard_normal(n), y=np.random.standard_normal(n), z=np.random.standard_normal(n),
            mode='markers', marker=dict(size=3, color='cyan', opacity=0.6)
        )])
        fig.update_layout(scene=dict(xaxis_visible=False, yaxis_visible=False, zaxis_visible=False),
                          paper_bgcolor='rgba(0,0,0,0)', margin=dict(l=0, r=0, b=0, t=0))
        st.plotly_chart(fig, use_container_width=True)

elif page == "MIDSTREAM UHS":
    st.header("🛡️ Subsurface Intelligence")
    # 这里嵌入你最自豪的 3D 梨形盐穴
    x, y, z = mechanics.generate_3d_cavern_mesh()
    fig = go.Figure(data=[go.Surface(x=x, y=y, z=z, colorscale='Electric', showscale=False)])
    fig.update_layout(scene=dict(xaxis_visible=False, yaxis_visible=False, zaxis_title='DEPTH'),
                      template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.caption("© 2026 FUTURE ENERGY LAB | ACCESS ID: CNPC-ULTRA-SECURE")