import os
import openai
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from langchain.embeddings.openai import OpenAIEmbeddings

#.environ["OPENAI_API_KEY"] = "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"
# os.environ["http_proxy"] = "http://localhost:7890"
# os.environ["https_proxy"] = "http://localhost:7890"
#
# # embeddings = OpenAIEmbeddings(openai_api_key=os.environ["OPENAI_API_KEY"])
# # print(embeddings)
#
# llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
#
# while True:
#     human_input = input("(human): ")
#     human_input = [HumanMessage(content=human_input)]
#     ai_output = llm(human_input)
#     print(f"(ai): {ai_output.content}")
# openai.api_key = "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"
# def chat_gpt(prompt):
#     # 你的问题
#     prompt = prompt
#
#     # 调用 ChatGPT 接口
#     model_engine = "text-davinci-003"
#     completion = openai.Completion.create(
#         engine=model_engine,
#         prompt=prompt,
#         max_tokens=1024,
#         n=1,
#         stop=None,
#         temperature=0.5,
#         timeout=1000,
#     )
#
#     response = completion.choices[0].text
#     print(response)
#
# chat_gpt("请把“我的家在东北，松花江上呐”这句话写成问题")

openai.api_key = "sk-NYsoG3VBKDiTuvdtC969F95aFc4f45379aD3854a93602327"
openai.api_base="https://key.wenwen-ai.com/v1"

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)