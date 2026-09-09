![Python](https://img.shields.io/badge/Python-3.12-blue)

![FastAPI](https://img.shields.io/badge/FastAPI-green)

![React](https://img.shields.io/badge/React-blue)

![TypeScript](https://img.shields.io/badge/TypeScript-blue)

![AI](https://img.shields.io/badge/AI-RAG-orange)

![License](https://img.shields.io/badge/license-MIT-green)


# 🤖 AI Document Assistant

### Full-Stack RAG Application with LangChain, OpenAI, React & FastAPI

An AI-powered full-stack document assistant that combines Retrieval-Augmented
Generation (RAG), LangChain, OpenAI and external tool integration.

The application can:

- 📄 Answer questions from PDF, Markdown and TXT documents
- 🧠 Generate grounded answers using retrieved document context
- 🔗 Orchestrate the LLM pipeline with LangChain
- 💬 Use structured prompt templates for consistent responses
- 🔧 Retrieve dynamic information through external tools
- 🧭 Route requests using intent detection
- ⚡ Provide a responsive React + TypeScript chat interface backed by FastAPI

---

## 🚀 Tech Stack

### 🧠  AI / LLM

- LangChain
- OpenAI / GPT-4.1-mini
- Retrieval-Augmented Generation (RAG)
- LangChain ChatPromptTemplate
- LCEL (LangChain Expression Language)
- StrOutputParser
- Prompt Engineering
- Context Injection
- Custom Document Retrieval
- Rule-based Intent Detection
- External Tool Integration

### ⚙️ Backend

- Python
- FastAPI
- Pydantic
- Uvicorn

### 🎨 Frontend

- React
- TypeScript
- Tailwind CSS

### 🛠 Development

- Git
- GitHub
- VS Code

---



## 📂 Project Structure

```
chatbot-project/
│
├── backend/
│   ├── main.py                # FastAPI entry point
    ├── app/                # FastAPI entry point
│   │    ├── models.py              # Request/response schemas
│   │    ├── rag.py                 # Document retrieval logic
│   │    ├── router.py              # Intent detection
│   │    ├── tools.py               # External service (mocked)
│   │    ├── loaders/               # Document loaders
│   │    │   ├── pdf_loader.py
│   │    │   ├── txt_loader.py
│   │    │   ├── md_loader.py
│   │    │   └── document_loader.py
│   │    ├── llm_service.py     # LangChain + OpenAI integration
│   │    ├── models.py          # Request/response schemas
│   │    ├── prompts.py         # LangChain prompt templates
│   │    ├── rag.py             # Document retrieval + context
│   │    ├── router.py          # Intent detection
│   │    └── tools.py           # External tools / mocked services
│   ├── data/                  # Static documents
│   │   ├── employee_guide.md
│   │   ├── handbook.pdf
│   │   └── vacation_policy.txt
│   ├── requirements.txt       # Python dependencies
│   ├── README.md              # Backend documentation
│   └── .env
│
├── frontend/
│   └── chatbot/
│       ├── src/               # React source code
│       ├── public/
│       ├── index.html
│       ├── package.json
│       ├── tailwind.config.js
│       ├── tsconfig.json
│       └── README.md          # Frontend documentation
│
├── .gitignore
├── README.md                  # Main project documentation
```

---

## 🧩 Architecture Overview

```
User → React Frontend → FastAPI Backend
                             ↓
                  ┌─────────────────────┐
                  │   Intent Detection  │
                  └─────────┬───────────┘
                            │
           ┌────────────────┴──────────────┐
           │                               │
   📄 Document Search (RAG)       🔧 External Tool
   (PDF, TXT, Markdown)             (Vacation API)
                                     Tool Request
             │                             
             ▼                             
      Custom Retrieval                
             │                        
             ▼
      Relevant Context
             │
             ▼
    LangChain ChatPromptTemplate
             │
             ▼
          ChatOpenAI
       (GPT-4.1-mini)
             │
             ▼
       StrOutputParser
             │
             ▼
       Grounded Answer
```

---
## ✨ Features

- Document Question Answering
- Multi-format Document Support
- Intent Detection
- External Tool Integration
- Source References
- REST API
- Responsive React UI

## 💡 Skills Demonstrated

- Generative AI Application Development
- Retrieval-Augmented Generation (RAG)
- LangChain
- OpenAI API Integration
- Prompt Engineering
- Context Injection
- LCEL
- LLM Response Parsing
- FastAPI
- REST API Development
- React
- TypeScript
- Python
- Document Processing
- Intent Detection
- Tool Integration
- Full-Stack Architecture

---

## ⚙️ Setup & Run

### 1️⃣ Clone repository

```
git clone <https://github.com/NourheneMbarek/chatbot-project>
cd chatbot-project
```

---

### 2️⃣ Backend Setup

```
cd backend

# create virtual environment
python -m venv venv

# activate
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# install dependencies
pip install -r requirements.txt

# run server
uvicorn main:app --reload
```

👉 Backend runs on: `http://127.0.0.1:8000`

---

### 3️⃣ Frontend Setup

```
cd frontend

npm install
npm run dev
```

👉 Frontend runs on: `http://localhost:5173`

---

## 💬 How It Works

### 1. Document-based answers (RAG)

* Documents are loaded at startup (`/backend/data`)
* Supported formats:

  * PDF
  * TXT
  * Markdown
* User questions are matched against document content
* Relevant answer is returned with sources

---

### 2. Dynamic data (Tool calling)

The chatbot detects intent:

* Example: **"How many vacation days do I have left?"**

Then:

* Calls a mocked external service (`tools.py`)
* Returns dynamic data instead of document answer

---

## 🧠 Intent Detection

Simple rule-based detection:

* `TOOL_VACATION` → calls external service
* Otherwise → document search

---

## 📡 API Endpoints

### GET `/`

Health check

```
{
  "message": "Backend running"
}
```

---

### POST `/chat`

Request:

```
{
  "question": "What is the vacation policy?"
}
```

Response:

```
{
  "answer": "...",
  "type": "document",
  "sources": ["guide.md"]
}
```

---

## 🧪 Example Questions

* "What is the vacation policy?"
* "How many vacation days do I have left?"
* "What does the handbook say about sick leave?"

---

## 📌 Design Decisions

* **Simple RAG** (no external vector DB) → keeps project lightweight
* **Rule-based intent detection** → easy to understand and extend
* **Separated layers**:

  * `rag.py` → document logic
  * `tools.py` → external data
  * `router.py` → intent detection

---
## 📝 Prompt Engineering with LangChain

V4 uses LangChain's `ChatPromptTemplate` to separate system instructions
from user input and retrieved document context.

The system prompt instructs the model to:

- Answer only from retrieved context
- Avoid inventing information
- Return a fallback response when information is unavailable
- Keep responses concise
- Avoid exposing technical file paths

### Pipeline

Question + Retrieved Context
            ↓
    ChatPromptTemplate
            ↓
        ChatOpenAI
            ↓
     StrOutputParser
            ↓
      Final Answer
---

## 🚀 Roadmap

### ✅ Completed

- Custom Document Retrieval
- Multi-format Document Loading
- Prompt Templates
- OpenAI Integration
- LangChain Integration
- LCEL Pipeline
- Intent Detection
- External Tool Integration

### 🔜 Next

- Sentence Embeddings
- Vector Similarity Search
- ChromaDB Vector Store
- Conversation Memory
- Streaming Responses
- Advanced Tool Calling / AI Agents
- Docker
- CI/CD

---

## 👩‍💻 Author

Nourhene Mbarek

---

## 🎯 Project Goal

The goal of this project is to explore modern AI application architecture by combining:

- Full-Stack Development
- Retrieval-Augmented Generation
- Prompt Engineering
- External Tool Integration
- Scalable Software Design

The project will continue to evolve with new Generative AI technologies and production-ready features.

---

## 📚 Learning → Implementation

This project evolves alongside my Generative AI learning journey.

### ✅ Learning Completed

- AI and Developer Productivity
- Introduction to Prompt Engineering for Generative AI
- Prompt Engineering with ChatGPT
- Prompt Engineering Skills for Developers
- Prompt Engineering with LangChain

### 🛠 Applied in this Project

- Prompt Engineering
- Reusable Prompt Templates
- Context Injection
- Retrieval-Augmented Generation
- OpenAI Integration
- LangChain
- LCEL
- Grounded LLM Responses

### 🔜 Next Learning & Implementation

- Embeddings
- Vector Databases
- ChromaDB
- Conversation Memory
- AI Agents & Advanced Tool Calling
---