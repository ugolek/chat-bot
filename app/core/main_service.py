from core.indexManager.index_manager import IndexManager
from langchain.chat_models import ChatOpenAI
from llama_index import LLMPredictor, LangchainEmbedding, ServiceContext, StorageContext, load_index_from_storage
from llama_index.vector_stores import PineconeVectorStore, ChromaVectorStore
from llama_index.storage.index_store import SimpleIndexStore
from llama_index.llms import OpenAI
from llama_index.storage.index_store import MongoIndexStore
from llama_index.node_parser import SentenceWindowNodeParser
from langchain.embeddings import HuggingFaceEmbeddings, SentenceTransformerEmbeddings
import pinecone
import os

class MainService:
    def __init__(self):
        self.index_manager = IndexManager()

    def queryFromCloud(self, question: str, l_index_name: str):
        l_index = self.index_manager.getIndex(l_index_name)
        ## and perform the query
        query = l_index.as_query_engine()

        return query.query(question)
    
    def upload_local_data(self, dataPathFolder, l_index_name):
        return self.index_manager.upload_data_to_index(dataPathFolder, l_index_name)
    
    def upload_data(self, data, l_index_name):
        return self.index_manager.upload_data_to_index(data, l_index_name)
