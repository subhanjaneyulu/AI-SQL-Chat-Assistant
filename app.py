import streamlit as st

from langchain_groq import ChatGroq

from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.tools import ArxivQueryRun
from langchain_community.tools import WikipediaQueryRun

from langchain_community.utilities import (
    ArxivAPIWrapper,
    WikipediaAPIWrapper
)

from langgraph.prebuilt import create_react_agent

from langchain.callbacks import StreamlitCallbackHandler

st.set_page_config(page_title="Search Agent")

st.title("🔎 AI Search Assistant")

# -----------------------
# Sidebar
# -----------------------

st.sidebar.title("Settings")

api_key = st.sidebar.text_input(
    "Enter your Groq API Key",
    type="password"
)

# -----------------------
# Tools
# -----------------------

search = DuckDuckGoSearchRun()

arxiv = ArxivQueryRun(
    api_wrapper=ArxivAPIWrapper(
        top_k_results=2,
        doc_content_chars_max=300
    )
)

wiki = WikipediaQueryRun(
    api_wrapper=WikipediaAPIWrapper(
        top_k_results=2,
        doc_content_chars_max=300
    )
)

tools = [
    search,
    wiki,
    arxiv
]

# -----------------------
# Chat History
# -----------------------

if "messages" not in st.session_state:

    st.session_state.messages = []

for message in st.session_state.messages:

    st.chat_message(message["role"]).write(
        message["content"]
    )

# -----------------------
# User Prompt
# -----------------------

prompt = st.chat_input(
    "Ask anything..."
)

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    st.chat_message("user").write(prompt)

    llm = ChatGroq(
        api_key=api_key,
        model="llama-3.3-70b-versatile",
        temperature=0
    )

    agent = create_react_agent(
        llm,
        tools
    )

    with st.chat_message("assistant"):

        st_callback = StreamlitCallbackHandler(
            st.container()
        )

        response = agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            },
            config={
                "callbacks": [st_callback]
            }
        )

        answer = response["messages"][-1].content

        st.write(answer)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )