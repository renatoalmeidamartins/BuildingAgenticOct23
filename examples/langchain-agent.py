from langchain.agents import create_agent


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always rainy in {city}!"

agent = create_agent(model= "bedrock_converse:global.amazon.nova-2-lite-v1:0", 
                    tools=[get_weather])

#config = {"configurable": {"thread_id": str(uuid7())}}
prompt = "What's the weather in San Francisco?"
#prompt = "How are you?"

result = agent.invoke(
    {"messages": [{"role": "user", "content": prompt}]}
)
print(result["messages"][-1].content_blocks)
print("\n---------------------------------------\n")
print(result)
