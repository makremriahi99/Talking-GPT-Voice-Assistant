# Assistente Vocale GPT — Chatbot con Voce in Italiano

Assistente AI vocale che risponde a voce in italiano: riceve un messaggio di testo, genera una risposta con **GPT-4o-mini** e la legge ad alta voce usando la sintesi vocale **gTTS**.

## Come funziona

```
Scrivi un messaggio
    └─ GPT-4o-mini genera la risposta
    └─ gTTS converte il testo in audio italiano
    └─ L'audio viene riprodotto automaticamente
```

## File

| File | Descrizione |
|---|---|
| `chatparla.py` | Chatbot principale — risposta testuale + audio |
| `CHATGPT.PY` | Chatbot solo testo (senza audio) |
| `GENERALE.py` | Esempio standalone di sintesi vocale con gTTS |

## Come si usa

```bash
pip install openai gtts
```

Imposta la chiave API come variabile d'ambiente:

```bash
# Windows
set OPENAI_API_KEY=la-tua-chiave

# Mac/Linux
export OPENAI_API_KEY=la-tua-chiave
```

Avvia il chatbot:

```bash
python chatparla.py
```

## Tecnologie

- `openai` — GPT-4o-mini per la generazione delle risposte
- `gTTS` (Google Text-to-Speech) — sintesi vocale in italiano
- Python 3

## Tag

`python` `openai` `gpt-4o-mini` `text-to-speech` `gtts` `assistente-vocale` `chatbot` `italiano` `ai`
