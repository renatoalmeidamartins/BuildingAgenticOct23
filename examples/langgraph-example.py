from langchain_aws import ChatBedrock
from langgraph.graph import StateGraph, MessagesState

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always rainy in {city}!"



llm = ChatBedrock(model_id="global.amazon.nova-2-lite-v1:0") # your preferred model

tools = [get_weather] 
llm_with_tools = llm.bind_tools(tools)
def chatbot(state: MessagesState): 
    response = llm_with_tools.invoke(messages)
    return {"messages": [response]}

system_message = "You're a helpful assistant…"


graph_builder = StateGraph(MessagesState)
graph_builder.add_node("chatbot", chatbot) 
graph_builder.add_node("tools", ToolNode(tools))

graph_builder.add_conditional_edges( "chatbot", tools_condition )
graph_builder.add_edge("tools", "chatbot")

graph_builder.set_entry_point("chatbot")
graph_builder.compile()
