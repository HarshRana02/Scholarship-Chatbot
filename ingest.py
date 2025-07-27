# INGEST SCRIPT FROM JSON TO CHROMADB FOR RAG MODEL

import json
import torch
from tqdm import tqdm
from langchain.schema import Document
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

def load_scholarship_data(path="D:/Projects/POCs/gov_scholarship_rag/data/scraped.json"):
    with open(path, "r", encoding="utf-8") as f:
        records = json.load(f)
    documents = [
    Document(
        page_content=(
            f"Scholarship Name: {item.get('Name', '')}\n"
            f"Education Qualification: {item.get('Education Qualification', '')}\n"
            f"Gender: {item.get('Gender', '')}\n"
            f"Community: {item.get('Community', '')}\n"
            f"Religion: {item.get('Religion', '')}\n"
            f"Disability: {item.get('Disability', '')}\n"
            f"Sports: {item.get('Sports', '')}\n"
            f"Annual Percentage: {item.get('Annual-Percentage', '')}\n"
            f"Income: {item.get('Income', '')}\n"
            f"Location: {item.get('India', '')}"
        ),
        metadata={"source": "India Scholarship Data"}
    )
    for item in records
]

    return documents

def embed_documents():
    documents = load_scholarship_data()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(documents)

    device = "cuda" if torch.cuda.is_available() else "cpu"
    if device == "cuda":
        gpu_name = torch.cuda.get_device_name(torch.cuda.current_device())
        print(f"CUDA is available. Using GPU: {gpu_name}")
    else:
        print("CUDA not available. Using CPU.")

    embedding = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": device}
    )

    print("Embedding documents...")
    vectordb = Chroma.from_documents(
        documents=tqdm(chunks, desc="Embedding chunks"),
        embedding=embedding,
        persist_directory="D:/Projects/POCs/gov_scholarship_rag/data/chroma_db"
    )
    vectordb.persist()
    print("Embedded documents into ChromaDB.")

if __name__ == "__main__":
    embed_documents()


