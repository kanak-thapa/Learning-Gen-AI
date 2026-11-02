## LLM
## TOOL - GOOGLE SEARCH TOOL
## AGENT
## MEMORY
## STREAMING
## WEB INTERFACE

from dotenv import load_dotenv
load_dotenv()

from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver

import streamlit as st

model = ChatGroq(model="openai/gpt-oss-20b")
search = GoogleSerperAPIWrapper()

if "memory" not in st.session_state:
    st.session_state.memory = MemorySaver()
    st.session_state.history = []

memory = MemorySaver()

agent = create_agent(
    model=model,
    tools=[search.run],
    system_prompt="You are a agent and can search for any question on google.",
    checkpointer=st.session_state.memory,
)

print(st.session_state.memory)

### Building Web Interface
st.subheader("QuickAnswer - Answer at the speed at thaught")
query = st.chat_input("Ask anything ?")

for message in st.session_state.history:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)

if query: 
    st.chat_message("user").markdown(query)
    st.session_state.history.append({"role": "user", "content": query})
    response = agent.invoke(
        {"messages": [{"role": "user", "content": query}]},
        {"configurable": {"thread_id": "1"}},
        stream_mode="messages"
    )

    ai_container = st.chat_message("ai")
    with ai_container:
        space = st.empty()
        message = ""

        for chunk in response: ## chunk tuple of single message
            message = message + chunk[0].content
            space.write(message)

        st.session_state.history.append({"role":"ai", "content": message})

    # answer = response["messages"][-1].content
    # st.chat_message("ai").markdown(answer)
    # st.session_state.history.append({"role": "ai", "content": answer})



### print(response["messages"][-1].content)


