from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core.node_parser import SentenceSplitter
from llama_index.llms.openai import OpenAI as oai
from openai import OpenAI
from langchain_openai import OpenAI as oi
from llama_index.core import Settings
import openai
import os
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, ServiceContext
from llama_index.core import set_global_service_context
from llama_index.core.response.pprint_utils import pprint_response
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.query_engine import SubQuestionQueryEngine
from sec_downloader import a,b

OpenAI.api_key =os.getenv("OPENAI_API_KEY")
oai.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'), organization='org_key')

Settings.llm = oai(model="gpt-3.5-turbo", temperature=0.1, max_tokens=1, api_key=os.getenv('OPENAI_API_KEY'))
Settings.embed_model = OpenAIEmbedding(
    model="text-embedding-3-small", embed_batch_size=100, api_key= os.getenv('OPENAI_API_KEY')
)
Settings.node_parser = SentenceSplitter(chunk_size=1024, chunk_overlap=20)


a_index = VectorStoreIndex.from_documents(a, show_progress=True, insert_batch_size=512)
b_index = VectorStoreIndex.from_documents(b, show_progress=True, insert_batch_size=512)

a_engine = a_index.as_query_engine(similarity_top_k=3)
b_engine = b_index.as_query_engine(similarity_top_k=3)

response =  a_engine.aquery('What is the revenue of Apple in 2021? Answer in millions with page reference')
print(response)


