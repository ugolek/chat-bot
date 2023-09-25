import chromadb

class CollectionManager:
    def __init__(self):
        self.client = self.get_client()

    def get_client(self):
        # client = chromadb.HttpClient(host='localhost', port=8000)
        # return chromadb.EphemeralClient()
        return chromadb.PersistentClient()
    
    def create_collection(self, name):
        return self.client.create_collection(name)

    def get_or_create_collection(self, name, metadata=None, embedding_function=None):
        return self.client.get_or_create_collection(name, metadata=metadata, embedding_function=embedding_function)

    def get_collection(self, name):
        return self.client.get_collection(name)

    def delete_collection(self, name):
        self.client.delete_collection(name)

    def update_collection(self, name, docs):
        collection = self.get_collection(name)
        if collection:
            for doc in docs:
                collection.add(ids=[str(uuid.uuid1())], metadatas=doc.metadata, documents=doc.page_content)

    def get_collections(self):
        return self.client.list_collections()
