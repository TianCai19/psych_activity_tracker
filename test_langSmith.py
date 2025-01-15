from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import os
from getpass import getpass

os.environ["LANGSMITH_PROJECT"] = "DeepSeek Chat Assistant"

import getpass
import os

#api in the .zshrc file
# os.environ["LANGSMITH_TRACING"] = "true"
# os.environ["LANGSMITH_API_KEY"] = getpass.getpass()

# Set API key for DeepSeek
if not os.environ.get("DEEPSEEK_API_KEY"):
    os.environ["DEEPSEEK_API_KEY"] = getpass("Enter API key for DeepSeek: ")

# Initialize DeepSeek Model
model = ChatOpenAI(
    model_name="deepseek-chat",
    openai_api_key=os.environ["DEEPSEEK_API_KEY"],
    openai_api_base="https://api.deepseek.com/v1",  # Update to your DeepSeek base URL
    temperature=0.7,
    max_tokens=300
)

# Define Prompt Template
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Respond conversationally."),
    ("user", "{text}")
])

# Conversation Loop
print("Chat with DeepSeek Assistant! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    
    # Format the prompt and generate response
    prompt = prompt_template.invoke({"text": user_input})
    response = model.invoke(prompt)
    print(f"Assistant: {response.content}")