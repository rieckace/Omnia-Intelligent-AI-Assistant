# src/memory_handler.py
from langchain.memory import VectorStoreRetrieverMemory
from langchain_community.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
import os

def create_longterm_memory(persist_directory="models/vector_store"):
    """
    Creates a long-term memory using Chroma Vector DB.
    Stores and retrieves conversation history across turns.
    """

    # Ensure persistence directory exists
    os.makedirs(persist_directory, exist_ok=True)

    # Explicitly define the device to use.
    model_kwargs = {'device': 'cpu'}

    # Create text embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs=model_kwargs
    )

    # Initialize Chroma vector store
    vectorstore = Chroma(
        collection_name="chat_memory",
        embedding_function=embeddings,
        persist_directory=persist_directory
    )

    # Create retriever memory
    memory = VectorStoreRetrieverMemory(
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        # return_messages=True  # <--- THIS IS THE FIX
    )
    return memory