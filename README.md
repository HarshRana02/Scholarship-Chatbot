# 🎓 Scholarship Chatbot 

An AI-powered chatbot that helps students discover Indian government scholarships. It uses **Retrieval-Augmented Generation (RAG)**, processes structured data from Excel/CSV files, and delivers conversational answers via OpenAI's LLM — accelerated with **CUDA-enabled GPU support** for blazing-fast embeddings and retrieval.

## 📌 How It Works
1. 📊 Load data from Excel/CSV  
2. 🔁 Convert to structured JSON  
3. 🧬 Embed using OpenAI Embeddings (GPU-accelerated)  
4. 🧠 Store vectors in ChromaDB  
5. 💬 Query via LangChain's RAG pipeline  
6. ⚡ CUDA boosts performance for embedding & retrieval

## 🗂️ File Structure

```
Scholarship-Chatbot/
├── data/             # Contains Excel/CSV files with scholarship data
├── app.py            # Streamlit UI to query the chatbot
├── data_to_json.py   # Converts CSV/Excel data to structured JSON
├── ingest.py         # Embeds data and stores in ChromaDB
├── rag_chain.py      # RAG logic: retrieval + LLM response generation
└── view_db.py        # Utility to view ChromaDB documents
```

## 🚀 Getting Started

### 1. Clone the Repository
<pre>
git clone https://github.com/HarshRana02/Scholarship-Chatbot.git
cd Scholarship-Chatbot
</pre>

### 2. Install Dependencies
<pre>
pip install -r requirements.txt
</pre>

### 3. Add Data
Place your Excel or CSV file in the **data/** folder.

### 4. Preprocess & Embed
<pre>
python data_to_json.py         # Convert structured file to JSON format
python ingest.py               # Embed JSON data into ChromaDB
</pre>

### 5. Run the Chatbot
<pre>
streamlit run app.py
</pre>
