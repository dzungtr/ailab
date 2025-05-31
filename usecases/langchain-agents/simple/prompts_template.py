import getpass
import os
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage

try:
    # load environment variables from .env file (requires `python-dotenv`)
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

os.environ["LANGSMITH_TRACING"] = "true"
if "LANGSMITH_API_KEY" not in os.environ:
    os.environ["LANGSMITH_API_KEY"] = getpass.getpass(
        prompt="Enter your LangSmith API key (optional): "
    )
if "LANGSMITH_PROJECT" not in os.environ:
    os.environ["LANGSMITH_PROJECT"] = getpass.getpass(
        prompt='Enter your LangSmith Project Name (default = "default"): '
    )
    if not os.environ.get("LANGSMITH_PROJECT"):
        os.environ["LANGSMITH_PROJECT"] = "default"

selfhost_model = ChatOllama(
    model = "qwen3:latest",
    base_url = "http://localhost:11434",
    temperature = 0.8,
    num_predict = 256,
)


messages = [
    SystemMessage("You are a translator. You will receive a message in English and will translate it to Vietnamese. You will based on the context of the conversation to choose the proper translation. reply with the final translation only"),
    SystemMessage("This conversation is happening in the office on normal working day"),
    HumanMessage("HI how are you today?"),
]

response = selfhost_model.invoke(messages)

# Extract only the message after </think> tag
content = response.content
if "</think>" in content:
    final_message = content.split("</think>")[1].strip()
else:
    final_message = content

print(f"response: {final_message}")
