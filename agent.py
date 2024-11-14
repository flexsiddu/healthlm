import os
from dotenv import load_dotenv
from model import llm, tools, memory
from langchain.agents import AgentExecutor, create_tool_calling_agent
from prompt import prompt

load_dotenv(dotenv_path='E:\Coding_stuff\jobb_code\Japan-GPT-main\.env')

os.environ["LANGCHAIN_TRACING_V2"] = "true"

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")

agent = create_tool_calling_agent(llm, tools, prompt=prompt)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    memory=memory,
    verbose=False,
    return_intermediate_steps=True,
)