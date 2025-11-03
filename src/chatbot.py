# src/chatbot.py
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.chains import ConversationChain
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,

)

# Import your memory handler
from src.memory_handler import create_longterm_memory

load_dotenv() # Load .env variables

def initialize_chatbot():
    """
    Initializes a Groq-powered chatbot with LONG-TERM vector memory.
    """
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("⚠️ GROQ_API_KEY not found in .env file.")

    llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0.7, api_key=api_key)

    # Create the long-term memory object
    memory = create_longterm_memory()

    prompt = ChatPromptTemplate(
        messages=[
            SystemMessagePromptTemplate.from_template(
                "You are Omnia, an intelligent AI assistant. "
                "You are friendly, helpful, and conversational. "
                "Use the following pieces of relevant conversation history to help answer the user's question: "
                "\n--- RELEVANT HISTORY ---\n"
                "{history}"  # <-- 'history' is now correctly treated as a string
                "\n--- END OF HISTORY ---\n\n"
                "If you don't know the answer, just say you don't know."
            ),
            # No MessagesPlaceholder is needed
            HumanMessagePromptTemplate.from_template("{input}"),
        ]
    )

    # Create the ConversationChain
    chain = ConversationChain(
        llm=llm,
        prompt=prompt,
        memory=memory, # Your long-term memory is plugged in
        verbose=True
    )

    return chain