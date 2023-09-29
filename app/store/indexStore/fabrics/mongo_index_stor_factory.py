import os
from llama_index.storage.index_store import MongoIndexStore
import pinecone


class MongoIndexStoreFabric:
    _instance = None

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.mongo_uri = os.environ["MONGO_URI"]
            self.mongo_db_name = os.environ["MONGO_DB"]
            self.initialized = True

    def get_index_store(self):
        return MongoIndexStore.from_uri(
            uri=self.mongo_uri,
            db_name=self.mongo_db_name)


MongoIndexStoreFabric.get_index_store = staticmethod(
    MongoIndexStoreFabric.get_index_store)
