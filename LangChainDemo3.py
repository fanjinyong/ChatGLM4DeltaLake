from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.document_loaders import TextLoader
import zhipuai
from LLM.ChatGLM.EmbeddingModel import ZhipuAIEmbeddings

# from langchain.embeddings import OpenAIEmbeddings
#
# embeddings = OpenAIEmbeddings()

loader = TextLoader("test.txt", encoding="utf-8")
documents = loader.load()
print(documents)
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

with open('test.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
s = ""
for line in lines:
    s += line

zhipuai.api_key = "5faffc5c543c469071127293daea56f1.PPR4nXe6b8Ds93tL"
# 请求模型
zhipuai_embeddings = ZhipuAIEmbeddings(zhipuai_api_key=zhipuai.api_key)
query_embedding = zhipuai_embeddings.embed_query('你好')
print(query_embedding[:10])
# db = FAISS.from_texts(s, zhipuai_embeddings)
#
# query = "被摘牌的中华老字号有谁？"
# docs = db.similarity_search(query)
#
# print(docs)
