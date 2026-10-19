
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

llm = ChatGoogleGenerativeAI(model="gemini-3.8-flash")

st.title("🤖 ASKBUDDY - AI QNA Bot")
st.markdown("My QnA Bot with LangChain and Google Gemini !")

# query = st.chat_input("ask anything ?")
# if query:
#     st.chat_message("user").markdown(query)
#     res = llm.invoke(query)
#     st.chat_message("ai").markdown(res.text)


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)

query = st.chat_input("ask anything ?")
if query:
    st.session_state.messages.append({"role":"user", "content":query})
    st.chat_message("user").markdown(query)
    res = llm.invoke(query)
    st.chat_message("ai").markdown(res.text)
    st.session_state.messages.append({"role": "ai", "content":res.text})


## yeh abhi hum basic ka padh rahe he

# while True:
#     query = input("User: ")
#     if query in ["quit", "exit", "bye"]:
#         print("good bye")
#         break

#     result = llm.invoke(query)
#     print("AI: ", result.text, "\n")

