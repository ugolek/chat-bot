from llama_index.indices.postprocessor import MetadataReplacementPostProcessor
from llama_index import VectorStoreIndex
from llama_index.node_parser import SentenceWindowNodeParser
from llama_index.embeddings import OpenAIEmbedding
from llama_index.llms import OpenAI
from llama_index import ServiceContext
from langchain.embeddings import HuggingFaceEmbeddings
from llama_index.vector_stores import PineconeVectorStore
from streamlit_chat import message
import os
import openai
import streamlit as st
import pinecone


os.environ["OPENAI_API_KEY"] = "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"
openai.api_key = os.environ["OPENAI_API_KEY"]


# Initialize Pinecone
print("Initializing Pinecone...")
pinecone.init(api_key="cb0cdcdf-2076-415d-a700-fd16c759e973",
              environment="us-west4-gcp-free")
index_name = "chatbot-index"

# Check if the index exists.
if index_name not in pinecone.list_indexes():
    print(f"Index {index_name} not found, exiting...")
    exit(code=1)


# Get a Pinecone index instance
print("Getting Pinecone index instance...")
pinecone_index = pinecone.Index(index_name=index_name)
print("Pinecone index instance obtained.")

vector_store = PineconeVectorStore(pinecone_index=pinecone_index)

node_parser = SentenceWindowNodeParser.from_defaults(
    window_size=3,
    window_metadata_key="window",
    original_text_metadata_key="original_text",
)

llm = OpenAI(model="gpt-3.5-turbo", temperature=0.1)

ctx = ServiceContext.from_defaults(
    llm=llm,
    embed_model=HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-mpnet-base-v2"
    ),
    node_parser=node_parser,
)

index = VectorStoreIndex.from_vector_store(vector_store, service_context=ctx)
# Index the documents
# for doc in documents:
#     print(doc.doc_id)
#     index.upsert(items={doc.doc_id: doc.embedding})

query_engine = index.as_query_engine(
    similarity_top_k=2,
    # the target key defaults to `window` to match the node_parser's default
    node_postprocessors=[
        MetadataReplacementPostProcessor(target_metadata_key="window")
    ],
)
# Test block for check window and sentence
# window_response = query_engine.query("what is Papers Clubs how add new one")

# window = window_response.source_nodes[0].node.metadata["window"]
# sentence = window_response.source_nodes[0].node.metadata["original_text"]

# print(f"Window: {window}")
# print("------------------")
# print(f"Original Sentence: {sentence}")
# st.set_page_config(
#     page_title="Gathers Chat",
#     page_icon=":robot:"
# )

st.header("Gathers Chat")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []


def query(payload):
    response = query_engine.query(payload)
    print(response);
    return response.response


def get_text():
    input_text = st.text_input("You: ", "", key="input")
    return input_text


user_input = get_text()
# user_input = 'what is Papers Clubs'

if user_input:
    output = query(user_input)

    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        print('||||||||generated|||||||', st.session_state['generated'])
        print('||||||||past|||||||', st.session_state['past'])
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i],
                is_user=True, key=str(i) + '_user')
