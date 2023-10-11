from http import HTTPStatus
from fastapi import HTTPException
from store.virtualFileSystem.s3_service import S3Service
from core.indexManager.index_manager import IndexManager
from core.contexts.serviceContext.service_context_initialization import init_global_service_context
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
        self.docstore_service = S3Service()
        init_global_service_context()

    # def upload_local_data(self, dataPathFolder, l_index_name):
    #     return self.index_manager.upload_data_to_index(dataPathFolder, l_index_name)

    async def upload_files_to_namespace(self, files, client_name: str, namespace: str, path: str):
        await self.docstore_service.upload_files(files, client_name, namespace, path)

        return await self.index_manager.upload_data_to_index_namespace(client_name, namespace)

    def ask_namespace(self, question: str, client_name: str, namespace: str):
        return self.index_manager.ask_index(question, client_name, namespace)