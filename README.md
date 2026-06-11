# Talking GPT — Voice AI Assistant in Italian

A minimal but complete **voice AI assistant** that listens to your text input, generates a response via GPT-4o-mini, and reads it aloud in Italian using text-to-speech.

## How it works

```
You type a message
    └─ OpenAI GPT-4o-mini generates a response
    └─ gTTS converts the response to Italian speech
    └─ Audio plays automatically
```

## Files

| File | Description |
|---|---|
| `chatparla.py` | Main voice chatbot — GPT response + gTTS playback |
| `CHATGPT.PY` | Text-only chatbot (no audio) |
| `GENERALE.py` | Standalone gTTS example — generates a spoken Italian message |

## Setup

```bash
pip install openai gtts
```

Set your OpenAI API key as an environment variable:

```bash
# Windows
set OPENAI_API_KEY=your-key-here

# Mac/Linux
export OPENAI_API_KEY=your-key-here
```

## Run

```bash
python chatparla.py
```

Type anything and the AI will respond in Italian — both in text and voice.

## Tech stack

- `openai` — GPT-4o-mini for response generation
- `gtts` (Google Text-to-Speech) — Italian speech synthesis
- Python 3

## Topics

`python` `openai` `gpt-4o-mini` `text-to-speech` `gtts` `voice-assistant` `chatbot` `italian` `ai`
