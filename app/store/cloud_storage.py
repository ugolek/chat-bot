from llama_index.indices.postprocessor import MetadataReplacementPostProcessor
import logging
from llama_index import SimpleDirectoryReader, VectorStoreIndex, GPTVectorStoreIndex, LLMPredictor
from llama_index.node_parser import SentenceWindowNodeParser
from llama_index.embeddings import OpenAIEmbedding
from llama_index.llms import OpenAI
from llama_index import ServiceContext, LangchainEmbedding, load_index_from_storage
from llama_index.vector_stores import ChromaVectorStore
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import HuggingFaceEmbeddings
from llama_index.storage.storage_context import StorageContext
from llama_index.vector_stores import PineconeVectorStore
from llama_index.storage.index_store import MongoIndexStore
import os
import chromadb
import openai
import streamlit as st
import pinecone

from collection_manager import CollectionManager

openai.api_key = os.environ["OPENAI_API_KEY"]

# create the sentence window node parser w/ default settings

PINECONE_INDEX_NAME = "chatbot-index"


class CloudStorage:
    def __init__(self):
        pinecone.init(api_key=os.environ["PINECONE_API"],
                      environment=os.environ["PINECONE_ENVIRONMENT"])
        index_name = PINECONE_INDEX_NAME

        if index_name not in pinecone.list_indexes():
            print(f"Index {index_name} not found, creating it...")
            pinecone.create_index(index_name, metric="cosine",
                                  shards=1, dimension=768)
            print(f"Index {index_name} created.")
        else:
            print(f"Index {index_name} already exists.")

        self.pinecone_index = pinecone.Index(index_name=index_name)

    def upload_data(self, dataPathFolder, collectionName):
        node_parser = SentenceWindowNodeParser.from_defaults(
            window_size=3,
            window_metadata_key="window",
            original_text_metadata_key="original_text",
        )


        llm_predictor_chat = LLMPredictor(llm=ChatOpenAI(
            temperature=0.2, model_name="gpt-3.5-turbo"))
        embed_model = LangchainEmbedding(HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-mpnet-base-v2"))

        service_context = ServiceContext.from_defaults(
            llm_predictor=llm_predictor_chat, embed_model=embed_model, node_parser=node_parser)

        index_store = MongoIndexStore.from_uri(
            uri="mongodb+srv://cardUser:cardUser@ugolekcluster.qebqp.mongodb.net/?retryWrites=true&w=majority",
            db_name="ugolekCluster")
        vector_store = PineconeVectorStore(pinecone_index=self.pinecone_index)
        storage_context = StorageContext.from_defaults(
            index_store=index_store, vector_store=vector_store)

        required_exts = [".md"]

        print("Loading documents from directory...")

        documents = SimpleDirectoryReader(
            input_dir='/Users/mkucher/Documents/chat-bot/datacut/' + dataPathFolder, required_exts=required_exts, recursive=True
        ).load_data()

        doc_summary_index = GPTVectorStoreIndex.from_documents(
            documents,
            service_context=service_context,
            storage_context=storage_context,
            show_progress=True,
        )

        doc_summary_index.set_index_id(collectionName)
