![Python](https://img.shields.io/badge/Python-3.12-blue)

![FastAPI](https://img.shields.io/badge/FastAPI-green)

![React](https://img.shields.io/badge/React-blue)

![TypeScript](https://img.shields.io/badge/TypeScript-blue)

![AI](https://img.shields.io/badge/AI-RAG-orange)

![License](https://img.shields.io/badge/license-MIT-green)


# 🤖 AI Document Assistant

### Full-Stack RAG Chatbot built with React & FastAPI


An AI-powered full-stack document assistant that combines document retrieval with external tool integration.

The application can:

- 📄 Answer questions from PDF, Markdown and TXT documents
- 🔧 Retrieve dynamic information through external tools
- 🧠 Route requests using intent detection
- ⚡ Provide a clean React chat interface backed by FastAPI

---

## 🚀 Tech Stack

### 🧠 AI

- Custom Retrieval Pipeline
- RAG-inspired Architecture
- Rule-based Intent Detection
- Tool Calling
- Multi-format Document Processing

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
│   ├── data/                  # Static documents
│   │   ├── employee_guide.md
│   │   ├── handbook.pdf
│   │   └── vacation_policy.txt
│   ├── requirements.txt       # Python dependencies
│   └── README.md              # Backend documentation
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
   (PDF, TXT, Markdown)          (Vacation API)
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

- FastAPI Development
- REST APIs
- React
- TypeScript
- Python
- Document Processing
- Retrieval-Augmented Generation (Concept)
- Prompt Engineering Concepts
- Software Architecture
- Clean Code

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
## 📝 Prompt Engineering

The application uses reusable prompt templates to prepare retrieved document context before sending it to a Large Language Model.

Current workflow:

1. Retrieve relevant documents
2. Inject context into a reusable prompt template
3. Include source references
4. Prepare the prompt for LLM processing

This architecture separates retrieval logic from prompt generation, making the system easier to maintain and extend.

---

## 🚀 Roadmap

- Prompt Templates
- OpenAI Integration
- LangChain
- Sentence Embeddings
- ChromaDB
- Conversation Memory
- Streaming Responses
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

## 📚 Learning Journey

This project evolves alongside my Generative AI learning path.

Current milestones:

- ✅ Prompt Engineering
- ✅ ChatGPT for Developers
- ✅ AI and Developer Productivity

Upcoming upgrades:

- LangChain
- Prompt Flow
- ChromaDB
- LLM Integration
---