# Chatbot
An interactive AI chatbot built using Python, Streamlit, and Gemini API. Designed to respond to user queries with text-based answers.
# Gemini Chatbot using Streamlit 💬⚡

This is a simple yet powerful chatbot application built using **Google's Gemini API** and **Streamlit UI**. The bot takes user input and responds in natural language, just like ChatGPT.

---

## 🧠 Project Overview
User Input ---> Gemini Model ---> Bot Response (Text)

This chatbot interacts with Google’s **Generative AI** model (Gemini 2.0) using API key authentication. The frontend is developed with **Streamlit**, giving a clean and interactive UI.

---

## 🔧 Setup & Tech Stack

| Purpose                      | Technology Used         |
|-----------------------------|--------------------------|
| UI Framework                | Streamlit                |
| Secrets Management          | python-dotenv            |
| Generative AI Model         | google-generativeai (Gemini) |
| Dependency Management       | uv (UltraViolet)         |
| Environment                 | Python 3.11 (venv)        |

---

## 🔑 How it Works

1. **User enters a query** via Streamlit UI.
2. The query is passed to **Gemini 2.0 model** using `google-generativeai`.
3. **API Key** is stored securely in a `.env` file and accessed using `python-dotenv`.
4. Gemini processes the input and sends **text-based response**.
5. Response is shown back in the same UI.

---

## 📂 Folder Structure
hltro/
│
├── .env # API key (not pushed to GitHub)
├── app.py # Main chatbot logic
├── requirements.txt # All dependencies
├── pyproject.toml # uv project config
├── uv.lock # Package lock file
└── README.md # This file

2. Create virtual environment
uv venv
.venv\Scripts\activate
3. Install dependencies
