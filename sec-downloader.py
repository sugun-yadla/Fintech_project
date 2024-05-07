from dotenv import load_dotenv
import openai
import os
from langchain_openai import OpenAI
from sec_edgar_downloader import Downloader
from llama_index.core import SimpleDirectoryReader, ServiceContext, VectorStoreIndex
from llama_index.core import set_global_service_context
from llama_index.core.response.pprint_utils import pprint_response
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.query_engine import SubQuestionQueryEngine

openai.api_key = 'sk-proj-hKQC4BE0U48yugBnJbc2T3BlbkFJTyNFZUpT1vjiw2u1r8AQ'


a = SimpleDirectoryReader(input_dir="sec_filings/sec-edgar-filings/AAPL/10-k", recursive=True).load_data()
b = SimpleDirectoryReader(input_dir="sec_filings/sec-edgar-filings/MSFT/10-k", recursive=True).load_data()
print(f'Loaded apple 10-K with {len(a)} pages')
print(f'Loaded microsoft 10-K with {len(b)} pages')

llm = OpenAI(temperature=0, model_name="gpt-4",  max_tokens=-1)

service_context = ServiceContext.from_defaults(llm=llm)
set_global_service_context(service_context=service_context)





# List of company tickers
companies = ['AAPL', 'MSFT']  # replace with your companies

# Directory to save filings
dir_to_save = 'sec_filings'

# Ensure the directory exists
os.makedirs(dir_to_save, exist_ok=True)


# Loop over each company
for company in companies:
    dl = Downloader("University of Massachusetts Amherst", 'syadla@umass.edu', dir_to_save)
    for year in range(1995, 2024):
    # Loop over each year from 1995 through 2023
        # Download the 10-K filings
        dl.get("10-K", company, limit=29, after=f"{year}-01-01", before=f"{year}-12-31")

print(f'Loaded lyft 10-K with {len(a)} pages')
print(f'Loaded Uber 10-K with {len(b)} pages')


