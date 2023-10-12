from llama_index.indices.vector_store.retrievers import VectorIndexAutoRetriever
from llama_index.vector_stores.types import MetadataInfo, VectorStoreInfo


class RetrieverService:
    def get_retriever(self, index: str) -> VectorIndexAutoRetriever:
        vector_store_info = VectorStoreInfo(
            content_info="bucnh of content which hold useful information about client ",
            metadata_info=[
                MetadataInfo(
                    name="client_name",
                    type="str",
                    description="Name of client which owns the data",
                ),
                MetadataInfo(
                    name="namespace",
                    type="str",
                    description="namespace of the client which owns the data, namespace is a way to group data of a client",
                ),
                MetadataInfo(
                    name="file_path_from_namespace",
                    type="str",
                    description="path of the file from the namespace of the client, it help to locate the file in the namespace and describe hierarchy structure of the namespace files",
                ),
                MetadataInfo(
                    name="file_name",
                    type="str",
                    description="name of the file",
                ),
            ],
        )

        retriever = VectorIndexAutoRetriever(
            index,
            vector_store_info=vector_store_info,
            max_top_k=100,
        )

        return retriever
