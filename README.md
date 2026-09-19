# ✨ AI Content Assistant

A modern, interactive Streamlit application powered by **Google Gemini AI** (`gemini-1.5-flash`) that generates tailored social media posts, captions, attention-grabbing hooks, and relevant hashtags based on target audience, platform, and tone.

---

## 🌟 Features

- **Multi-Platform Optimization**: Formats content specifically for LinkedIn, Instagram, Twitter/X, Facebook, YouTube Community, and Threads.
- **Tailored Control**: Customize by topic, target audience, tone of voice, and content type (educational, promotional, storytelling, etc.).
- **Smooth Animated UI**: Custom CSS animations for headers, card containers, and hover effects.
- **Streamlined Workflow**: View rich formatted Markdown previews along with a raw text box for fast copying.
- **Flexible Configuration**: Supply your API key via sidebar input or environment variables.

---

## 📁 Project Structure

├── app.py              # Main Streamlit application file
├── requirements.txt    # Project dependencies
├── .gitignore          # Git ignore rules for virtualenvs and secrets
└── README.md           # Documentation

---

## 📦 Prerequisites & Installation

### 1. Prerequisites

Ensure you have Python **3.8 or higher** installed. Check your version with:


python --version



### 2. Clone or Setup Project Directory

Create a project folder and place your `app.py`, `requirements.txt`, and `.gitignore` files inside:

```bash
mkdir ai-content-assistant
cd ai-content-assistant

```

### 3. Create a Virtual Environment (Recommended)

```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows (Command Prompt)
python -m venv venv
venv\Scripts\activate

```

### 4. Install Dependencies

```bash
pip install -r requirements.txt

```

---

## 🔑 Setting Up Your Gemini API Key

You need a free Gemini API Key from Google AI Studio.

1. Get your API key at [Google AI Studio](https://aistudio.google.com/?utm_source=gemini).
2. You can provide your key in two ways:
* **In-App Sidebar**: Enter it directly into the secure password input inside the app UI.
* **Environment Variable**:
* **Linux / macOS**:





```bash
       export GEMINI_API_KEY="your_actual_api_key_here"
       

```

```
 - **Windows (CMD)**:

```

```cmd
       set GEMINI_API_KEY=your_actual_api_key_here
       

```

```
 - **Windows (PowerShell)**:

```

```powershell
       $env:GEMINI_API_KEY="your_actual_api_key_here"
       

```

---

## 🏃 Running the Application Locally

Launch the app using Streamlit:

```bash
streamlit run app.py

```

Your default browser will open automatically at `http://localhost:8501`.

---

## ☁️ Deployment on Streamlit Community Cloud

Deploying your assistant online for free takes only a few minutes:

1. **Push to GitHub**:
Push `app.py`, `requirements.txt`, `.gitignore`, and `README.md` to a GitHub repository.
2. **Connect to Streamlit Cloud**:
* Go to [share.streamlit.io](https://share.streamlit.io/?utm_source=gemini) and log in with GitHub.
* Click **New app**.
* Select your repository, branch, and set `app.py` as the main file path.


3. **Configure API Key Secrets**:
* Before deploying, click **Advanced settings...**
* Under **Secrets**, add your API key in TOML format:



```toml
     GEMINI_API_KEY = "your_actual_api_key_here"
     

```

4. **Deploy**: Click **Deploy!** Streamlit will build and host your app live.

---

## 📜 License

This project is licensed under the MIT License.

## 💻 Deployment

link: https://ai-content-assistant-01.streamlit.app/
