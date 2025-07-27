# VIEW CHROMA DB CONTENTS

import torch
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# Load embedding model
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cuda" if torch.cuda.is_available() else "cpu"}
)

# Load the Chroma DB
db = Chroma(
    persist_directory="D:/Projects/POCs/gov_scholarship_rag/data/chroma_db",
    embedding_function=embedding
)

# Get total number of documents
collection = db._collection  # Low-level Chroma API
doc_count = collection.count()
print(f"Total documents stored in Chroma DB: {doc_count}")

# Show a few documents (top 5)
sample_results = db.similarity_search("scholarship", k=5)
print("Sample documents:")
for i, doc in enumerate(sample_results, 1):
    print(f"\n--- Document {i} ---")
    print(doc.page_content)
    print("Metadata:", doc.metadata)