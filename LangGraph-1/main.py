import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langgraph.graph import MessagesState, StateGraph, END
from nodes import run_agent_reasoning, tool_node

load_dotenv()

AGENT_REASON = "AGENT_REASON"
ACT = "ACT"
LAST = -1

def should_continue(state :MessagesState) -> str:
    if state['messages'][LAST].tool_calls:
        return ACT
    return END

flow = StateGraph(MessagesState)

flow.add_node(AGENT_REASON, run_agent_reasoning)
flow.add_node(ACT, tool_node)
flow.set_entry_point(AGENT_REASON)

flow.add_conditional_edges(AGENT_REASON, should_continue, {END: END, ACT: ACT})

flow.add_edge(ACT, AGENT_REASON)

app = flow.compile()

app.get_graph().draw_mermaid_png(output_file_path="flow.png")

if __name__ == '__main__':
    res = app.invoke({"messages": HumanMessage(content="what is the current temperature in Tokyo in celsius? List it and cube it")})
    print(res["messages"][LAST].content)