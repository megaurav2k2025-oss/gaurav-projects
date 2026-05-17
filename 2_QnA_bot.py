from dotenv import load_dotenv
load_dotenv()

##from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
import streamlit as st
##llm = ChatGoogleGenerativeAI(model = "gemini-3.1-flash-tts-preview")
llm = ChatOpenAI(model = "gpt-4")

st.title("Ask QnA Bot")
st.markdown("QnA based on python, langchain, OpenAI and streamlit !")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)

query = st.chat_input("Ask Me Anything ?")
if query:
    st.session_state.messages.append({"role":"user","content":query})
    st.chat_message("user").markdown(query)
    res = llm.invoke(query)
    st.chat_message("ai").markdown(res.content)
    st.session_state.messages.append({"role":"ai","content":res.content})