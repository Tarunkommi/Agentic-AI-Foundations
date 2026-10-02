import os
import math
from dotenv import load_dotenv

load_dotenv()

# Initialize the model 
from langchain.chat_models import init_chat_model

# Gemini_AI models: gemini-2.5-flash-lite is fast, cost-effective, and supports tool calling
model = init_chat_model("google_genai:gemini-2.5-flash-lite")


# Define your tools ("the hands that lets the LLM interact with the world")
from langchain.tools import tool

@tool
def add(a: float, b: float) -> float:
    """Add two numbers together.
    The agent will use this when it detects an addition problem"""
    return a + b

@tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers together.
    The agent will use this when it detects a multiplication problem"""
    return a * b

@tool 
def divide(a: float, b: float) -> float:
    """Divide the first number by the second.
    Includes error handling for division by zero"""
    if b == 0:
        return "Error: Cannot divide by zero"
    return str(a / b)

@tool
def square_root(x: float) -> float:
    """Calculate the square root of a number.
    Includes error handling for negative numbers"""
    if x < 0:
        return "Error: Cannot calculate the square root of a negative number"
    return math.sqrt(x)

# Combine the tools into a list
tools = [add, multiply, divide, square_root]

# Print available tools
print("Available tools:")
for t in tools:
    print(f"{t.name}: {t.description}")

print()

# Create an agent
# Note: LangGraph's create_react_agent is the standard tool-calling agent runner in modern LangChain
try:
    from langgraph.prebuilt import create_react_agent
    agent = create_react_agent(model=model, tools=tools)
except ImportError:
    from langchain.agents import create_agent
    agent = create_agent(model=model, tools=tools)

# Run the agent
def run_agent(question: str):
    """Run the agent and print a clean, beginner friendly execution trace"""
    print(f"\nUser: {question}")
    result = agent.invoke({
        "messages": [{"role": "user", "content": question}]
    })
    print("\nClean Agent Execution Trace")
    print("_" * 60)
    step = 1
    for msg in result["messages"]:
        # 1. human message : Original user question
        if msg.type == "human":
            print(f"{step}. User asked")
            print(f"   {msg.content}")
            step += 1

        elif msg.type == "ai" and getattr(msg, "tool_calls", None):
            for tool_call in msg.tool_calls:
                tool_name = tool_call['name']
                tool_args = tool_call.get('args', {})
                print(f"{step}. Agent decision: call {tool_name} with {tool_args}")
                step += 1

        elif msg.type == "tool":
            print(f"{step}. Tool Observation")
            print(f"   Tool returned: {msg.content}")
            step += 1

        elif msg.type == "ai" and msg.content:
            print(f"{step}. Final Response")
            if isinstance(msg.content, list):
                text = "".join(part.get("text", "") if isinstance(part, dict) else str(part) for part in msg.content)
                print(f"   {text.strip()}")
            else:
                print(f"   {msg.content}")
            step += 1

    print("=" * 60)
    print()

if __name__ == "__main__":
    run_agent("What is 48+37?")
    run_agent("What is 15 multiplied by 8, then divided by 3 ? ")
    run_agent("I have a rectangle with length 5 and width 4. What is the area and what is the square root of the area? ")
