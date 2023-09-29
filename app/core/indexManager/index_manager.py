from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, StorageContext
from store.indexStore.index_store_manager import IndexStoreManager

from store.vectorStore.vector_store_manager import VectorStoreManager


class IndexManager:
    __instance = None
    __index_dictionary = {}

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance') or cls._instance is None:
            cls._instance = super(IndexManager, cls).__new__(cls)
        return cls._instance


    def getIndex(self, index):
        if (index not in IndexManager.__index_dictionary):
            IndexManager.__index_dictionary[index] = self.createIndex(index)

        return IndexManager.__index_dictionary[index]

    def createIndex(l_index_name):
        vector_store = VectorStoreManager.get_or_create(l_index_name)
        doc_summary_index = GPTVectorStoreIndex.from_vector_store(
            vector_store==vector_store,
            show_progress=True,
        )

        return doc_summary_index

    def upload_local_data_to_index(self, dataPathFolder, l_index_name):
        vector_store = VectorStoreManager.create(l_index_name)
        index_store = IndexStoreManager.get_or_create()
        storage_context = StorageContext.from_defaults(
            index_store=index_store, vector_store=vector_store)

        required_exts = [".md"]
        documents = SimpleDirectoryReader(
            input_dir='/Users/mkucher/Documents/chat-bot/datacut/' + dataPathFolder, required_exts=required_exts, recursive=True
        ).load_data()

        doc_summary_index = GPTVectorStoreIndex.from_documents(
            documents,
            storage_context=storage_context,
            show_progress=True,
        )

        doc_summary_index.set_index_id(l_index_name)

    def upload_data_to_index(self, data, l_index_name):
        vector_store = VectorStoreManager.create(l_index_name)
        index_store = IndexStoreManager.get_or_create()
        storage_context = StorageContext.from_defaults(
            index_store=index_store, vector_store=vector_store)

        required_exts = [".md"]
        documents = SimpleDirectoryReader(
            input_dir='/Users/mkucher/Documents/chat-bot/datacut/' + dataPathFolder, required_exts=required_exts, recursive=True
        ).load_data()

        doc_summary_index = GPTVectorStoreIndex.from_documents(
            documents,
            storage_context=storage_context,
            show_progress=True,
        )

        doc_summary_index.set_index_id(l_index_name)
