# ui/main.py
import sys
import os
import streamlit as st

# --------------------------------
# Path Setup
# --------------------------------
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if root_path not in sys.path:
    sys.path.append(root_path)

try:
    from src.chatbot import initialize_chatbot
except ImportError:
    st.error("Error: Could not import 'initialize_chatbot'. Please check 'src/chatbot.py'.")
    st.stop()

# --------------------------------
# Page Setup
# --------------------------------
st.set_page_config(
    page_title="Omnia – The Intelligent AI Assistant",
    page_icon="🧠",
    layout="centered"
)

# --------------------------------
# Custom CSS – Clean, Centered, and Professional
# --------------------------------
st.markdown(
    """
<style>
body {
    background-color: #0b0c10;
    font-family: 'Inter', sans-serif;
    color: #f1f1f1;
}

/* Main Container */
.main > div {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
    padding-bottom: 8rem;
}

/* Title Section */
.title-container {
    text-align: center;
    margin-top: 15px;
    margin-bottom: 35px;
}
.title-container h1 {
    font-size: 3.2rem;
    font-weight: 800;
    background: linear-gradient(90deg, #a78bfa, #7c3aed);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: -0.5px;
    text-shadow: 0 0 25px rgba(124, 58, 237, 0.3);
}
.title-container p {
    color: #b5b9c9;
    font-size: 1.15rem;
    margin-top: -5px;
}

/* Chat Container 
.chat-box {
    background: rgba(18, 19, 23, 0.95);
    border: 1px solid #1f2127;
    border-radius: 20px;
    padding: 1.5rem;
    height: calc(100vh - 220px);
    max-height: calc(100vh - 220px);
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    gap: 1.2rem;
    margin-bottom: 0;
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.6);
}
*/

/* Placeholder */
.empty-placeholder {
    background: rgba(18, 19, 23, 0.9);
    border: 1px solid #1f2127;
    border-radius: 16px;
    padding: 3rem 2rem; /* Use padding to give it size */
    /* REMOVED: height: 65vh; 
      REMOVED: max-height: 65vh;
      REMOVED: min-height: 120px;
    */
    display: flex;
    flex-direction: column; 
    align-items: center;
    justify-content: center;
    color: #9da3af;
    font-size: 1.1rem; /* Made font slightly larger */
    margin-bottom: 1.5rem; /* Added space below it */
}

/* Scrollbar */
.chat-box::-webkit-scrollbar {
    width: 8px;
}
.chat-box::-webkit-scrollbar-thumb {
    background: #3a3f47;
    border-radius: 6px;
}

/* Message Bubbles */
.message {
    max-width: 75%;
    padding: 1rem 1.4rem;
    border-radius: 18px;
    line-height: 1.7;
    font-size: 1.05rem;
    word-wrap: break-word;
    white-space: pre-wrap;
    animation: fadeIn 0.3s ease;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
}
.user {
    background: linear-gradient(135deg, #7b61ff 0%, #6a5acd 100%);
    align-self: flex-end;
    color: #fff;
    border-bottom-right-radius: 4px;
}
.bot {
    background: linear-gradient(135deg, #2d2f36 0%, #3b3e47 100%);
    align-self: flex-start;
    border-bottom-left-radius: 4px;
    color: #eaeaea;
}

/* Input Section */
#fixed-input-wrapper {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    z-index: 1000;
    background-color: #0b0c10;
    padding: 15px 0;
    border-top: 1px solid #1f2127;
    box-shadow: 0 -10px 20px rgba(0, 0, 0, 0.4);
}

.input-area-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1rem;
    background-color: #1a1c22;
    border: 1px solid #2b2f36;
    border-radius: 18px;
    padding: 0.5rem 1rem;
    display: flex;
    align-items: center;
}

[data-testid="stTextInput"] > div > div > input {
    background-color: transparent;
    color: #f1f1f1;
    border: none;
    width: 100%;
    font-size: 1.1rem;
    padding: 0.5rem 0;
}
[data-testid="stTextInput"] > div > div > input:focus {
    outline: none;
    box-shadow: none;
}

/* Buttons */
.stButton button {
    background: linear-gradient(135deg, #7b61ff 0%, #9a70ff 100%);
    color: white;
    border-radius: 14px;
    border: none;
    font-weight: 700;
    padding: 0.5rem 1.5rem;
    margin-left: 10px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
    transition: all 0.2s;
}
.stButton button:hover {
    background: linear-gradient(135deg, #6a5acd 0%, #9278ff 100%);
    transform: translateY(-1px);
}

/* Clear Chat Button */
#clear-button {
    text-align: center;
    margin-top: 1rem;
    margin-bottom: 2rem;
}
#clear-button button {
    background: #333333 !important;
    font-weight: 500;
    padding: 0.4rem 1.2rem;
}
#clear-button button:hover {
    background: #4a4a4a !important;
}

/* Animations */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(5px); }
    to { opacity: 1; transform: translateY(0); }
}
</style>
""",
    unsafe_allow_html=True,
)

