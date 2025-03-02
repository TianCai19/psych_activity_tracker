# feedback.py


from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

#from langchain.chains import LLMChain  # 从 langchain.chains 导入 LLMChain
from langchain.prompts import PromptTemplate  # 从 langchain.prompts 导入 PromptTemplate
import config
import logging



from prompt_template import prompt_template






# 配置日志记录
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FeedbackGenerator:
    def __init__(self, model_name="gpt-4o-mini"):
        """
        初始化 FeedbackGenerator。

        参数:
            model_name (str): 要使用的 OpenAI 模型名称。默认为 "gpt-3.5-turbo-instruct"。
        """
        if not config.OPENAI_API_KEY:
            logger.error("OpenAI API 密钥未设置。")
            raise ValueError("OpenAI API 密钥未设置，请设置环境变量 OPENAI_API_KEY。")
        
        logger.info(f"使用的 OpenAI API Base URL: {config.OPENAI_API_BASE_URL}")  # 调试信息
        logger.info(f"使用的 Anthropic API Base URL: {config.ANTHROPIC_API_BASE_URL}")  # 调试信息
        


        if "gpt" in model_name.lower():
            logger.info(f"选择的模型: {model_name}")  # 调试信息

            self.llm = ChatOpenAI(
                model_name=model_name,
                openai_api_key=config.OPENAI_API_KEY,
                openai_api_base=config.OPENAI_API_BASE_URL,
                temperature=config.TEMPERATURE,
                max_tokens=config.MAX_TOKENS,
                timeout=config.TIMEOUT,
                max_retries=config.MAX_RETRIES
            )
        elif "claude" in model_name.lower():
            logger.info(f"选择的模型: {model_name}")  # 调试信息
            self.llm= ChatAnthropic(
                model=model_name,
                temperature=config.TEMPERATURE,
                max_tokens=config.MAX_TOKENS,
                timeout=config.TIMEOUT,
                max_retries=config.MAX_RETRIES,
                api_key=config.ANTHROPIC_API_KEY,
                base_url=config.ANTHROPIC_API_BASE_URL,
                # other params...
            )
        elif "deepseek" in model_name.lower():
            logger.info(f"选择的模型: {model_name}")  # 调试信息
            self.llm = ChatOpenAI(
                model_name=model_name,
                openai_api_key=config.DEEPSEEK_API_KEY,
                openai_api_base=config.DEEPSEEK_API_BASE_URL,
                temperature=config.DEEPSEEK_TEMERATURE,
                max_tokens=config.MAX_TOKENS,
                timeout=config.TIMEOUT,
                max_retries=config.MAX_RETRIES
            )
        elif "llama" in model_name.lower():
            logger.info(f"选择的模型:ollama: {model_name}")  # 调试信息
            self.llm = ChatOpenAI(
                base_url=config.OLLAMA_API_BASE_URL,
                model=model_name,
                temperature=config.TEMPERATURE,
                #max_tokens=config.MAX_TOKENS
            )
        else:
            raise ValueError(f"Unsupported model_name: {model_name}")
        logger.info(f"Llama 模型初始化结果: {self.llm}")
        # 如果 LLM 初始化失败，抛出异常
        if not self.llm:
            raise ValueError("ChatOllama 初始化失败，请检查配置或模型名称。")

                
        
# 使用导入的提示模板
        self.prompt = prompt_template

        self.chain = self.prompt | self.llm  # 使用 | 运算符将提示模板和 LLMChain 连接起来
        logger.info("FeedbackGenerator 初始化成功。")

    def generate_feedback(self, chat_history, user_input):
        try:
            logger.info("生成反馈：")
            logger.info(f"Chat History: {chat_history}")
            logger.info(f"User Input: {user_input}")
            feedback = self.chain.invoke({"chat_history": chat_history, "user_input": user_input}).content  # 使用 invoke 方法
            logger.info("反馈生成成功。")
            return feedback
        except Exception as e:
            logger.error(f"生成反馈时发生错误：{e}")
            return f"生成反馈时发生错误：{e}"


# if main  test
if __name__ == "__main__":
    # feedback = FeedbackGenerator(model_name="claude-3-5-sonnet-20241022")
    # # feedback = FeedbackGenerator(model_name="gpt-4o-mini")
    chat_history = "2022-01-01 09:00:00: 用户说：我感到焦虑。"
    user_input = "2022-01-01 09:30:00: 用户说：我感到压力很大。"
    # print(feedback.generate_feedback(chat_history, user_input))
    
    # feedback = FeedbackGenerator(model_name="gpt-3.5-turbo")
    # print(feedback.generate_feedback(chat_history, user_input))
    
    feedback = FeedbackGenerator(model_name="llama3.2")
    print(feedback.generate_feedback(chat_history, user_input))
