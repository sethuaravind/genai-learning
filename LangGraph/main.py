from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langgraph.graph import MessagesState, StateGraph, END


from nodes import run_agent_reasoning, tool_nodes


load_dotenv()


def should_continue(state: MessagesState) -> str:
    if not state['messages'][LAST].tool_calls:
        return END
    return ACT



AGENT_REASON = 'agent_reason'
ACT = 'act'
LAST = -1

flow = StateGraph(MessagesState)

flow.add_node(AGENT_REASON, run_agent_reasoning)
flow.set_entry_point(AGENT_REASON)
flow.add_node(ACT, tool_nodes)

flow.add_conditional_edges(AGENT_REASON, should_continue, {END: END, ACT:ACT})

flow.add_edge(ACT, AGENT_REASON)

app = flow.compile()
# app.get_graph().draw_mermaid_png(output_file_path='flow_corrected.png')


res = app.invoke({'messages': [HumanMessage(content='what is the temperature in tokyo? List it and triple it')]})
print(res["messages"][LAST].content)