
from store.vectorStore.fabrics.pinecone_vector_store_fabric import PineconeVectorStoreFabric


class VectorStoreManager:
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(VectorStoreManager, cls).__new__(cls)
        return cls._instance

    def __init__(self, **kwargs):
        self.kwargs = kwargs
    
    @staticmethod
    def get_or_create (index_name, vector_store_type = 'PineconeVectorStore', namespace=None):
        if vector_store_type == 'PineconeVectorStore':
            return PineconeVectorStoreFabric.get_vector_store(index_name, namespace)
        else:
            raise Exception('Unsupported vector store type')
            