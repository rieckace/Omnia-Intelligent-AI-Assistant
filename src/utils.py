# src/utils.py
def format_response(user_input, bot_response):
    """
    Cleanly formats the chatbot response for display.
    """
    return f"🧑 You: {user_input}\n🤖 Bot: {bot_response}"
