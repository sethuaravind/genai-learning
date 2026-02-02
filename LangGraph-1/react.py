from dotenv import load_dotenv
from langchain_core.tools import Tool, tool
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

load_dotenv()

@tool
def cube(num: float) -> float:
    """
    Calculating cube of the number
    """
    return num ** 3


tools = [TavilySearch(max_results=1), cube]

llm = ChatOpenAI(model='gpt-5-mini-2025-08-07', temperature=1).bind_tools(tools)