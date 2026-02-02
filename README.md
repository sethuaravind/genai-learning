# genai-learning
This repo is to learn the langchain implementaton, along with some fundamental featuers


# Directories
- LangGraph & LangGraph-1 - both are used for the basic langgraph method - use LangGraph-1 for better understanding
- Reflection_Agent - Incomplete
- Reflexion_agent - Incomplete


# Table of Content

- Vector DB
- RAG
- PDF Reader
- CSV Reader
- LangGraph
- Reflection Agent



# LangGraph - Simple Example
LangGraph is power library of Langchain that helps to create a flow for agentic AI to perform series of tasks.

There are 6 types of code module
1.	Code – Fully rely on human code
2.	LLM call – Using LLM for simple task like summarization
3.	Chain – One direction flow
4.	Router – eg RAG
5.	State Machine – Cycle based decision - Langgraph
6.	Autonomous – Fully autonomous – RGPT

Graph – Data Structure
State Machine – State Machine is computation model consists of states and transfer between those states that helps in sequence of computer tasks. 

## Flow Engineering
- Flow Engineering is systematic approach for development that incorporate AI decision making. 
- AutoGPT and BabyAGI involves in developing the long term planning, they chunk the task and operate on it.
- Flow Engineering consists of planning and testing phase to develop the code like human.
- Developer write state, what is the flow and what needs to be done. LLM will decide which flow to take.


## Core Components

-	Nodes – Python Functions
-	Edges – Connect those nodes
-	Conditional Edges – helps to make decision to select which node
-	Start node and end node – No operation
-	Stage or Agent State – dict (eg: node result, chat history)

Node’s function gets the input as state (GraphState) and return output as dict.

Pro's of LangGraph
-	Cyclic Graph
-	Human in the loop
-	Persistance


#### Code Structure
- import tools from langchain_core.tools
- create tool with tool decorator
- Store tools in tools list


### File Structure
react.py -> LLM initialization & tools list
node.py -> agent reasoning function & tool nodes
main.py -> Graph development


### Simple Graph Creation Requirements
- Initialize Agent Reasoning node
- Set entry Point
- Add ACT node
- Set Conditional Edges
- Create edges between ACT and Agent reasoning
- Compile the graph
- Draw the flow


# Reflection Agent
Reflection agent improves the quality and success rate of the agent.

## Template
- Create generation prompt and reflection prompt
- Create generation chain and reflection chain
- Create generation node and reflection node
- Define the graph
- Create nodes
- Set entry point
- Set conditional edges
- Set edges
- Compile the graph
- Draw the graph


## Common Mistake
- Use 'ChatMessagePromptTemplate' instead of 'ChatPromptTemplate'

## Code Structure
- Chains -> contains reflection & generation agents
- main -> Contain langgraph

## Functions
ChatTemplatePrompt.from_messages -> This is not in general function list -> input structure is [('{who uses}', '{message}'), {messageplaceholder}]