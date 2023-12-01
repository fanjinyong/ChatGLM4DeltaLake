import openai

openai.api_key = "sk-NYsoG3VBKDiTuvdtC969F95aFc4f45379aD3854a93602327"
openai.api_base="https://key.wenwen-ai.com/v1"

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful teacher."},
    {"role": "user", "content": "tell me how to calculate 3+4？"}
  ]
)

print(completion)
# https://zhuanlan.zhihu.com/p/655954134