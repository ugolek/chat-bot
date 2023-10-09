from store.indexStore.fabrics.mongo_index_stor_factory import MongoIndexStoreFabric


class IndexStoreManager:
    _instance = None
    _vector_stores_dictionary = {}

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(IndexStoreManager, cls).__new__(cls)
        return cls._instance

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def get_or_create(index_store_type='MongoIndexStore'):
        if index_store_type == 'MongoIndexStore':
            return MongoIndexStoreFabric.get_index_store()
        else:
            raise Exception('Unsupported index store type')
    
  
        
IndexStoreManager.get_or_create = staticmethod(
    IndexStoreManager.get_or_create)