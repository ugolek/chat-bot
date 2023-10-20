from llama_index import ListIndex, VectorStoreIndex, StorageContext
from llama_index.indices.vector_store.retrievers import VectorIndexAutoRetriever
from llama_index.retrievers import RecursiveRetriever
from llama_index.vector_stores.types import MetadataInfo, VectorStoreInfo
from llama_index.tools import QueryEngineTool, ToolMetadata
from llama_index.indices.base import BaseIndex
from llama_index.agent import OpenAIAgent
from llama_index.llms import OpenAI


class RetrieverService:
    def get_retriever(self, index: str) -> VectorIndexAutoRetriever:
        vector_store_info = VectorStoreInfo(
            content_info="bucnh of content which hold useful information about client",
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
                MetadataInfo(
                    name="keywords",
                    type="str",
                    description="keywords of the current node",
                ),
            ],
        )

        retriever = VectorIndexAutoRetriever(
            index,
            vector_store_info=vector_store_info,
            max_top_k=100,
        )

        return retriever,

    def get_recursive_retriever(self, indices: list[BaseIndex], storage_context: StorageContext) -> RecursiveRetriever:
        grouped_indices = {}
        agents = {}

        for index in indices:
            key, value = index.index_id.split(':')

            if value not in grouped_indices:
                grouped_indices[value] = {}
            grouped_indices[value][key] = index

        result = []
        for unique_id, indices in grouped_indices.items():
            doc_structure = {
                'doc_index': unique_id,
                'vector_index': indices['vector_index'],
                'summary_index': indices['summary_index']
            }
            result.append(doc_structure)

        for doc_structure in result:
            vector_query_engine = doc_structure['vector_index'].as_query_engine()
            list_query_engine = doc_structure['summary_index'].as_query_engine()

            query_engine_tools = [
                QueryEngineTool(
                    query_engine=vector_query_engine,
                    metadata=ToolMetadata(
                        name="vector_tool",
                        description=f"Useful for retrieving specific context related to {doc_structure['doc_index']}",
                    ),
                ),
                QueryEngineTool(
                    query_engine=list_query_engine,
                    metadata=ToolMetadata(
                        name="summary_tool",
                        description=f"Useful for summarization questions related to {doc_structure['doc_index']}",
                    ),
                ),
            ]

            function_llm = OpenAI(model="gpt-3.5-turbo-0613")

            agent = OpenAIAgent.from_tools(
                query_engine_tools,
                llm=function_llm,
                verbose=True,
            )

            agents[doc_structure['doc_index']] = agent

            root_vector_store = storage_context.vector_store
            vector_retriever = VectorStoreIndex.from_vector_store(
                root_vector_store).as_retriever()

            recursive_retriever = RecursiveRetriever(
                "vector",
                retriever_dict={"vector": vector_retriever},
                query_engine_dict=agents,
                verbose=True,
            )

            return recursive_retriever
