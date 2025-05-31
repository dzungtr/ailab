import getpass
import os

from langchain.chat_models import init_chat_model
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain_ollama import ChatOllama

memory = MemorySaver()
config = {"configurable": {"thread_id": "abc123"}}

if not os.environ.get("ANTHROPIC_API_KEY"):
  os.environ["ANTHROPIC_API_KE"] = getpass.getpass("Enter API key for Tavily: ")

search = TavilySearchResults(max_results=2)

# If we want, we can create other tools.
# Once we have all the tools we want, we can put them in a list that we will reference later.
tools = [search]


if not os.environ.get("ANTHROPIC_API_KEY"):
  os.environ["ANTHROPIC_API_KEY"] = getpass.getpass("Enter API key for Anthropic: ")


# model = init_chat_model("claude-3-5-sonnet-latest", model_provider="anthropic")
# model_with_tools = model.bind_tools(tools)

selfhost_model = ChatOllama(
    model = "llama3.1:8b",
    base_url = "http://localhost:11434",
    temperature = 0.8,
    num_predict = 256,
)

# response = model.invoke([HumanMessage(content="What is the wheather in Ho Chi Minh city, Viet Nam")])

# print(f"ContentString: {response.content}")
# print(f"ToolCalls: {response.tool_calls}")
agent_executor = create_react_agent(selfhost_model, tools, checkpointer=memory)



for chunk in agent_executor.stream(
    {"messages": [HumanMessage(content="what is the latest news about president Donald Trump")]},
    config,
):
    print(chunk)
    print("----")

