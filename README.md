# 🤖 Simple Chatbot (Full-Stack)

A simple full-stack chatbot application that:

* Answers questions from **static multi-format documents** (PDF, TXT, Markdown)
* Retrieves **dynamic data** (e.g. vacation days) from a mocked external service

---

## 🚀 Tech Stack

### Backend

* Python + FastAPI
* Custom RAG (Retrieval-Augmented Generation)
* Document loaders (PDF, TXT, Markdown)

### Frontend

* React + TypeScript
* Tailwind CSS (chat UI)

---

## 📂 Project Structure

```
chatbot-project/
│
├── backend/
│   ├── main.py
│   ├── rag.py
│   ├── models.py
│   ├── router.py
│   ├── tools.py
│   ├── loaders/
│   └── data/
│
├── frontend/
│
└── README.md

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

## 🔧 Improvements (Future Work)

* Add embeddings (OpenAI / local models)
* Replace rule-based intent with NLP model
* Add authentication (user-specific data)
* Improve UI (chat history, streaming responses)
* Dockerize full application

---

## 👩‍💻 Author

Nourhene Mbarek

---

## ✅ Notes

This project was built as part of a technical assignment to demonstrate:

* Full-stack development
* Document processing
* External service integration
* Clean architecture and separation of concerns

---
