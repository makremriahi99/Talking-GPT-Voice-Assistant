from openai import OpenAI
from gtts import gTTS
import os

# Inizializza il client OpenAI
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

while True:
    prompt = input("You: ")

    # Genera la risposta dell'AI
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="gpt-4o-mini"
    )
    
    response_message = chat_completion.choices[0].message.content
    print("AI:", response_message)

    # Converte il testo in audio
    tts = gTTS(text=response_message, lang="it")  # Puoi cambiare la lingua, es. "en" per l'inglese
    tts.save("response.mp3")

    # Riproduce l'audio (funziona su Windows, macOS e Linux)
    os.system("start response.mp3" if os.name == "nt" else "mpg321 response.mp3")
