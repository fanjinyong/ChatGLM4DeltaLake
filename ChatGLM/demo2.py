import zhipuai
from langchain.callbacks.manager import CallbackManagerForLLMRun

# https://open.bigmodel.cn/dev/api#http
zhipuai.api_key = "5faffc5c543c469071127293daea56f1.PPR4nXe6b8Ds93tL"
#
response = zhipuai.model_api.invoke(
    model="chatglm_6b",
    prompt=[{"role": "user", "content": "推荐下性价比高的笔记本电脑"}],
    temperature=0.9,
    top_p=0.7,
    incremental=True
)

print(response)




