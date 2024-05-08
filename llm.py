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

api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

client = oai(organization='org_key')

llm = oai(temperature=0, model_name="gpt-3.5-turbo-instruct", max_tokens=1)
service_context = ServiceContext.from_defaults(llm=llm)
set_global_service_context(service_context=service_context)

a = SimpleDirectoryReader(input_dir="sec_filings/sec-edgar-filings/AAPL/10-k", recursive=True).load_data()
b = SimpleDirectoryReader(input_dir="sec_filings/sec-edgar-filings/MSFT/10-k", recursive=True).load_data()

print(f'Loaded Apple 10-K with {len(a)} pages')
print(f'Loaded Microsoft 10-K with {len(b)} pages')


"""Settings.llm = oai(model="text-embedding-3-small", temperature=0)
Settings.embed_model = OpenAIEmbedding(
    model="text-embedding-3-small", embed_batch_size=50
)
Settings.node_parser = SentenceSplitter(chunk_size=256, chunk_overlap=10)"""


a_index = VectorStoreIndex.from_documents(a, show_progress=True, insert_batch_size=512)
b_index = VectorStoreIndex.from_documents(b, show_progress=True, insert_batch_size=512)

a_engine = a_index.as_query_engine(similarity_top_k=3)
b_engine = b_index.as_query_engine(similarity_top_k=3)

response =  a_engine.aquery('What is the revenue of Apple in 2021? Answer in millions with page reference')
print(response)


