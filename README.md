# 🚀 AI-First CRM HCP Module

## 📌 Objective

This project is an **AI-First Customer Relationship Management (CRM) module** designed for Life Sciences field representatives to log and manage their interactions with Healthcare Professionals (HCPs).

The system supports:
- **Structured Form-based logging**, and  
- **Conversational AI-based logging using LangGraph and Groq LLM**,  

making data entry faster, smarter, and more user-friendly for field teams.

---

## 🛠 Tech Stack

### **Frontend**
- React  
- Redux (State Management)  
- Axios (API Communication)  
- Google Font: Inter  

### **Backend**
- FastAPI (Python)  
- SQLAlchemy ORM  
- Uvicorn Server  

### **AI & Automation**
- **LangGraph** (AI Agent Framework)  
- **Groq LLM – gemma2-9b-it**

### **Database**
- **MySQL** (`ai_crm_db`)

---

## ✨ Features

### 🔹 1) Dual Mode Interaction Logging

#### 📌 Form Mode (Structured Logging)
Field representatives can log interactions using a structured form that includes:
- HCP Name  
- Interaction Type (Visit, Call, Email, etc.)  
- Purpose of Visit  
- Samples Given (Yes/No)  
- Follow-up Date  

All form data is directly validated and stored in the MySQL database.

#### 📌 AI Chat Mode (Conversational Logging)
Users can describe their interaction in natural language, for example:

> “I met Dr. Anitha today and provided samples.”

The AI agent processes this text, extracts key details, summarizes it, and stores structured data in the database.

---

### 🔹 2) AI-Powered Processing with LangGraph

A **LangGraph AI agent** acts as the intelligence layer that:
- Understands user intent from chat input  
- Calls appropriate tools dynamically  
- Coordinates between LLM and database operations  

---

### 🔹 3) LLM-Based Summarization (Groq)

Uses **Groq LLM (gemma2-9b-it)** to:
- Summarize long chat descriptions  
- Extract meaningful insights  
- Generate concise interaction summaries  

**Example:**

Input:
> “Met the doctor regarding clinical trial updates, discussed dosage, side effects, and market trends.”

AI Summary:
> “Discussion focused on clinical trial progress, dosage, and market trends.”

---

### 🔹 4) Automated Entity Extraction

From chat text, the system automatically extracts:
- HCP Name (e.g., Dr. Anitha)  
- Whether samples were given  
- Purpose of interaction  
- Type of interaction (Visit/Call/Chat)  

---

### 🔹 5) 5 LangGraph AI Tools (Core Requirement)

The LangGraph agent uses at least five tools:

1. **Log Interaction Tool**  
   - Saves structured interaction data into MySQL  
   - Works for both form and chat inputs  

2. **Edit Interaction Tool**  
   - Allows modification of previously logged interactions  

3. **Fetch Interaction History Tool**  
   - Retrieves past interactions of a specific doctor  

4. **Summarization Tool (LLM-Based)**  
   - Uses Groq to generate concise summaries  

5. **Entity Extraction Tool**  
   - Identifies key details such as:
     - Doctor name  
     - Samples given  
     - Visit type  

---

### 🔹 6) Centralized Interaction Database (MySQL)

All interactions (Form + Chat) are stored in a single table:



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

### 🔹 Frontend Setup
cd frontend
npm install
npm start
