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

---
## 2. Create virtual environment:
   uv venv
   .venv\Scripts\activate
   
---

## 3. Install dependencies:
uv add -r requirements.txt

---

## 4. Add your API key:

Create a file named .env : GOOGLE_API_KEY=your_api_key_here

---

## 5.  Run the App:

streamlit run app.py

---

👩‍💻 Created By
Anjali Pal
🎓 B.Tech (CS-AI), Arya College of Engineering, Jaipur
📧 anjalipal2912@gmail.com

---
🏁 Purpose :
This project is part of my learning journey in AI + Web UI Development.
It showcases backend integration with Gemini (Generative AI) and frontend skills using Streamlit — a perfect example of combining ML and full-stack development.

---

# 🌱 Future Enhancements

Add voice input and output support
Save and display chat history
Allow switching between text, image, and audio models

---

🌍 Live Demo (Optional)
Add a link here when you deploy via Streamlit Cloud / Render / HuggingFace

---

🛡️ License
MIT License — free to use with proper credit.

---

### ✅ What To Do Next

1. Go to your GitHub repo (`Chatbot`)
2. Click **Add file → Create new file**
3. Name it `README.md`
4. Paste the content above
5. Write commit message:  
   `Added detailed README documentation`
6. Click “Commit new file”

---

Let me know if you want the file ready in `.md` format to directly upload. I'm here t
