from langchain.agents import load_tools, initialize_agent, AgentType
from ChatGLM.ChatGLM import ChatGLM

import os
os.environ["SERPAPI_API_KEY"] = "..."

llm = ChatGLM(model="chatglm_6b")

tools = load_tools(["serpapi", "llm-math"], llm=llm)

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

agent.run("What was the high temperature in SF yesterday in Fahrenheit? What is that number raised to the .023 power?")