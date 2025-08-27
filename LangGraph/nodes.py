from dotenv import load_dotenv
from langgraph.graph import MessagesState
from langgraph.prebuilt import ToolNode

from react import llm, tools

SYSTEM_MESSAGE = "You are a useful assistance that uses the tool to answer the question"


def run_agent_reasoning(state: MessagesState) -> MessagesState:
    "Run the agent reasoning code"
    response = llm.invoke([{'role': 'system', 'content': SYSTEM_MESSAGE}, *state['messages']])

    return {'messages': [response]}

tool_nodes = ToolNode(tools)