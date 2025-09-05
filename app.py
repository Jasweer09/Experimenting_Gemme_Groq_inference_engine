import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.chains.retrieval import create_retrieval_chain
import asyncio

from dotenv import load_dotenv
load_dotenv()

#fetching the api keys from the env file
groq_api_key = os.getenv("GROQ_API_KEY")
google_api_key = os.getenv("GOOGLE_API_KEY")

st.title("Gemma Model Q&A ChatBot")

#Defining the Gemma Model using Groq inference
llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name = "gemma2-9b-it"
)

#Setup Prompt template
prompt = ChatPromptTemplate.from_template(
"""
Answer the questions based on the provided context only.
Please provide the most accurate response based on the question

<context>
{context}
<context>
Question: {input}
"""
)

try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

## defining the Vector embedding function
def vector_embedding():
    if "vectors" not in st.session_state:
        st.session_state.embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
        st.session_state.loader = PyPDFDirectoryLoader("./us_census")
        st.session_state.document = st.session_state.loader.load()
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size =1000, chunk_overlap =200)
        st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.document)
        st.session_state.vectorstore=FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings)
    
prompt1 = st.text_input("Enter Query from Documents?")

if st.button("Creating Vector Store"):
    vector_embedding()
    st.write("Vector Store DB is ready for User Queries")

import time

if prompt1:
    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = st.session_state.vectorstore.as_retriever()
    retrival_chain = create_retrieval_chain(retriever, document_chain)

    start =time.process_time()
    response = retrival_chain.invoke({'input': prompt1})
    st.write(response['answer'])

    st.expander("Context for above Response")
    for i, doc in enumerate(response["context"]):
        st.write(doc.page_content)
        st.write("-------------------------------------------")