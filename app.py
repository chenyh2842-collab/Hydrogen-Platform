import streamlit as st
import mechanics
import plotly.graph_objects as go
import time

# 1. 全球顶级视觉配置 (Advanced Cyber-UI)
st.set_page_config(page_title="H2 VISION 2050 | GLOBAL TERMINAL", layout="wide", initial_sidebar_state="expanded")

# 注入动态扫描线和霓虹玻璃效果
st.markdown("""
    <style>
    /* 动态背景扫描线效果 */
    .main {
        background: linear-gradient(180deg, #000b1a 0%, #001529 100%);
        background-attachment: fixed;
        color: #00f2ff;
    }
    .main::before {
        content: " ";
        position: fixed;
        top: 0; left: 0; bottom: 0; right: 0;
        background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%), linear-gradient(90deg, rgba(255, 0, 0, 0.06), rgba(0, 255, 0, 0.02), rgba(0, 0, 255, 0.06));
        z-index: 9999;
        background-size: 100% 2px, 3px 100%;
        pointer-events: none;
    }

    /* 玻璃拟态卡片 */
    [data-testid="stMetric"] {
        background: rgba(0, 242, 255, 0.03) !important;
        border: 1px solid rgba(0, 242, 255, 0.3) !important;
        backdrop-filter: blur(10px);
        border-radius: 20px !important;
        box-shadow: 0 0 20px rgba(0, 242, 255, 0.1);
        transition: transform 0.3s ease;
    }
    [data-testid="stMetric"]:hover {
        transform: translateY(-5px);
        border: 1px solid #00f2ff !important;
        box-shadow: 0 0 30px rgba(0, 242, 255, 0.4);
    }

    /* 标题发光动画 */
    h1 {
        text-transform: uppercase;
        letter-spacing: 5px;
        background: linear-gradient(90deg, #00f2ff, #ffffff, #00f2ff);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: shine 3s linear infinite;
    }
    @keyframes shine { to { background-position: 200% center; } }
    </style>
    """, unsafe_allow_html=True)


# 2. 增强版 3D 动态渲染函数 (在模块中调用)
def draw_dynamic_3d():
    X, Y, Z = mechanics.generate_3d_cavern_mesh()
    # 增加科技感：流光网格层
    fig = go.Figure(data=[
        go.Surface(x=X, y=Y, z=Z,
                   colorscale='Cyan_r',
                   showscale=False,
                   contours_z=dict(show=True, usecolormap=True, highlightcolor="limegreen", project_z=True)),
        go.Scatter3d(x=X.flatten()[::10], y=Y.flatten()[::10], z=Z.flatten()[::10],
                     mode='markers', marker=dict(size=2, color='#ffffff', opacity=0.5))
    ])
    fig.update_layout(
        scene=dict(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            zaxis=dict(backgroundcolor="rgb(0, 10, 20)", gridcolor="rgba(0, 242, 255, 0.2)"),
            camera=dict(eye=dict(x=1.5, y=1.5, z=0.8))
        ),
        margin=dict(l=0, r=0, b=0, t=0),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    return fig


# 3. 系统标题区
st.markdown("### 💠 QUANTUM ENERGY NODE 01")
st.title("Hydrogen Neural Twin")
st.markdown("---")

# 4. 动态数据流展示区
cols = st.columns(4)
with cols[0]:
    st.metric("CORE TEMP", "65.2 °C", "+0.2%")
with cols[1]:
    st.metric("H2 PURITY", "99.9998%", "OPTIMAL")
with cols[2]:
    st.metric("STORAGE CAP", "1,240,000 m³", "LIVE")
with cols[3]:
    st.metric("NETWORK SYNC", "SYNCED", "14ms")

# 5. 内容分流 (这里只展示 Storage 板块的动态升级)
st.write("### 🛰️ Real-time Geo-Structural Analysis")
col_l, col_r = st.columns([1, 2])
with col_l:
    st.info("Neural Link Active: Monitoring subterranean pressure variances.")
    depth = st.select_slider("Select Depth Simulation (m)", options=[800, 1200, 1500, 2000, 3000])
    # 模拟数据加载动画
    with st.spinner('Accessing Formation Data...'):
        time.sleep(0.5)
        p, t, dens = mechanics.get_uhs_physics(depth)
        st.write(f"#### 地层压力: `{p} MPa`")
        st.write(f"#### 环境温度: `{t} °C`")

with col_r:
    # 动态 3D 模型
    fig = draw_dynamic_3d()
    st.plotly_chart(fig, use_container_width=True)