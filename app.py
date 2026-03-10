import streamlit as st
import mechanics
import plotly.graph_objects as go
import numpy as np
import time

# 1. 初始化顶级视觉配置 (Interstellar Command Center)
st.set_page_config(page_title="H2 GLOBAL NEXUS | NX-500", layout="wide", initial_sidebar_state="collapsed")

# 2. 注入极致赛博视觉 CSS (核心：全息、霓虹、故障、呼吸感)
st.markdown("""
    <style>
    /* 全局：深空赛博蓝背景 + 动态扫描线纹理 */
    .main {
        background: #000206;
        background-image: 
            radial-gradient(circle at center, #001529 0%, #000206 100%),
            linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.2) 50%);
        background-size: 100% 100%, 100% 3px;
        color: #e6f7ff;
    }

    /* 顶部 Glitch 故障艺术大标题 */
    .hero-title {
        font-family: 'Segoe UI Light', 'Courier New', monospace;
        font-size: 3.8rem;
        font-weight: 900;
        text-align: center;
        letter-spacing: 20px;
        color: rgba(0, 242, 255, 0.9);
        text-shadow: 
            0 0 15px #00f2ff, 
            0 0 30px #00a2ff,
            -3px 0 #ff00de, 
            3px 0 #00ff00;
        margin-top: 40px;
        margin-bottom: 5px;
        text-transform: uppercase;
        animation: glitch 1s infinite linear;
    }
    @keyframes glitch {
        0% { transform: skew(0deg); }
        20% { transform: skew(1.5deg); }
        60% { transform: skew(-0.8deg); }
        100% { transform: skew(0deg); }
    }

    /* 玻璃拟态卡片 3.0：呼吸边框 + 全息模糊 */
    [data-testid="stMetric"] {
        background: rgba(0, 242, 255, 0.03) !important;
        border: 1px solid rgba(0, 242, 255, 0.25) !important;
        backdrop-filter: blur(15px);
        border-radius: 18px !important;
        box-shadow: 0 0 25px rgba(0, 242, 255, 0.1);
        transition: 0.4s;
    }
    [data-testid="stMetric"]:hover {
        transform: translateY(-8px);
        border: 1px solid #00f2ff !important;
        box-shadow: 0 0 50px rgba(0, 242, 255, 0.4);
    }

    /* 系统控制面板全透明 */
    [data-testid="stSidebar"] {
        background-color: rgba(0, 5, 15, 0.95) !important;
        border-right: 1px solid rgba(0, 242, 255, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)


# 3. 辅助函数：渲染全球能源地图 (Holographic World Map)
def render_holographic_map():
    # 使用地理坐标数据 (Plotly 自带)
    df = pd.DataFrame({'lat': [], 'lon': [], 'name': []})  # 占位

    # 建立 3D 地理散射图 (使用地球模型)
    fig = go.Figure()

    # 地球网格
    # (使用 mechanics.py 中的粒子球逻辑模拟全球网络感)
    n = 2000
    phi = np.random.uniform(0, 2 * np.pi, n)
    theta = np.random.uniform(0, np.pi, n)
    r = 10
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)

    fig.add_trace(go.Scatter3d(
        x=x, y=y, z=z, mode='markers',
        marker=dict(size=1.2, color=z, colorscale='Cyan', opacity=0.3)
    ))

    # 全球各大洲霓虹轮廓 (电影质感核心)
    # (这里需要复杂的地理数据，我们用 Scatter3d 模拟主要节点)
    cities = pd.DataFrame({
        'name': ['Beijing', 'New York', 'London', 'Tokyo', 'Singapore'],
        'lat': [39.9, 40.7, 51.5, 35.7, 1.3],
        'lon': [116.4, -74.0, -0.1, 139.7, 103.8]
    })

    # 经纬度转 3D
    cities['z'] = 10 * np.sin(np.radians(cities['lat']))
    cities['y'] = 10 * np.cos(np.radians(cities['lat'])) * np.sin(np.radians(cities['lon']))
    cities['x'] = 10 * np.cos(np.radians(cities['lat'])) * np.cos(np.radians(cities['lon']))

    # 添加主要节点发光点和连接线
    fig.add_trace(go.Scatter3d(
        x=cities['x'], y=cities['y'], z=cities['z'],
        mode='markers+lines',
        marker=dict(size=8, color='#ff00de', opacity=0.8),
        line=dict(color='#00f2ff', width=3)
    ))

    fig.update_layout(
        scene=dict(
            xaxis_visible=False, yaxis_visible=False, zaxis_visible=False,
            camera=dict(eye=dict(x=1.4, y=1.4, z=0.5)),
            aspectmode='cube'
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0, r=0, b=0, t=0),
        showlegend=False
    )
    return fig


# 4. 侧边栏：系统控制中心 (默认英文)
if 'lang' not in st.session_state: st.session_state.lang = "English"
with st.sidebar:
    st.markdown("### `SYSTEM ACCESS`")
    if st.button("🌐 SWITCH LANGUAGE"):
        st.session_state.lang = "中文" if st.session_state.lang == "English" else "English"

    curr_lang = st.session_state.lang
    st.divider()
    page = st.selectbox("OPERATIONAL SECTOR", ["GLOBAL NEXUS", "UHS RESEARCH", "ECONOMICS"])
    st.divider()
    # 系统日志瀑布流
    st.code(">> INITIALIZING QUANTUM LINK\n>> SCANNING GEO-STORAGE\n>> ID: CNPC-ULTRA-2050", language="bash")
    st.caption("NEURAL-NET STATUS: ONLINE")

# 5. 主页面模块
# Glitch 大标题
title_text = "H2 NEBULA GLOBAL COMMAND" if curr_lang == "English" else "氢能全球指挥终端"
st.markdown(f'<p class="hero-title">{title_text}</p>', unsafe_allow_html=True)
st.caption(
    f"<p style='text-align: center; color: #00f2ff; opacity: 0.6;'>System Status: [Operational] | NX-Series v5.0</p>",
    unsafe_allow_html=True)

if page == "GLOBAL NEXUS":
    # 中央：全息旋转地球地图 (视觉重心)
    st.plotly_chart(render_holographic_map(), use_container_width=True, config={'displayModeBar': False})

    st.write("---")
    # 底部数据矩阵 (玻璃拟态半透明)
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("NETWORK STATUS", "ENCRYPTED", "OPTIMAL")
    m2.metric("ENERGY SYNC", "94.8%", "+3.1%")
    m3.metric("CORE TEMP", "1.2 MK", "Stable")
    m4.metric("CARBON OFFSET", "125k Tons", "Live")

st.markdown("---")
st.caption(f"© 2026 FUTURE ENERGY LAB | ACCESS ID: CNPC-ULTRA-SECURE")