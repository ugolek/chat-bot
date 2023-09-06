from llama_index.indices.postprocessor import MetadataReplacementPostProcessor
import logging
from llama_index import SimpleDirectoryReader, VectorStoreIndex
from llama_index.node_parser import SentenceWindowNodeParser
from llama_index.embeddings import OpenAIEmbedding
from llama_index.llms import OpenAI
from llama_index import ServiceContext, set_global_service_context
from langchain.embeddings import HuggingFaceEmbeddings
from streamlit_chat import message
from llama_index.storage.storage_context import StorageContext
from llama_index.vector_stores import PineconeVectorStore
import os

import openai
import streamlit as st
import pinecone

os.environ["OPENAI_API_KEY"] = "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"
openai.api_key = os.environ["OPENAI_API_KEY"]



# Initialize Pinecone
print("Initializing Pinecone...")
pinecone.init(api_key="cb0cdcdf-2076-415d-a700-fd16c759e973",
              environment="us-west4-gcp-free")
index_name = "chatbot-index"

# Check if the index exists. If not, create it.
if index_name not in pinecone.list_indexes():
    print(f"Index {index_name} not found, creating it...")
    pinecone.create_index(index_name, metric="cosine",
                          shards=1, dimension=768)
    print(f"Index {index_name} created.")
else:
    print(f"Index {index_name} already exists.")

# Get a Pinecone index instance
print("Getting Pinecone index instance...")
pinecone_index = pinecone.Index(index_name=index_name)
print("Pinecone index instance obtained.")

# create the sentence window node parser w/ default settings
node_parser = SentenceWindowNodeParser.from_defaults(
    window_size=3,
    window_metadata_key="window",
    original_text_metadata_key="original_text",
)

llm = OpenAI(model="gpt-3.5-turbo", temperature=0.1)
ctx = ServiceContext.from_defaults(
    llm=llm,
    embed_model=HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-mpnet-base-v2"
    ),
    node_parser=node_parser,
)

required_exts = [".md"]

print("Loading documents from directory...")

documents = SimpleDirectoryReader(
    input_dir="./data", required_exts=required_exts, recursive=True
).load_data()

print(f"Loaded {len(documents)} documents.")

vector_store = PineconeVectorStore(pinecone_index=pinecone_index)
storageContext = StorageContext.from_defaults(
    vector_store=vector_store
)

index = VectorStoreIndex.from_documents(
    storage_context=storageContext, service_context=ctx, documents=documents)