# --------------------------------
# Header Section
# --------------------------------
st.markdown(
    """
<div class="title-container">
    <h1>🧠 Omnia</h1>
    <p>Your Intelligent AI Assistant powered by <strong>LangChain</strong> & <strong>Groq LLMs</strong> ⚡</p>
</div>
""",
    unsafe_allow_html=True,
)

# --------------------------------
# Initialize Chatbot
# --------------------------------
if "chatbot" not in st.session_state:
    st.session_state.chatbot = initialize_chatbot()
if "history" not in st.session_state:
    st.session_state.history = []

# --------------------------------
# Chat Display
# --------------------------------
st.container()

if st.session_state.get("history") and len(st.session_state.history) > 0:
    st.markdown('<div class="chat-box" id="chat-box">', unsafe_allow_html=True)
    for role, text in st.session_state.history:
        css_class = "user" if role == "user" else "bot"
        st.markdown(f'<div class="message {css_class}">{text}</div>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
else:
    st.markdown(
        '<div class="empty-placeholder">👋 Hi, I’m &nbsp;<strong>Omnia</strong> — Ask me anything to begin our conversation!</div>',
        unsafe_allow_html=True,
    )

# --------------------------------
# Clear Chat Button
# --------------------------------
st.markdown('<div id="clear-button">', unsafe_allow_html=True)
if st.button("🧹 Clear Conversation", key="clear_chat_button"):
    st.session_state.chatbot = initialize_chatbot()
    st.session_state.history = []
    st.rerun()
st.markdown("</div>", unsafe_allow_html=True)

# --------------------------------
# Input Section (Fixed)
# --------------------------------
st.markdown('<div id="fixed-input-wrapper">', unsafe_allow_html=True)

# --- No manual session state flags needed ---

# --- Create form ---
# 'clear_on_submit=True' is the key. It automatically clears all widgets
# inside the form *after* this block is processed on a successful submit.
with st.form(key="chat_form", clear_on_submit=True):
    st.markdown('<div class="input-area-container">', unsafe_allow_html=True)

    col1, col2 = st.columns([8, 1])
    with col1:
        # The widget's value is returned to this local variable
        user_input = st.text_area(
            "💬 Message:",
            placeholder="   Ask Omnia...",
            key="user_input_widget",  # A key is still good practice
            label_visibility="collapsed",
            height=50,
        )
    with col2:
        # 'submitted' is now a simple boolean, True if clicked this run
        # We REMOVE the on_click callback entirely
        submitted = st.form_submit_button("Send", key="send_button")

    st.markdown("</div>", unsafe_allow_html=True)

# --- Handle submission *immediately after* the form ---
# This is the standard, correct pattern.
# 'submitted' will be True on the rerun *after* the user clicks.
# 'user_input' (the local variable) will contain the text from that submission.
if submitted and user_input.strip():
    with st.spinner("Omnia is thinking..."):
        # Use the local variable 'user_input'
        response = st.session_state.chatbot.run(user_input)

    # Use the local variable 'user_input'
    st.session_state.history.append(("user", user_input))
    st.session_state.history.append(("bot", response))

    # --- NO MANUAL CLEARING NEEDED ---
    # The 'clear_on_submit=True' in st.form() handles this for you.
    # The 'st.session_state.user_input = ""' line is removed.
    # The 'st.session_state.submitted = False' line is removed.

    # Rerun to show the new message and the now-cleared input box
    st.rerun() # Replaced experimental_rerun with st.rerun

st.markdown("</div>", unsafe_allow_html=True)

# --------------------------------
# Auto Scroll
# --------------------------------
st.markdown(
    """
    <script>
        setTimeout(function(){
            var chatBox = document.getElementById("chat-box");
            if (chatBox) chatBox.scrollTop = chatBox.scrollHeight;
        }, 120);
    </script>
    """,
    unsafe_allow_html=True,
)
