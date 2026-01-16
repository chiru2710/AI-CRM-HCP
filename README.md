
Each record contains:
- Interaction ID (UUID)  
- HCP Name  
- Interaction Type  
- Purpose  
- Samples Given (Boolean)  
- Follow-up Date  
- AI Summary  
- Timestamp  

---

### 🔹 7) FastAPI Backend with REST APIs

Two main endpoints:

**POST /log-interaction/**
- Accepts structured form data  
- Saves directly to database  

**POST /chat-log/**
- Accepts natural language text  
- Processes via LangGraph + Groq  
- Converts to structured data and stores in DB  

---

### 🔹 8) React + Redux Frontend

- Two modes in UI:
  - Form Mode  
  - Chat Mode  
- Redux manages UI state (mode switching)  
- Axios handles API communication with FastAPI  

---

### 🔹 9) Error Handling & AI Fallback

- If Groq API fails, system uses a safe fallback summary instead of crashing  
- Prevents 500 errors in production  

---

### 🔹 10) Scalable & Modular Design

The project is designed to be scalable and modular, allowing future additions such as:
- User Authentication  
- Role-Based Access Control  
- Analytics Dashboard  
- Mobile App Integration  

---

## 📂 Project Structure

AI-First-CRM-HCP/
│
├── backend/
│ ├── main.py
│ ├── database.py
│ ├── models.py
│ ├── routes.py
│ ├── langgraph_agent.py
│ ├── .env
│ └── requirements.txt
│
└── frontend/
├── src/
│ ├── App.js
│ ├── store.js
│ ├── interactionSlice.js
│ ├── api.js
│ └── components/
│ └── LogInteractionScreen.js
└── package.json


---

## ▶️ How to Run the Project

### 🔹 Backend Setup

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

Backend will run at:
👉 http://127.0.0.1:8000

### 🔹 frontend Setup
cd frontend
npm install
npm start

Frontend will run at:
👉 http://localhost:3000


Developed By:
JANGILI Ch M Srinivasa Vara Prasad
B.Tech CSE
CGPA: 8.6
