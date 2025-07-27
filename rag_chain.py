# RETRIEVE AND GENERATE (RAG) CHAIN FOR SCHOLARSHIP CHATBOT

from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import Ollama
from langchain.chains import RetrievalQA
import torch

def get_rag_chain():
    embedding = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": "cuda" if torch.cuda.is_available() else "cpu"}
    )

    vectordb = Chroma(
        persist_directory="D:/Projects/POCs/gov_scholarship_rag/data/chroma_db",
        embedding_function=embedding
    )
    retriever = vectordb.as_retriever(search_kwargs={"k": 3})
    llm = Ollama(model="mistral")

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )
    return qa_chain
