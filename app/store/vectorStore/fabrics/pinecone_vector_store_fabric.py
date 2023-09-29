import os
from llama_index.vector_stores import PineconeVectorStore
import pinecone


class PineconeVectorStoreFabric:
    def get_vector_store(index_name):
        api_key = os.environ["PINECONE_API"]
        environment = os.environ["PINECONE_ENVIRONMENT"]

        pinecone.init(api_key=api_key, environment=environment)

        if index_name not in pinecone.list_indexes():
            print(f"Index {index_name} not found, creating it...")
            pinecone.create_index(
                index_name, metric="cosine", shards=1, dimension=768)
            print(f"Index {index_name} created.")
        else:
            print(f"Index {index_name} already exists.")

        pinecone_index = pinecone.Index(index_name=index_name)

        return PineconeVectorStore(pinecone_index=pinecone_index)


PineconeVectorStoreFabric.get_vector_store = staticmethod(
    PineconeVectorStoreFabric.get_vector_store)
