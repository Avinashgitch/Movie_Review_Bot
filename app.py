import os
import requests
import gradio as gr
from dotenv import load_dotenv

# Load API keys
load_dotenv()
OMDB_API_KEY = os.getenv("OMDB_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

OMDB_URL = "http://www.omdbapi.com/"
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

chat_history = []
last_movie = None

def fetch_movie_details(movie_name):
    """Fetch details from OMDb API."""
    params = {"t": movie_name, "apikey": OMDB_API_KEY}
    r = requests.get(OMDB_URL, params=params)
    if r.status_code == 200:
        data = r.json()
        if data.get("Response") == "True":
            return data
    return None

def chat_with_groq(user_message):
    """Send message to Groq API with history."""
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    messages = [
        {"role": "system", "content": "You are a friendly and knowledgeable movie expert. You can review movies, answer questions, recommend films, and share trivia. Always keep responses spoiler-free."}
    ] + chat_history + [{"role": "user", "content": user_message}]

    payload = {
        "model": "llama3-8b-8192",
        "messages": messages,
        "temperature": 0.8
    }

    r = requests.post(GROQ_URL, headers=headers, json=payload)
    if r.status_code == 200:
        reply = r.json()["choices"][0]["message"]["content"].strip()
        chat_history.append({"role": "user", "content": user_message})
        chat_history.append({"role": "assistant", "content": reply})
        return reply
    else:
        return f"❌ API Error: {r.text}"

def moviebot(user_input):
    global last_movie
    movie_data = fetch_movie_details(user_input)

    if movie_data:  # If OMDb found the movie
        last_movie = movie_data.get("Title")
        movie_info = f"""
        Title: {movie_data.get('Title')}
        Year: {movie_data.get('Year')}
        Genre: {movie_data.get('Genre')}
        Director: {movie_data.get('Director')}
        Actors: {movie_data.get('Actors')}
        Plot: {movie_data.get('Plot')}
        """
        prompt = f"Please write a short, spoiler-free review and answer any related questions for the movie:\n{movie_info}"
        return chat_with_groq(prompt)

    elif last_movie and "?" in user_input:  # Follow-up question
        context_info = f"User is asking about the movie '{last_movie}'. Question: {user_input}"
        return chat_with_groq(context_info)

    else:  # General movie question
        return chat_with_groq(user_input)

# Gradio UI
with gr.Blocks(theme="default") as demo:
    gr.Markdown("## 🎬 MovieBot - Chat About Movies")
    chatbot = gr.Chatbot()
    msg = gr.Textbox(placeholder="Type a movie name or ask a movie question...")
    clear = gr.Button("Clear Chat")

    def respond(message, chat_state):
        bot_reply = moviebot(message)
        chat_state.append((message, bot_reply))
        return chat_state, ""

    msg.submit(respond, [msg, chatbot], [chatbot, msg])
    clear.click(lambda: [], None, chatbot)

if __name__ == "__main__":
    demo.launch()
