import streamlit as st
import mechanics
import plotly.graph_objects as go
import numpy as np
import requests

# 1. 顶级页面配置 (关闭侧边栏，开场全屏震撼)
st.set_page_config(page_title="H2 NEBULA | GLOBAL NX", layout="wide", initial_sidebar_state="collapsed")

# 2. 注入“星际指挥中心 2.0”CSS (视觉核心)
st.markdown("""
    <style>
    /* 全局深空背景，加入背景视频纹理 (可换成你自己的视频) */
    .main {
        background-color: #000205;
        background-image: radial-gradient(circle at 50% 50%, #001f3f 0%, #000205 100%);
        color: #e6f7ff;
    }
    .main::before {
        content: " ";
        position: fixed;
        top: 0; left: 0; bottom: 0; right: 0;
        background-image: 
            radial-gradient(1px 1px at 20px 30px, #fff, rgba(0,0,0,0)),
            radial-gradient(1px 1px at 40px 70px, #fff, rgba(0,0,0,0));
        background-size: 200px 200px, 150px 150px;
        z-index: -1;
        opacity: 0.1;
    }

    /* 顶部 Glitch 霓虹标题动画 */
    .hero-title {
        font-family: 'Courier New', monospace;
        font-size: 3.5rem;
        font-weight: 900;
        text-align: center;
        letter-spacing: 15px;
        color: rgba(0, 242, 255, 0.9);
        text-shadow: 
            0 0 20px #00f2ff,
            0 0 40px #00a2ff,
            -2px 0 #ff00de,
            2px 0 #00ff00;
        animation: glitch 1.5s infinite;
        margin-top: 50px;
        text-transform: uppercase;
    }
    @keyframes glitch {
        0% { transform: skew(0deg); }
        20% { transform: skew(2deg); }
        60% { transform: skew(-1deg); }
        100% { transform: skew(0deg); }
    }

    /* 玻璃拟态卡片 2.0：半透明 + 发光边框 */
    [data-testid="stMetric"] {
        background: rgba(0, 242, 255, 0.03) !important;
        border: 1px solid rgba(0, 242, 255, 0.3) !important;
        backdrop-filter: blur(15px);
        border-radius: 15px !important;
        box-shadow: 0 0 25px rgba(0, 242, 255, 0.1);
        transition: 0.3s;
    }
    [data-testid="stMetric"]:hover {
        border: 1px solid #00f2ff !important;
        box-shadow: 0 0 40px rgba(0, 242, 255, 0.5);
    }

    /* 侧边栏全屏化 */
    [data-testid="stSidebar"] {
        background-color: rgba(0, 10, 20, 0.9) !important;
        border-right: 1px solid rgba(0, 242, 255, 0.5);
    }
    </style>
    """, unsafe_allow_html=True)


# 3. 辅助函数：渲染 3D 科幻地球模型背景图
def render_cyber_earth():
    # 生成地球粒子点云 (模拟卫星探测纹理)
    n = 1500
    phi = np.random.uniform(0, 2 * np.pi, n)
    theta = np.random.uniform(0, np.pi, n)
    r = 10 + np.random.normal(0, 0.2, n)

    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)

    # 增加地球网格层
    u = np.linspace(0, 2 * np.pi, 50)
    v = np.linspace(0, np.pi, 50)
    u, v = np.meshgrid(u, v)
    X = 10 * np.sin(v) * np.cos(u)
    Y = 10 * np.sin(v) * np.sin(u)
    Z = 10 * np.cos(v)

    fig = go.Figure(data=[
        go.Scatter3d(x=x, y=y, z=z, mode='markers', marker=dict(size=1.5, color=z, colorscale='Cyan', opacity=0.4)),
        go.Surface(x=X, y=Y, z=Z, colorscale='Electric', showscale=False, opacity=0.1)
    ])

    fig.update_layout(
        scene=dict(
            xaxis_visible=False, yaxis_visible=False, zaxis_visible=False,
            camera=dict(eye=dict(x=1.3, y=1.3, z=0.6)),
            aspectmode='cube'
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0, r=0, b=0, t=0),
        showlegend=False
    )
    return fig


# 4. 侧边栏及多语言引擎 (默认英文)
if 'lang' not in st.session_state: st.session_state.lang = "English"
with st.sidebar:
    st.markdown("### `SYSTEM ACCESS`")
    if st.button("🌐 SWITCH LANGUAGE"):
        st.session_state.lang = "中文" if st.session_state.lang == "English" else "English"

    lang = st.session_state.lang
    st.divider()
    page = st.selectbox("OPERATIONAL SECTOR", ["GLOBAL NEXUS", "UHS RESEARCH", "ECONOMICS"])
    st.divider()
    st.code(">> QUANTUM LINK ACTIVE\n>> GLOBAL STORAGE SYNCED\n>> ID: CNPC-ULTRA-2050", language="bash")

# 5. 主页面模块
if page == "GLOBAL NEXUS":
    # Glitch大标题
    title_text = "H2 NEXUS COMMAND" if lang == "English" else "氢能全球枢纽终端"
    st.markdown(f'<p class="hero-title">{title_text}</p>', unsafe_allow_html=True)

    # 中央：旋转的科幻 3D 地球背景 (视觉重心)
    st.plotly_chart(render_cyber_earth(), use_container_width=True, config={'displayModeBar': False})

    # 底部数据矩阵 (玻璃拟态悬浮)
    st.write("---")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("GLOBAL SYNC", "98.2%", "+1.4%")
    m2.metric("ENERGY OUTPUT", "24 GW", "Optimal")
    m3.metric("CORE TEMP", "1.2 MK", "Stable")
    m4.metric("SYSTEM LOAD", "ELITE", "Max")


elif page == "UHS RESEARCH":
    st.title("🛡️ Subsurface Intelligence")
    l, r = st.columns([1, 2])
    with l:
        depth = st.slider("Depth (m)", 500, 3000, 1500)
        p, t, dens = mechanics.get_uhs_physics(depth)
        st.metric("Pressure (MPa)", p)
        st.metric("Density (kg/m³)", dens)
    with r:
        # 这里嵌入高级梨形盐穴
        x, y, z = mechanics.generate_3d_cavern_mesh()
        fig = go.Figure(data=[go.Surface(x=x, y=y, z=z, colorscale='Electric', showscale=False)])
        fig.update_layout(scene=dict(xaxis_visible=False, yaxis_visible=False, zaxis_title='DEPTH'),
                          template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.caption("© 2026 FUTURE ENERGY LAB | ACCESS ID: CNPC-ULTRA-SECURE")