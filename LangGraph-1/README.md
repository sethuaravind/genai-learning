The code in this folder helps you to create basic langgraph model.

1. Create a file -  react.py - this contain the tools that you are going to use in the llm
    - Define what are the tools that you want to use in LLM with DocString
    - Define LLM model and bind the tools in LLM model
2. Create a file -  nodes.py - Define the nodes that you are going to use in the LangGraph
    - Create a reason node - basically a function: 
        - Prompting needs to be done in reason node
        - LLM needs to be in reason node - which provides the reason - LLM takes list as an input which contains - role, content (prompt), state["messages"]
        - LLM response should be stored in dictionary and return in reason node function
    - Create tool node: import the tools from 'react.py' file and apply it as input to the ToolNode (imported from langgraph)
3. Create main file - connecting the nodes
    - import all the nodes
    - Create StateGraph with MessagesState
    - Create nodes in StateGraph using imported node functions
    - Set entry point
    - Add conditional edges for reason agent and tool calling. Input for conditional edges are reason agent node, ACT node, END node (imported from langgraph) and should continue function (function that decides the next node)
    - 'Should continue' function uses the messagesState to decide the flow
    - Compile the graph





Nodes
MessageState - 
ToolNode - 