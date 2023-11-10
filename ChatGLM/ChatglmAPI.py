import zhipuai

class ChatglmAPI(object):
    api_key = "5faffc5c543c469071127293daea56f1.PPR4nXe6b8Ds93tL"
    text = []
    model = "chatglm_6b"
    temperature = 0.9
    top_p = 0.7

    def __init__(self, role, content) -> None:
        self.text.clear()
        self.get_text(role, content)

    def get_text(self, role, content) -> None:
        role_content: dict[str, any] = {"role": role, "content": content}
        self.text.append(role_content)
        self.check_length()

    def get_length(self) -> int:
        length = 0
        for role_content in self.text:
            length += len(role_content["content"])
        return length

    def check_length(self) -> None:
        while self.get_length() > 8000:
            del self.text[0]

    def set_params(self, model, temperature, top_p) -> None:
        self.model = model
        self.temperature = temperature
        self.top_p = top_p

    def response(self) -> str:
        zhipuai.api_key = self.api_key
        #return "gggg"
        result = zhipuai.model_api.invoke(
            model=self.model,
            prompt=self.text,
            temperature=self.temperature,
            top_p=self.top_p,
            incremental=True
        )
        print(result)
        return result['data']['choices'][0]['content']
