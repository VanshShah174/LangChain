from dotenv import load_dotenv
from langchain_openai import ChatOpenAI 
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

load_dotenv()

model = ChatOpenAI(model="meta-llama/llama-3-8b-instruct")

chat_history = []

system_message = SystemMessage(content="You are a helpful AI assistant.")
chat_history.append(system_message)

while True:
    query = input("You: ")
    if query.lower() == "exit":
        break
    chat_history.append(HumanMessage(content=query))
    
    result = model.invoke(chat_history)
    response= result.content
    chat_history.append(AIMessage(content=response))
    
    print(f"AI: {response}")
    
print("----Message History---")
print(chat_history)