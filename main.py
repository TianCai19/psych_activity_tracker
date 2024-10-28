# main.py

import streamlit as st

def main():
    st.sidebar.title("导航")
    app_mode = st.sidebar.radio("选择页面", ["添加记录", "查看反馈", "管理记录"])

    if app_mode == "添加记录":
        from pages.Add_Record import add_record
        add_record()
    elif app_mode == "查看反馈":
        from pages.View_Feedback import view_feedback
        view_feedback()
    elif app_mode == "管理记录":
        from pages.Manage_Records import manage_records
        manage_records()

if __name__ == "__main__":
    st.set_page_config(page_title="心理活动记录与反馈系统", layout="wide")
    main()
