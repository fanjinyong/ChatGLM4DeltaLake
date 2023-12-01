from langchain import ConversationChain
from LLM.ChatGLM import ChatGLM
llm = ChatGLM(model="chatglm_6b")
conversation = ConversationChain(llm=llm, verbose=True)
output = conversation.predict(input="你能说下今天天气吗")
print(output)

output = conversation.predict(input="再说一句")
print(output)