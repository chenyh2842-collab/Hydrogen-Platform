import streamlit as st
import mechanics
import plotly.graph_objects as go
import pandas as pd

# 1. PAGE CONFIGURATION & THEME INJECTION
st.set_page_config(page_title="H2 VISION: GLOBAL TWIN", layout="wide", initial_sidebar_state="expanded")

# Cyber-Tech CSS
st.markdown("""
    <style>
    .main { background: radial-gradient(circle, #001529 0%, #000811 100%); color: #e6f7ff; }
    [data-testid="stSidebar"] { background-color: #000a1a !important; border-right: 1px solid #00f2ff; }
    .stMetric { background: rgba(0, 242, 255, 0.03); border: 1px solid #00f2ff; border-radius: 15px; padding: 20px; box-shadow: 0 0 20px rgba(0, 242, 255, 0.1); }
    h1, h2, h3 { color: #00f2ff; text-shadow: 0 0 15px rgba(0, 242, 255, 0.6); font-family: 'Orbitron', sans-serif; }
    .stSlider [data-baseweb="slider"] { margin-bottom: 20px; }
    .stButton>button { background: transparent; color: #00f2ff; border: 1px solid #00f2ff; border-radius: 5px; width: 100%; transition: 0.5s; }
    .stButton>button:hover { background: #00f2ff; color: #000; box-shadow: 0 0 30px #00f2ff; }
    </style>
    """, unsafe_allow_html=True)

# 2. MULTILINGUAL ENGINE
if 'lang' not in st.session_state: st.session_state.lang = "English"

UI = {
    "English": {
        "title": "⚡ H2 VALUE CHAIN DIGITAL TWIN",
        "tag": "FUTURE ENERGY INTELLIGENCE TERMINAL v3.0",
        "nav": ["SYSTEM OVERVIEW", "UPSTREAM: PRODUCTION", "MIDSTREAM: UHS STORAGE", "DOWNSTREAM: LOGISTICS",
                "ECONOMICS"],
        "lang_btn": "切换至中文 (Switch to Chinese)",
        "metrics": ["Global Purity", "Active Storage", "Efficiency", "Mass Flow"],
        "3d_btn": "INITIATE NEURAL RENDERING",
        "footer": "CNPC Hydrogen Lab - Quantum Simulation Active"
    },
    "中文": {
        "title": "⚡ 氢能全产业链数字孪生平台",
        "tag": "未来能源智能控制终端 v3.0",
        "nav": ["系统总览", "上游：制氢仿真", "中游：地下储氢机理", "下游：物流监控", "经济性分析"],
        "lang_btn": "Switch to English (切换至英文)",
        "metrics": ["全球纯度", "实时储量", "转化效率", "质量流量"],
        "3d_btn": "启动神经渲染分析",
        "footer": "中石油氢能实验室 - 量子模拟运行中"
    }
}

# 3. SIDEBAR NAVIGATION
with st.sidebar:
    st.markdown("### `USER ACCESS`")
    if st.button(UI[st.session_state.lang]["lang_btn"]):
        st.session_state.lang = "中文" if st.session_state.lang == "English" else "English"

    C = UI[st.session_state.lang]
    st.divider()
    page = st.radio("CORE MODULES", C["nav"])
    st.divider()
    st.caption(C["footer"])

# 4. MODULE ROUTING
st.title(C["title"])
st.caption(f"ID: CNPC-H2-2050 | STATUS: {C['tag']}")

if "OVERVIEW" in page or "总览" in page:
    st.write("---")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric(C["metrics"][0], "99.999%", "Optimal")
    m2.metric(C["metrics"][1], "1.42M Tons", "+3.2%")
    m3.metric("System Load", "42%", "-5%")
    m4.metric("Carbon Offset", "124k Tons", "Live")

    st.write("---")
    st.subheader("Global Hydrogen Infrastructure Map")
    st.info("Neural link established. Global storage nodes are operating within normal parameters.")

elif "PRODUCTION" in page or "制氢" in page:
    st.subheader("Green Hydrogen Production Simulation")
    l, r = st.columns([1, 2])
    with l:
        pw = st.slider("Input Power (MW)", 1, 100, 20)
        tech = st.selectbox("Electrolyzer Tech", ["ALK", "PEM"])
        temp = st.slider("Cell Temperature (°C)", 20, 100, 65)
    with r:
        eff, flow = mechanics.simulate_electrolysis(pw, tech, temp)
        st.metric(C["metrics"][2], f"{eff}%")
        st.metric(C["metrics"][3], f"{flow} kg/h")


elif "STORAGE" in page or "储氢" in page:
    st.subheader("Underground Hydrogen Storage (UHS) Mechanics")
    l, r = st.columns([1, 2])
    with l:
        depth = st.number_input("Target Formation Depth (m)", value=1200)
        p, t, dens = mechanics.get_uhs_physics(depth)
        st.metric("Pressure (MPa)", p)
        st.metric("Temperature (°C)", t)
        st.metric("Gas Density (kg/m³)", dens)
    with r:
        if st.button(C["3d_btn"]):
            X, Y, Z = mechanics.generate_3d_cavern_mesh()
            fig = go.Figure(data=[go.Surface(x=X, y=Y, z=Z, colorscale='Electric', showscale=False)])
            fig.update_layout(scene=dict(xaxis_visible=False, yaxis_visible=False, zaxis_title='DEPTH (m)'),
                              template="plotly_dark", margin=dict(l=0, r=0, b=0, t=0))
            st.plotly_chart(fig, use_container_width=True)


elif "ECONOMICS" in page or "经济" in page:
    st.subheader("Financial Feasibility & Strategy")
    cap = st.slider("Storage Capacity (Tons)", 100, 5000, 1000)
    d_target = st.slider("Burial Depth (m)", 500, 3000, 1200)

    capex, save, roi = mechanics.get_financial_metrics(cap, d_target)

    c1, c2, c3 = st.columns(3)
    c1.metric("Project CAPEX", f"${capex}M")
    c2.metric("Est. Savings vs Tanks", f"${save}M")
    c3.metric("ROI Period", f"{roi} Years")

    st.divider()
    st.progress(min(1.0, 10 / roi))
    st.caption("Investment Viability Index (Green = High)")

elif "LOGISTICS" in page or "物流" in page:
    st.subheader("Downstream Delivery & Safety Pipeline")
    l, r = st.columns(2)
    with l:
        length = st.slider("Pipeline Length (km)", 10, 500, 150)
        in_p = st.slider("Inlet Pressure (MPa)", 2.0, 10.0, 5.0)
    with r:
        out_p, risk = mechanics.calculate_pipe_flow(in_p, length, 200)
        st.metric("Outlet Pressure", f"{out_p} MPa")
        st.write(f"Risk Index: {risk}%")
        st.error("Extreme Risk Zone" if risk > 80 else "Safe Operation")