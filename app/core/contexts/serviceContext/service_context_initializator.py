from llama_index import ServiceContext, LLMPredictor, LangchainEmbedding, set_global_service_context
from langchain.embeddings import HuggingFaceEmbeddings
from llama_index.node_parser import SentenceWindowNodeParser
from langchain.chat_models import ChatOpenAI


node_parser = SentenceWindowNodeParser.from_defaults(
    window_size=3,
    window_metadata_key="window",
    original_text_metadata_key="original_text",
)

llm_predictor_chat = LLMPredictor(llm=ChatOpenAI(
    temperature=0.2, model_name="gpt-3.5-turbo"))

embed_model = LangchainEmbedding(HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2"))

service_context = ServiceContext.from_defaults(
    llm_predictor=llm_predictor_chat, embed_model=embed_model, node_parser=node_parser)

set_global_service_context(service_context)
