from llama_index.indices.postprocessor import MetadataReplacementPostProcessor
import logging
from llama_index import SimpleDirectoryReader, VectorStoreIndex, GPTVectorStoreIndex
from llama_index.node_parser import SentenceWindowNodeParser
from llama_index.embeddings import OpenAIEmbedding
from llama_index.llms import OpenAI
from llama_index import ServiceContext, set_global_service_context
from llama_index.vector_stores import ChromaVectorStore
from langchain.embeddings import HuggingFaceEmbeddings
from llama_index.storage.storage_context import StorageContext
from llama_index.vector_stores import PineconeVectorStore
import os

import chromadb
import openai
import streamlit as st

from collection_manager import CollectionManager

openai.api_key = os.environ["OPENAI_API_KEY"]

# create the sentence window node parser w/ default settings
class LocalStorage:
    chroma_client = None

    def __init__(self):
        index_manager = CollectionManager()
        self.chroma_client = index_manager.get_client()

    def upload_data(self, dataPathFolder, collectionName):
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
            input_dir=dataPathFolder, required_exts=required_exts, recursive=True
        ).load_data()

        print(f"Loaded {len(documents)} documents.")

        chroma_collection = self.chroma_client.get_collection(collectionName)
        vector_store = ChromaVectorStore(chroma_collection=chroma_collection)

        storageContext = StorageContext.from_defaults(
            vector_store=vector_store
        )


        index = GPTVectorStoreIndex.from_documents(documents=documents,
                                                   storage_context=storageContext,
                                                   service_context=ctx)
        
        index.set_index_id(collectionName)
        index.storage_context.persist('./storage/index_storage/' + collectionName + '/')
