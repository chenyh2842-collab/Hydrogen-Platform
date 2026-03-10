import streamlit as st
import mechanics
import plotly.graph_objects as go
from streamlit_lottie import st_lottie
import requests
import time

# 1. 顶级视觉配置
st.set_page_config(page_title="H2 NEXUS | GLOBAL ENERGY", layout="wide", initial_sidebar_state="collapsed")

# 2. 注入“黑客帝国+未来实验室”CSS
st.markdown("""
    <style>
    /* 全局暗黑发光背景 */
    .main {
        background-color: #00050a;
        background-image: 
            radial-gradient(circle at 50% 50%, #001f3f 0%, #00050a 100%),
            url("https://www.transparenttextures.com/patterns/carbon-fibre.png");
        color: #00f2ff;
    }

    /* 霓虹标题动画 */
    .hero-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 3.5rem;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(to right, #00f2ff, #7000ff, #00f2ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradient-move 5s infinite linear;
        text-shadow: 0 0 30px rgba(0, 242, 255, 0.5);
    }

    @keyframes gradient-move {
        0% { background-position: 0% 50%; }
        100% { background-position: 200% 50%; }
    }

    /* 侧边栏全透明化 */
    [data-testid="stSidebar"] {
        background-color: rgba(0, 8, 20, 0.8) !important;
        border-right: 1px solid #00f2ff;
        backdrop-filter: blur(15px);
    }
    </style>
    """, unsafe_allow_html=True)


# 3. 辅助函数：加载动态 Lottie 动画 (3D 氢气/能量球)
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200: return None
    return r.json()


# 这里使用一个代表“未来科技/地球能源”的 Lottie 链接
lottie_energy = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_m6cu96ze.json")  # 3D 旋转科技球
lottie_h2 = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_S6936A.json")  # 3D 氢分子脉动

# 4. 侧边栏控制
with st.sidebar:
    st.markdown("## `ACCESS GRANTED`")
    if st.button("🌐 Switch Language / 切换语言"):
        st.session_state.lang = "中文" if st.session_state.get('lang', 'English') == 'English' else 'English'

    lang = st.session_state.get('lang', 'English')
    st.divider()
    page = st.selectbox("CORE OPERATIONS", ["DASHBOARD", "PRODUCTION", "UHS STORAGE", "LOGISTICS", "ECONOMICS"])

# 5. 首页：极致震撼开场
if page == "DASHBOARD":
    # 顶部流光标题
    st.markdown(f'<p class="hero-title">{"H2 GLOBAL NEXUS TERMINAL" if lang == "English" else "氢能全球枢纽终端"}</p>',
                unsafe_allow_html=True)

    # 中央 3D 动态氢气/地球示意图 (顶级的视觉重心)
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        st_lottie(lottie_energy, speed=1, reverse=False, loop=True, quality="high", height=400)

    # 底部数据矩阵
    st.write("---")
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.metric("GLOBAL SYNC", "ONLINE", delta="Stable")
    with m2:
        st.metric("ENERGY OUTPUT", "14.2 GW", delta="+2.4%")
    with m3:
        st.metric("H2 PURITY", "99.998%", delta="Max")
    with m4:
        st.metric("RISK LEVEL", "0.02%", delta="-0.01%", delta_color="inverse")

    # 引入一个 3D 动态背景感官图


# 6. 其他模块（保持高端风格）
elif page == "UHS STORAGE":
    st.markdown("## 🛰️ Subterranean Neural Scan")
    l, r = st.columns([1, 1])
    with l:
        # 这里的 3D 模型我们也做发光处理
        x, y, z = mechanics.generate_3d_cavern_mesh()
        fig = go.Figure(data=[go.Mesh3d(x=x.flatten(), y=y.flatten(), z=z.flatten(),
                                        intensity=z.flatten(), colorscale='Viridis', opacity=0.8)])
        fig.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig, use_container_width=True)
    with r:
        st_lottie(lottie_h2, height=300)
        st.write("### Real-time Formation Pressure: 12.4 MPa")
        st.progress(62)
        st.caption("Monitoring hydrogen molecular diffusion in salt cavern...")

# 7. 底部状态栏
st.markdown("---")
st.caption("SYSTEM STATUS: [OPERATIONAL] | CORE: QUANTUM-H2 | ENCRYPTION: ACTIVE")