from langchain.agents import load_tools, initialize_agent, AgentType
from LLM.ChatGLM import ChatGLM
import os
from langchain.llms import OpenAI
# llm = OpenAI(temperature=0)

os.environ["SERPAPI_API_KEY"] = "..."

llm = ChatGLM.ZhipuAILLM(model="chatglm_std", temperature=0, zhipuai_api_key="5faffc5c543c469071127293daea56f1.PPR4nXe6b8Ds93tL")

tools = load_tools(["serpapi", "llm-math"], llm=llm)

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

agent.run("What was the high temperature in SF yesterday in Shanghai? What is that number raised to the .023 power?")