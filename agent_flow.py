# agent_flow.py
from langgraph.graph import StateGraph
from research_agent import perform_research
from answer_agent import draft_answer
from typing import TypedDict

# Define the state schema
class AgentState(TypedDict):
    query: str
    context: str
    answer: str

# graph = LangGraph()
graph = StateGraph(AgentState)

# Add agents as nodes
graph.add_node("researcher", perform_research)
graph.add_node("answer_drafter", draft_answer)

graph.set_entry_point("researcher")
graph.add_edge("researcher", "answer_drafter")
graph.set_finish_point("answer_drafter")

# Compile the graph
compiled_graph = graph.compile()
print("21",compiled_graph)

# # Define how the information flows
# graph.add_edge("researcher", "answer_drafter")

# Run the process
def run_agents(query):
    result = compiled_graph.invoke({"query": query, "context": "", "answer": ""})
    return result.get("answer")

# Test run
if __name__ == "__main__":
    query = "What does a UI/UX designer do?"
    # query = "What is AI?"
    final_answer = run_agents(query)
    print("Final Answer:", final_answer)