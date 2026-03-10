import streamlit as st
import mechanics

# --- 1. 语言配置字典 ---
LANG = {
    "中文": {
        "title": "🛡️ 氢能全产业链数字化监管平台",
        "nav": ["总体概览", "上游：制氢机理", "中游：地下储氢", "下游：加氢输送"],
        "lang_label": "选择语言",
        "uhs_title": "中石油地下储氢 (UHS) 模块",
        "btn_calc": "开始计算机理数据"
    },
    "English": {
        "title": "🛡️ Hydrogen Value Chain Digital Platform",
        "nav": ["Overview", "Upstream: Generation", "Midstream: UHS", "Downstream: Delivery"],
        "lang_label": "Language",
        "uhs_title": "CNPC Underground Hydrogen Storage (UHS)",
        "btn_calc": "Calculate Mechanics"
    }
}

# --- 2. 界面初始化 ---
st.set_page_config(page_title="H2 Platform", layout="wide")

# 侧边栏：语言切换
selected_lang = st.sidebar.radio("🌐 Language/语言", ["中文", "English"])
content = LANG[selected_lang]

# 侧边栏：板块导航
st.sidebar.markdown("---")
page = st.sidebar.radio(content["lang_label"], content["nav"])

# --- 3. 核心板块内容 ---

if "总体概览" in page or "Overview" in page:
    st.title(content["title"])
    st.info("展示氢气从制备、地下储存到终端利用的全流程数字孪生。")
    # 这里可以放一张全产业链的示意图


elif "中游" in page or "Midstream" in page:
    st.title(content["uhs_title"])

    # 建立地下储氢的子框架
    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("📍 储层类型选择")
        storage_type = st.selectbox("类型", ["盐穴 (Salt Cavern)", "枯竭气田 (Depleted Gas Field)"])
        depth = st.slider("储层深度 (m)", 500, 3000, 1200)

    with col2:
        # 这里嵌入你最自豪的机理计算
        st.subheader("📊 机理分析结果")
        pressure = mechanics.get_pressure(depth)
        st.metric("预估地层压力 (Pressure)", f"{pressure} MPa")

    st.divider()
    st.write("### 3D 储层模拟预览")
    # 下一步我们将在这里嵌入 3D 模型代码
    st.warning("3D 渲染模块正在加载...")

else:
    st.title(page)
    st.write("该模块框架已建立，等待进一步机理代码嵌入。")