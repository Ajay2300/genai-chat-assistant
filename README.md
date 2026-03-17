An AI-powered chatbot built using Flask and Google Gemini API that answers user queries in real-time. The application is deployed on Render and accessible via a web interface.

🚀 Live Demo

👉 https://genai-chat-assistant-1.onrender.com

🧠 Features

💬 Interactive chat interface

🤖 AI-generated responses using Gemini API

⚡ Fast backend using Flask

🌐 Deployed on cloud (Render)

🔐 Secure API key handling using environment variables

🛠️ Tech Stack

Backend: Python, Flask

AI Model: Google Gemini API

Frontend: HTML, CSS, JavaScript

Deployment: Render

Server: Gunicorn

📂 Project Structure
genai-chat-assistant
│
├── app.py
├── requirements.txt
├── docs.json
│
├── templates/
│   └── index.html
│
└── static/
    └── styles.css
⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/genai-chat-assistant.git
cd genai-chat-assistant
2️⃣ Create virtual environment
python -m venv venv

Activate it:

venv\Scripts\activate
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Add API Key

Create a .env file and add:

GEMINI_API_KEY=your_api_key_here
5️⃣ Run the application
python app.py

Open in browser:

http://127.0.0.1:5000
🌐 Deployment

The project is deployed using Render:

Build Command:

pip install -r requirements.txt

Start Command:

gunicorn app:app
🔒 Security Note

API keys are stored securely using .env

.env is ignored using .gitignore

Never expose API keys in public repositories

📸 Demo

You can record and upload a demo video here (optional).

📈 Future Improvements

Add chat history memory

Improve UI/UX

Use vector databases like FAISS

Add user authentication
