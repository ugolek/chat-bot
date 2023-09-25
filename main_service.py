from collection_manager import CollectionManager
from storage.local_storage import LocalStorage
from langchain.chat_models import ChatOpenAI
from llama_index import LLMPredictor, LangchainEmbedding, ServiceContext, StorageContext, load_index_from_storage
from llama_index.vector_stores import ChromaVectorStore
from llama_index.storage.index_store import SimpleIndexStore
from langchain.embeddings import HuggingFaceEmbeddings, SentenceTransformerEmbeddings

class MainService:
    def __init__(self):
        self.collection_manager = CollectionManager()
        self.storage = LocalStorage()

    def query(self, question: str, collectionName: str):
        client = self.collection_manager.get_client()
        collection = client.get_collection(collectionName)

        load_storage_context = StorageContext.from_defaults(
            vector_store=ChromaVectorStore(chroma_collection=collection),
            index_store=SimpleIndexStore.from_persist_dir(
                persist_dir=('./storage/index_storage/' + collectionName + '/')
            ),
        )

                # init LLM Model
        llm_predictor = LLMPredictor(llm=ChatOpenAI(
            temperature=0.2, max_tokens=512, model_name='gpt-3.5-turbo'))

        # init embedding model
        embed_model = LangchainEmbedding(HuggingFaceEmbeddings())

        # construct service context
        load_service_context = ServiceContext.from_defaults(
            llm_predictor=llm_predictor, embed_model=embed_model)

        # finally to load the index
        load_index = load_index_from_storage(service_context=load_service_context,
                                            storage_context=load_storage_context)

        query = load_index.as_query_engine()
        return query.query(question)