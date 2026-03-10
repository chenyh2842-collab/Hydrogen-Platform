import streamlit as st

# 1. 页面基本设置
st.set_page_config(page_title="Yonghui 的氢能研究空间", layout="wide", page_icon="🚀")

# 2. 侧边栏导航
st.sidebar.title("导航中心")
page = st.sidebar.radio("前往：", ["个人主页", "氢能实验台", "研究成果", "联系我"])

# 3. 页面内容分发逻辑
if page == "个人主页":
    st.title("👋 欢迎来到我的氢能探索空间")
    col1, col2 = st.columns([1, 2])
    with col1:
        # 这里可以放你的照片或头像
        st.image("https://via.placeholder.com/200", caption="氢能研究者")
    with col2:
        st.subheader("关于我")
        st.write("我是 Yonghui，目前正在致力于地下氢气储存（UHS）的机理研究和数字化平台开发。")
        st.write("🎯 **研究方向：** 盐穴储氢、多相流数值模拟、Vibe Coding。")

elif page == "氢能实验台":
    # 这里直接调用你之前的机理模块
    import mechanics
    st.title("🧪 地下储氢仿真实验室")
    depth = st.slider("选择深度", 500, 2000)
    st.metric("预估地层压力", f"{mechanics.get_pressure(depth)} MPa")

elif page == "研究成果":
    st.title("📚 发表论文与项目")
    st.info("这里可以列出你的 PDF 文档、PPT 或者是 GitHub 代码库链接。")

elif page == "联系我":
    st.title("📬 保持联系")
    with st.form("contact_form"):
        name = st.text_input("姓名")
        message = st.text_area("留言")
        if st.form_submit_button("发送"):
            st.success(f"感谢 {name}，消息已收到（模拟）！")