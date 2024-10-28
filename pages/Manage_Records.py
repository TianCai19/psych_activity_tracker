# pages/Manage_Records.py

import streamlit as st
from memory import MemoryManager

def manage_records():
    st.header("管理心理活动记录")
    memory_manager = MemoryManager()

    records = memory_manager.get_all_records()

    if not records:
        st.info("当前没有心理活动记录。")
        return

    st.subheader("所有心理活动记录")

    for record in reversed(records):  # 显示最新的记录在上方
        with st.container():
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"**时间**: {record['timestamp']}")
                st.markdown(f"**内容**: {record['content']}")
            with col2:
                if st.button("删除", key=record['id']):
                    success = memory_manager.remove_record(record['id'])
                    if success:
                        st.success("记录已删除。")
                        st.experimental_rerun()
                    else:
                        st.error("删除记录失败。")

if __name__ == "__main__":
    manage_records()
