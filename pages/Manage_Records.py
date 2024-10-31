# pages/Manage_Records.py

import streamlit as st
from memory import MemoryManager, ConversationManager

def manage_records():
    st.header("管理心理活动记录")
    memory_manager = MemoryManager()
    conversation_manager = ConversationManager()

    records = memory_manager.get_all_records()
    conversations = conversation_manager.get_all_conversations()

    if not records and not conversations:
        st.info("当前没有心理活动记录或对话。")
        return

    if records:
        st.subheader("所有心理活动记录")

        for record in reversed(records):
            with st.container():
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.markdown(f"**时间**: {record['timestamp']}")
                    st.markdown(f"**内容**: {record['content']}")
                with col2:
                    if st.button("删除记录", key=record['id']):
                        success = memory_manager.remove_record(record['id'])
                        if success:
                            st.success("记录已删除。")
                            st.experimental_rerun()
                        else:
                            st.error("删除记录失败。")

    if conversations:
        st.subheader("所有对话记录")

        for convo in reversed(conversations):
            with st.container():
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.markdown(f"**时间**: {convo['timestamp']}")
                    st.markdown(f"**用户输入**: {convo['user_input']}")
                    st.markdown(f"**反馈**: {convo['feedback']}")
                with col2:
                    if st.button("删除对话", key=convo['id']):
                        success = conversation_manager.remove_conversation(convo['id'])
                        if success:
                            st.success("对话已删除。")
                            st.experimental_rerun()
                        else:
                            st.error("删除对话失败。")

if __name__ == "__main__":
    manage_records()