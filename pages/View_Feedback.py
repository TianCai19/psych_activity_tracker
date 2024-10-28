# pages/View_Feedback.py

import streamlit as st
from memory import MemoryManager
from feedback import FeedbackGenerator
import time
import config

def view_feedback():
    st.header("查看心理反馈")
    memory_manager = MemoryManager()
    
    # 获取可用的模型列表
    available_models = config.AVAILABLE_MODELS
    
    # 添加一个选择模型的下拉菜单
    model_name = st.selectbox("选择用于生成反馈的模型", available_models, index=0)
    
    # 初始化 FeedbackGenerator，传入选择的模型
    feedback_generator = FeedbackGenerator(model_name=model_name)

    records = memory_manager.get_all_records()

    if not records:
        st.info("当前没有心理活动记录，请先添加记录。")
        return

    # 显示最近的记录
    st.subheader("最近的心理活动记录")
    for record in reversed(records[-10:]):  # 显示最近10条
        st.write(f"{record['timestamp']}: {record['content']}")

    # 获取最新的用户输入
    latest_entry = records[-1]['content']

    # 生成反馈
    with st.spinner("生成反馈中..."):
        # 构建聊天历史字符串
        chat_history = "\n".join([f"{r['timestamp']}: {r['content']}" for r in records])
        feedback = feedback_generator.generate_feedback(chat_history, latest_entry)
        time.sleep(1)  # 模拟处理时间

    st.success("反馈生成成功！")
    st.write("**反馈：**")
    st.write(feedback)

if __name__ == "__main__":
    view_feedback()
