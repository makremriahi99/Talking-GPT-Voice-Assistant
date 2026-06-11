from gtts import gTTS

# Example: generate a spoken Italian message
text = "Ciao! Questo è un esempio di sintesi vocale in italiano."
tts = gTTS(text=text, lang='it')
tts.save("output.mp3")
print("Audio saved as output.mp3")

