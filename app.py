import streamlit as st
st.markdown(
    """
    <style>
    .stTextInput>div>div>input {
        font-size: 16px;
        padding: 10px;
        border-radius: 8px;
    }
    .stButton>button {
        background-color: #5b88f8;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)





import streamlit as st
from ai_chatbot import ask_chatbot

st.set_page_config(page_title="Fida's AI Chatbot 💬", layout="centered")
st.title("🧠 Fida's AI Chatbot")

# ✅ Session state setup
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "user_message" not in st.session_state:
    st.session_state.user_message = ""

# ✅ Handle clear chat first!
if st.button("🧹 Clear Chat"):
    st.session_state.chat_history = []
    st.session_state.user_message = ""
    st.rerun()  # 👈 Optional but ensures instant clearing

# ✅ Process input only after clear is handled
def process_input():
    user_input = st.session_state.user_message
    if user_input.strip():
        with st.spinner("Thinking..."):
            response = ask_chatbot(user_input)
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Bot", response))
    st.session_state.user_message = ""

# ✅ Input field
st.text_input(
    "You:",
    key="user_message",
    on_change=process_input,
    placeholder="Type your message and press Enter..."
)

# ✅ Show chat history
st.markdown("### 💬 Conversation")
for speaker, message in st.session_state.chat_history:
    icon = "🧍‍♀️" if speaker == "You" else "🤖"
    st.markdown(f"{icon} **{speaker}:** {message}")

