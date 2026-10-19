
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_groq import ChatGroq

# Initialize Groq LLM
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.7
)

# Streamlit UI - python library
# web interface provide

st.title("🤖 ASKBUDDY - AI QNA Bot")
st.markdown("My QnA Bot with LangChain and Groq!")



# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
# we want a chat window 
# Get user input
query = st.chat_input("Ask anything?")

if query:
    # Display and store user message
    st.session_state.messages.append({
        "role": "user",
        "content": query
    })

    with st.chat_message("user"):
        st.markdown(query)

    # Get Groq response
    try:
        with st.chat_message("assistant"):
            with st.spinner("ASKBUDDY is thinking..."):
                res = llm.invoke(query)
                answer = res.content

            st.markdown(answer)

        # Store assistant response
        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })

    except Exception as e:
        st.error(f"Something went wrong: {e}")