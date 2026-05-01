# 🤖 Debales AI Assistant (LangGraph + RAG + SERP API)

## 📌 Overview

This project is an AI-powered assistant built for the Debales AI Intern Assignment.
It uses **LangGraph** to orchestrate a workflow that intelligently routes user queries to:

* 📚 **RAG (Retrieval-Augmented Generation)** → for Debales AI-related questions
* 🌐 **SERP API (Google Search)** → for external/general queries

The system ensures **accurate, context-grounded responses** and avoids hallucinations.

---

## 🚀 Features

* ✅ RAG pipeline using FAISS + HuggingFace embeddings
* ✅ SERP API integration for real-time external data
* ✅ LangGraph workflow with routing logic
* ✅ CLI-based chatbot interface
* ✅ No hallucination (answers grounded in context)
* ✅ Fully free setup (Groq + HuggingFace)

---

## 🧠 Architecture

```
User Query
   ↓
Router (LangGraph)
   ↓
 ┌───────────────┬───────────────┐
 │ Debales Query │ External Query│
 │     (RAG)     │   (SERP API)  │
 └───────────────┴───────────────┘
   ↓
Final Response (LLM - Groq)
```

---

## 📁 Project Structure

```
debales-ai-agent/
│
├── app.py                # CLI chatbot
├── graph.py              # LangGraph workflow
├── rag.py                # RAG pipeline
├── scraper.py            # Website scraping
├── tools.py              # SERP API tool
├── router.py             # Query routing logic
│
├── debales.txt           # Scraped data
├── vectorstore/          # FAISS vector DB
│
├── requirements.txt
└── .env.example
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone <your-repo-link>
cd debales-ai-agent
```

---

### 2️⃣ Create virtual environment (recommended)

```bash
python -m venv venv
```

Activate:

**Windows (CMD):**

```bash
venv\Scripts\activate
```

**PowerShell:**

```bash
venv\Scripts\Activate.ps1
```

**Git Bash:**

```bash
source venv/Scripts/activate
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Add API Keys

Create a `.env` file (optional) OR directly add keys in code.

Example `.env`:

```
GROQ_API_KEY=your_groq_api_key
SERP_API_KEY=your_serp_api_key
```

---

### 5️⃣ Scrape data

```bash
python scraper.py
```

---

### 6️⃣ Build vector database

```bash
python rag.py
```

---

### 7️⃣ Run chatbot

```bash
python app.py
```

---

## 💬 Example Usage

```
You: What is Debales AI?
Bot: Debales AI is a platform that...

You: Who is Elon Musk?
Bot: Elon Musk is a business magnate...

You: Debales AI vs OpenAI
Bot: Debales AI focuses on..., while OpenAI...
```

---

## 🔧 Technologies Used

* LangGraph
* LangChain
* FAISS (Vector Database)
* HuggingFace Embeddings
* Groq (LLM)
* SERP API
* BeautifulSoup

---

## ⚠️ Design Decisions

* Used **HuggingFace embeddings** → avoids API cost
* Used **Groq LLM** → free + fast alternative to OpenAI
* Implemented **routing logic** for correct query handling
* Ensured **no hallucination** via context-based answering

---

## 🚧 Challenges & Solutions

* ❌ LangChain import issues → Updated to modular packages
* ❌ OpenAI quota error → Switched to Groq
* ❌ Model deprecation → Updated to latest supported model
* ❌ LangGraph state error → Passed query across nodes

---

## 📈 Future Improvements

* 🔹 LLM-based router (instead of keyword matching)
* 🔹 Streamlit UI for better user experience
* 🔹 Multi-source scraping (blogs, docs, integrations)
* 🔹 Support for mixed queries (RAG + SERP together)

---

## 🎥 Demo

Include a short demo video showing:

* Architecture explanation
* Live chatbot interaction
* Code walkthrough

---

## 🏁 Conclusion

This project demonstrates:

* RAG implementation
* Tool calling with SERP API
* LangGraph workflow design

It is modular, scalable, and production-ready with minor enhancements.

---

## 🙌 Author

Swati Kumar
Debales AI Intern Assignment Submission
