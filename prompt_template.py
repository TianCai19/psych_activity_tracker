# FILE: prompt_template.py

from langchain.prompts import PromptTemplate

# 定义提示模板
prompt_template = PromptTemplate(
    input_variables=["chat_history", "user_input"],
    template="""
    你是一个心理辅导师。以下是用户最近的心理活动记录：

    {chat_history}

    用户最新的心理活动记录：
    {user_input}

    请根据以上内容，提供有针对性和个性化的反馈和建议。
    根据最新的活动，给出一个最新活动的反馈
    """
)