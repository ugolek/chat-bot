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

    def get_or_create(self, index_store_type='MongoIndexStore'):
        return self._create(index_store_type)
    
    def _create (self, index_name, index_store_type):
        if index_store_type == 'MongoIndexStore':
            return MongoIndexStoreFabric.get_index_store(index_name)
        else:
            raise Exception('Unsupported index store type')