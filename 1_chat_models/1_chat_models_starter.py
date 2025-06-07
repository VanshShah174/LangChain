# import os

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv


load_dotenv()

llm = ChatOpenAI(
    model="meta-llama/llama-3-8b-instruct",
    temperature=0.7,
    # base_url=os.environ["OPENAI_API_BASE"],  # 👈 Explicit base_url for OpenRouter
    # api_key=os.environ["OPENAI_API_KEY"],    # 👈 Explicit API key
)

result = llm.invoke("How can I learn more about langchain?")

print(result.content)
