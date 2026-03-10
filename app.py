import streamlit as st
import mechanics
import plotly.graph_objects as go
import numpy as np

# 1. 初始化配置
st.set_page_config(page_title="H2 NEXUS | GLOBAL", layout="wide", initial_sidebar_state="collapsed")

# 2. 注入顶级赛博 UI (全息投影风格)
st.markdown("""
    <style>
    .main {
        background: radial-gradient(circle at center, #001529 0%, #000408 100%);
        color: #00f2ff;
    }
    .hero-title {
        font-family: 'Courier New', Courier, monospace;
        font-size: 3.5rem;
        font-weight: 900;
        text-align: center;
        letter-spacing: 12px;
        color: #00f2ff;
        text-shadow: 0 0 15px #00f2ff, 0 0 30px #0055ff;
        margin-top: 30px;
    }
    [data-testid="stMetric"] {
        background: rgba(0, 242, 255, 0.05) !important;
        border: 1px solid rgba(0, 242, 255, 0.3) !important;
        border-radius: 15px !important;
        backdrop-filter: blur(10px);
    }
    </style>
    """, unsafe_allow_html=True)


# 3. 稳健的 3D 粒子地球函数 (修复了 ValueError)
def render_hologram_earth():
    # 使用极坐标采样生成地球点云
    n = 2000
    phi = np.random.uniform(0, 2 * np.pi, n)
    theta = np.random.uniform(0, np.pi, n)
    x = 10 * np.sin(theta) * np.cos(phi)
    y = 10 * np.sin(theta) * np.sin(phi)
    z = 10 * np.cos(theta)

    fig = go.Figure(data=[go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(size=1.5, color=z, colorscale='Blues', opacity=0.5)
    )])

    fig.update_layout(
        scene=dict(xaxis_visible=False, yaxis_visible=False, zaxis_visible=False,
                   camera=dict(eye=dict(x=1.3, y=1.3, z=0.7))),
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0, r=0, b=0, t=0),
        showlegend=False
    )
    return fig


# 4. 侧边栏及语言
if 'lang' not in st.session_state: st.session_state.lang = "English"
with st.sidebar:
    st.markdown("### `COMMAND CONTROL`")
    if st.button("🌐 SWITCH LANGUAGE"):
        st.session_state.lang = "中文" if st.session_state.lang == "English" else "English"
    lang = st.session_state.lang
    page = st.radio("SECTOR", ["GLOBAL NEXUS", "UHS STUDY", "FINANCE"])

# 5. 板块逻辑
if page == "GLOBAL NEXUS":
    st.markdown(f'<p class="hero-title">{"H2 NEXUS COMMAND" if lang == "English" else "氢能全球枢纽终端"}</p>',
                unsafe_allow_html=True)

    # 震撼的地球开场
    st.plotly_chart(render_hologram_earth(), use_container_width=True, config={'displayModeBar': False})

    st.write("---")
    cols = st.columns(4)
    cols[0].metric("SYNC STATUS", "ACTIVE", "GLOBAL")
    cols[1].metric("STORAGE", "1.2M T", "+0.4%")
    cols[2].metric("CORE TEMP", "STABLE", "65°C")
    cols[3].metric("NETWORK", "ENCRYPTED", "SECURE")


elif page == "UHS STUDY":
    st.header("🛡️ Subsurface Intelligence Scan")
    l, r = st.columns([1, 2])
    with l:
        depth = st.slider("Depth", 500, 3000, 1200)
        p, t, d = mechanics.get_uhs_physics(depth)
        st.metric("Pressure", f"{p} MPa")
        st.metric("Density", f"{d} kg/m³")
    with r:
        # 调用梨形盐穴
        X, Y, Z = mechanics.generate_3d_cavern_mesh()
        fig = go.Figure(data=[go.Surface(x=X, y=Y, z=Z, colorscale='Electric', showscale=False)])
        fig.update_layout(scene=dict(xaxis_visible=False, yaxis_visible=False),
                          paper_bgcolor='rgba(0,0,0,0)', margin=dict(l=0, r=0, b=0, t=0))
        st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.caption(f"© 2026 FUTURE ENERGY LAB | {lang} VERSION ACTIVE")