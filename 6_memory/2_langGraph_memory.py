import uuid
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START,MessagesState,StateGraph
from langchain_openai import ChatOpenAI

def create_chat_app():
    
    workflow = StateGraph(state_schema= MessagesState)

    model = ChatOpenAI()
    
    def call_model(state: MessagesState):
        response = model.invoke(state['messages'])
        return {"messages": response}
    
    workflow.add_edge(START,'model')
    workflow.add_node("model", call_model)
    
    memory = MemorySaver()
    
    app = workflow.compile(checkpointer=memory)
    return app

def chat():
    
    app = create_chat_app()
    
    thread_id = uuid.uuid4()
    config = {"configurable" : {"thread_id": thread_id}}
    
    print("Chat Started. Type 'quit' to quit.")
    print('-' * 50)
    
    while True:
        
        user_input = input("\nYou: ")
        
        if user_input.lower() == 'quit':
            print("Exiting chat.")
            break
        
        input_message = HumanMessage(content=user_input)
        
        try:
            
            for event in app.stream(
                {"messages": [input_message]},
                config,
                stream_mode="values"
            ):
                response = event["messages"][-1].content
                print("\nAI:", response)
                
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again.")
            
if __name__ == "__main__":
    chat()