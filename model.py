import torch
import chromadb
from llama_index.llms import LlamaCPP
from llama_index.llms.llama_utils import messages_to_prompt, completion_to_prompt
from llama_index.embeddings import HuggingFaceEmbedding
from llama_index import VectorStoreIndex
from llama_index import ServiceContext
from llama_index.vector_stores import ChromaVectorStore



# Using minstral 7b instruct model, found it worked better than phi-2 in testing
llm = LlamaCPP(
    model_path="./mistral-7b-instruct-v0.2.Q5_K_S.gguf",
    temperature=0.4,
    max_new_tokens=512,
    context_window=2048,
    generate_kwargs={},
    model_kwargs={"n_gpu_layers": -1},
    messages_to_prompt=messages_to_prompt,
    completion_to_prompt=completion_to_prompt,
    verbose=True,
)


#Using a custom embedding model, this one performs pretty well on MTEB leaderboard
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-large-en-v1.5")
service_context = ServiceContext.from_defaults(
    chunk_size=1024,
    llm=llm,
    embed_model=embed_model,
    chunk_overlap=128,
)


#fetching the from the chroma database

db2 = chromadb.PersistentClient(path="./chroma_db")
chroma_collection = db2.get_or_create_collection("laws_of_power")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
index = VectorStoreIndex.from_vector_store(
vector_store,
service_context=service_context,
)


def generate_text(query):
    query_engine = index.as_query_engine()
    response = query_engine.query(f"{query}")
    return response