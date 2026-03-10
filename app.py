import streamlit as st
import mechanics
import plotly.graph_objects as go
import numpy as np
import time

# 1. 顶级页面配置
st.set_page_config(page_title="H2 NEXUS | GLOBAL TERMINAL", layout="wide", initial_sidebar_state="collapsed")

# 2. 注入顶级赛博朋克 CSS (含背景微光和发光文字)
st.markdown("""
    <style>
    .main {
        background-color: #00050a;
        background-image: radial-gradient(circle at 50% 50%, #001f3f 0%, #00050a 100%);
        color: #00f2ff;
    }
    .hero-title {
        font-family: 'Courier New', monospace;
        font-size: 4rem;
        font-weight: 900;
        text-align: center;
        color: #00f2ff;
        text-shadow: 0 0 20px #00f2ff, 0 0 40px #00a2ff;
        letter-spacing: 10px;
        margin-top: 50px;
    }
    [data-testid="stMetric"] {
        background: rgba(0, 242, 255, 0.05) !important;
        border: 1px solid #00f2ff !important;
        box-shadow: 0 0 15px rgba(0, 242, 255, 0.2);
    }
    </style>
    """, unsafe_allow_html=True)


# 3. 手搓 3D 动态能源核心 (替代报错的 Lottie)
def render_cyber_core():
    # 生成 3D 粒子云
    n = 1000
    theta = np.random.uniform(0, 2 * np.pi, n)
    phi = np.random.uniform(0, np.pi, n)
    r = 10 + np.random.normal(0, 1, n)

    x = r * np.sin(phi) * np.cos(theta)
    y = r * np.sin(phi) * np.sin(theta)
    z = r * np.cos(phi)

    fig = go.Figure(data=[go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(size=2, color=z, colorscale='Electric', opacity=0.8)
    )])

    fig.update_layout(
        scene=dict(
            xaxis_visible=False, yaxis_visible=False, zaxis_visible=False,
            camera=dict(eye=dict(x=1.2, y=1.2, z=1.2)),
            aspectmode='cube'
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0, r=0, b=0, t=0),
        showlegend=False
    )
    return fig


# 4. 侧边栏
if 'lang' not in st.session_state: st.session_state.lang = "English"
with st.sidebar:
    st.markdown("### `SECURITY ACCESS`")
    if st.button("🌐 SWITCH LANGUAGE"):
        st.session_state.lang = "中文" if st.session_state.lang == "English" else "English"
    lang = st.session_state.lang
    page = st.radio("SELECT SECTOR", ["GLOBAL HUB", "UHS RESEARCH", "ECONOMICS"])

# 5. 主页面逻辑
if page == "GLOBAL HUB":
    # 动态流光标题
    title_text = "H2 NEXUS TERMINAL" if lang == "English" else "氢能全球枢纽终端"
    st.markdown(f'<p class="hero-title">{title_text}</p>', unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: #00f2ff; opacity: 0.6;'>FUTURE ENERGY INFRASTRUCTURE v4.0</h4>",
                unsafe_allow_html=True)

    # 渲染 3D 能源核心 (这就是你要的高大上开场动态图)
    st.plotly_chart(render_cyber_core(), use_container_width=True, config={'displayModeBar': False})

    # 数据矩阵
    st.write("---")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("NETWORK", "ENCRYPTED", "SECURE")
    m2.metric("SYNC RATE", "99.8%", "LIVE")
    m3.metric("CORE TEMP", "1.2 MK", "STABLE")
    m4.metric("PURITY", "99.9999%", "MAX")

elif page == "UHS RESEARCH":
    st.title("🛡️ Subsurface Intelligence")
    col1, col2 = st.columns([1, 2])
    with col1:
        depth = st.slider("Depth Factor", 500, 3000, 1200)
        st.info("Neural scanning formation...")
    with col2:
        # 这里使用之前的高级 3D 盐穴
        x, y, z = mechanics.generate_3d_cavern_mesh()
        fig = go.Figure(data=[go.Surface(x=x, y=y, z=z, colorscale='Hot', showscale=False)])
        fig.update_layout(scene=dict(xaxis_visible=False, yaxis_visible=False), template="plotly_dark",
                          paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.caption(f"© 2026 FUTURE ENERGY LAB | ACCESS ID: {time.time()}")