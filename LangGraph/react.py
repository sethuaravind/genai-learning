from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

load_dotenv()


@tool
def triple(num: float) -> float:
    """
    Returns the given float values multiplied by 3
    """
    return float(num) * 3


tools = [TavilySearch(max_results=1), triple]


llm = ChatOpenAI(temperature=0).bind_tools(tools)