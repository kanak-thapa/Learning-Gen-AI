from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq

import streamlit as st

st.title("lets have a chit chat")
st.markdown("HII i am a chatBOT")

llm = ChatGroq(model="openai/gpt-oss-20b")

if "messages" not in st.session_state: 
    st.session_state.messages = []

for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)


query = st.chat_input("ask your question...")
if query:
    st.session_state.messages.append({"role": "user", "content": query})
    st.chat_message("user").markdown(query)
    ans = llm.invoke(query)
    st.chat_message("ai").markdown(ans.content)
    st.session_state.messages.append({"role": "ai", "content": ans.content})





















# from langchain_groq import ChatGroq
# import streamlit as st

# llm = ChatGroq(model="openai/gpt-oss-20b")

# st.title("lets have a chitchat")

# history = []
    
# while True:
#     query = input("enter you question: ")
#     if query in ["quit", "exit"]:
#         print("bye..")
#         break

#     history.append({"role": "user", "content": query})
#     ans = llm.invoke(history)# keep this in mind
#     history.append({"role": "ai", "content": ans.content})
#     print(ans.content)