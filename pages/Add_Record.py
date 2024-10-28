# pages/Add_Record.py

import streamlit as st
from memory import MemoryManager

def add_record():
    st.header("添加心理活动记录")
    memory_manager = MemoryManager()

    user_input = st.text_area("请输入你的心理活动记录", height=150)

    if st.button("提交"):
        if user_input.strip() == "":
            st.warning("请输入有效的心理活动记录。")
        else:
            memory_manager.clean_old_entries()
            record_id = memory_manager.add_record(user_input)
            st.success(f"记录已成功添加！记录 ID: {record_id}")

if __name__ == "__main__":
    add_record()
