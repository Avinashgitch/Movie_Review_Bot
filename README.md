# 🎬 Movie Reviewer & Q&A Bot

An AI-powered chatbot that provides **movie reviews, trivia, and recommendations** in a natural conversational style.  
It combines the **OMDb API** for accurate movie details and the **Groq API** for AI-generated responses.  
The bot runs in a **Gradio web interface** so users can easily chat with it from their browser.

---

## 🚀 Features
- Search for any movie and get a **spoiler-free review**
- Retrieve **movie metadata** (title, release year, cast, genre, plot, IMDb rating)
- Ask **follow-up questions** about the same movie
- Get **general movie-related answers** (e.g., recommendations, trivia)
- Works for **multiple genres, languages, and release years**
- Simple, clean **web interface** built with Gradio

---

## 🛠 Tech Stack
- **Backend APIs:** [OMDb API](https://www.omdbapi.com/), [Groq API](https://groq.com/)
- **Language:** Python
- **Libraries:** `requests`, `python-dotenv`, `gradio`
- **UI:** Gradio web interface

---

## 📂 Installation & Setup

### 1️⃣ Clone this repository
```bash
git clone https://github.com/yourusername/Movie_Review_Bot.git
cd Movie_Review_Bot
```


### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```


### 3️⃣ Create a .env file in the root folder
Add your API keys inside .env:
```bash
OMDB_API_KEY=your_omdb_api_key_here
GROQ_API_KEY=your_groq_api_key_here
```
