# 🤖 Django AI Chatbot (Groq API)

A **ChatGPT-style conversational chatbot** built using **Django** and **Groq API**.
It supports **user authentication, chat history, multiple conversations, Markdown responses, and a modern UI**.

---

## 🚀 Features

* 🔐 User Authentication (Register / Login / Logout)
* 💬 ChatGPT-style chat interface
* 🧠 AI responses using **Groq API**
* 📜 Chat history stored in database
* ➕ Create multiple chat sessions
* ❌ Delete conversations
* 🌙 Dark / Light theme toggle
* ✨ Markdown formatted AI responses
* ⌨ Typing animation
* 🔄 Auto-scroll chat
* 📱 Responsive UI

---

## 🏗 Project Structure

```
ai_chatbot/
│
├── accounts/          # User authentication app
│
├── chats/             # Chatbot logic and chat sessions
│
├── templates/         # HTML templates
│
├── manage.py
│
└── requirements.txt
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/yourusername/django-ai-chatbot.git
cd django-ai-chatbot
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv venv
```

Activate it:

Windows

```
venv\Scripts\activate
```

Mac/Linux

```
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Add Groq API Key

Create a `.env` file or add inside `settings.py`.

Example:

```
GROQ_API_KEY=your_api_key_here
```

Get your key from:

https://console.groq.com/

---

### 5️⃣ Run Migrations

```
python manage.py makemigrations
python manage.py migrate
```

---

### 6️⃣ Create Superuser (Optional)

```
python manage.py createsuperuser
```

---

### 7️⃣ Run the Server

```
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000
```

---

## 🧠 AI Model

This project uses **Groq LLM API**.

Example model:

```
llama3-70b-8192
```

You can change the model in:

```
views.py
```

---

## 🖥 Technologies Used

* **Python**
* **Django**
* **Groq API**
* **HTML / CSS / JavaScript**


## 👨‍💻 Author

Built by **Ashutosh Rath**

---

## ⭐ If you like this project

Give it a **star on GitHub ⭐**
