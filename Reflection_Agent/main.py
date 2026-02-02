from typing import List, Sequence

from dotenv import load_dotenv
from langchain_core.messages import BaseMessage, HumanMessage
from chains import reflection_chain, generation_chain
from langgraph.graph import StateGraph, MessagesState, END, MessageGraph

load_dotenv()


REFLECT = 'reflect'
GENERATE = 'generate'

def should_continue(state: List[MessagesState]):
    if len(state) > 6:
        return END
    return REFLECT

def generation_node(state: Sequence[MessagesState]):
    return generation_chain.invoke({"messages": state})


def reflection_node(message: Sequence[MessagesState]) -> List[MessagesState]:
    res = reflection_chain.invoke({"messages": message})
    return [HumanMessage(content=res.content)]


builder = StateGraph(MessagesState)
builder.add_node(GENERATE, generation_node)
builder.set_entry_point(GENERATE)
builder.add_node(REFLECT, reflection_node)
builder.add_conditional_edges(GENERATE, should_continue, {END: END, REFLECT:REFLECT})
builder.add_edge(REFLECT, GENERATE)
graph = builder.compile()
# graph.get_graph().draw_mermaid_png(output_file_path='Reflection_Agent/flow.png')


inputs = [HumanMessage(content='''Make this tweet better:
- newly tool calling feature is seriously underrated.
After a long wait, it's here making the implementation of agents across different models with function calling. Made a video covering their newest blog post''')]
response = graph.invoke({'messages': inputs})