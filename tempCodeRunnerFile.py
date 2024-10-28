# feedback.py

from langchain_openai.llms import OpenAI  # 从 langchain_openai.llms 导入 OpenAI
from langchain.chains import LLMChain  # 从 langchain.chains 导入 LLMChain
from langchain.prompts import PromptTemplate  # 从 langchain.prompts 导入 PromptTemplate
import config

class FeedbackGenerator:
    def __init__(self):
        if not config.OPENAI_API_KEY:
            raise ValueError("OpenAI API 密钥未设置，请设置环境变量 OPENAI_API_KEY。")
        
        self.llm = OpenAI(
            temperature=0.7,
            api_key=config.OPENAI_API_KEY,
            base_url=config.OPENAI_API_BASE_URL  # 传递自定义的 Base URL
        )
        
        self.prompt = PromptTemplate(
            input_variables=["chat_history", "user_input"],
            template="""
            你是一个心理辅导师。以下是用户最近的心理活动记录：

            {chat_history}

            用户最新的心理活动记录：
            {user_input}

            请根据以上内容，提供有针对性和个性化的反馈和建议。
            """
        )
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)

    def generate_feedback(self, chat_history, user_input):
        feedback = self.chain.invoke({"chat_history": chat_history, "user_input": user_input})  # 使用 invoke 方法
        return feedback


## test it work
feedback = FeedbackGenerator()
chat_history = "2022-01-01 09:00:00: 用户说：我感到焦虑。"
user_input = "2022-01-01 09:30:00: 用户说：我感到压力很大。"
feedback.generate_feedback(chat_history, user_input)
print(feedback.generate_feedback(chat_history, user_input))