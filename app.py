import streamlit as st
import mechanics
import plotly.graph_objects as go
import pandas as pd

# 1. 页面基础配置
st.set_page_config(page_title="CNPC Hydrogen Platform", layout="wide", page_icon="⛽")

# 2. 语言字典 (中英双语)
LANG = {
    "中文": {
        "nav": ["总览", "上游: 绿氢制备", "中游: 地下储氢", "下游: 安全输运"],
        "hero_title": "中国石油氢能全产业链数字化实验室",
        "u_h": "可再生能源制氢模拟",
        "m_h": "地下储氢 (UHS) 物理机理",
        "d_h": "氢气输送与损耗监测",
        "calc": "计算结果",
        "3d_view": "3D 储层几何形态"
    },
    "English": {
        "nav": ["Overview", "Upstream", "Midstream", "Downstream"],
        "hero_title": "CNPC Hydrogen Value Chain Digital Lab",
        "u_h": "Green Hydrogen Production",
        "m_h": "UHS Physical Mechanics",
        "d_h": "Transport & Loss Monitoring",
        "calc": "Calculation Results",
        "3d_view": "3D Reservoir Geometry"
    }
}

# 3. 侧边栏控制
st.sidebar.title("CNPC Digital Twin")
sel_lang = st.sidebar.radio("Language / 语言", ["中文", "English"])
content = LANG[sel_lang]
page = st.sidebar.selectbox("Navigation", content["nav"])

# --- 逻辑分流 ---

if "总览" in page or "Overview" in page:
    st.title(content["hero_title"])
    st.image("https://via.placeholder.com/1000x300?text=CNPC+Hydrogen+Ecosystem+Twin", use_column_width=True)
    st.write("本平台集成了制、储、运三大环节的物理机理模型，支持中石油地下储氢（UHS）项目的数字化预研。")

elif "上游" in page or "Upstream" in page:
    st.header(content["u_h"])
    col1, col2 = st.columns(2)
    with col1:
        pw = st.number_input("风光电站规模 (MW)", value=10.0)
        tech = st.selectbox("电解槽技术", ["碱性 ALK", "质子交换膜 PEM"])
        tech_idx = 0 if "ALK" in tech else 1
    with col2:
        res = mechanics.calculate_h2_production(pw, tech_idx)
        st.metric("小时产氢量 (kg/h)", res)

elif "中游" in page or "Midstream" in page:
    st.header(content["m_h"])
    c1, c2 = st.columns([1, 2])
    with c1:
        d = st.slider("目标埋深 (m)", 500, 3000, 1200)
        pres, temp, cap = mechanics.get_storage_mechanics(d)
        st.write(f"### {content['calc']}")
        st.write(f"地层压力: **{pres} MPa**")
        st.write(f"地层温度: **{temp} °C**")
        st.info(f"容量系数: {cap} (反映存储密度)")
    with c2:
        st.subheader(content["3d_view"])
        x, y, z = mechanics.generate_3d_cavern_data()
        fig = go.Figure(data=[go.Mesh3d(x=x.flatten(), y=y.flatten(), z=z.flatten(),
                                       color='orange', opacity=0.6, intensity=z.flatten(), colorscale='Viridis')])
        fig.update_layout(scene=dict(aspectmode='data'))
        st.plotly_chart(fig, use_container_width=True)

elif "下游" in page or "Downstream" in page:
    st.header(content["d_h"])
    dist = st.slider("运输距离 (km)", 10, 500, 100)
    mode = st.radio("运输方式", ["长管拖车 (Truck)", "输氢管道 (Pipeline)"])
    m_idx = 0 if "Truck" in mode else 1
    loss = mechanics.transport_loss(dist, m_idx)
    st.warning(f"预计路途损耗率: {loss * 100}%")
    st.progress(loss * 10)