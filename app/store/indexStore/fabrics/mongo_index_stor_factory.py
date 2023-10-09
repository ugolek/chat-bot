import os
from llama_index.storage.index_store import MongoIndexStore
import pinecone


class MongoIndexStoreFabric:
    _instance = None

    def get_index_store():
        mongo_uri = os.environ["MONGO_URI"]
        mongo_db_name = os.environ["MONGO_DB"]

        return MongoIndexStore.from_uri(
            uri=mongo_uri,
            db_name=mongo_db_name)


MongoIndexStoreFabric.get_index_store = staticmethod(
    MongoIndexStoreFabric.get_index_store)
