from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
import os
from getpass import getpass

# Set API key for DeepSeek
if not os.environ.get("DEEPSEEK_API_KEY"):
    os.environ["DEEPSEEK_API_KEY"] = getpass("Enter API key for DeepSeek: ")

# Initialize the DeepSeek model
model = ChatOpenAI(
    model_name="deepseek-chat",  # Replace with the specific DeepSeek model name if needed
    openai_api_key=os.environ["DEEPSEEK_API_KEY"],
    openai_api_base="https://api.deepseek.com/v1",  # Update to your DeepSeek base URL
    temperature=0.7,
)

# Conversation history to store past messages
conversation_history = []

# Function to add messages to the conversation history
def add_to_history(message):
    conversation_history.append(message)

# Function to simulate chatbot interaction with memory
def chat_with_memory(user_input):
    # Add the user's message to the history
    add_to_history(HumanMessage(content=user_input))
    
    # Call the model with the conversation history
    response = model.invoke(conversation_history)
    
    # Add the AI's response to the history
    add_to_history(AIMessage(content=response.content))
    
    # Return the AI's response
    return response.content

# Example usage
if __name__ == "__main__":
    print("Chatbot with Memory (DeepSeek). Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chat ended.")
            break
        ai_response = chat_with_memory(user_input)
        print(f"AI: {ai_response}")