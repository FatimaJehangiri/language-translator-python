# Task 1 — Language Translation Tool

A desktop GUI (Tkinter) app that translates text between languages using Google
Translate under the hood (via the `deep-translator` library — no API key needed).

## Features
- Text input box
- Source & target language dropdowns (+ swap button)
- Translate button → calls Google Translate
- Copy-to-clipboard button
- Text-to-speech for both the input and the translated text

## Why `deep-translator` instead of the official Google Cloud Translate API?
The official Google Cloud Translation API and Microsoft Translator both require a
paid API key/billing account. `deep-translator`'s `GoogleTranslator` wraps the free,
public Google Translate web endpoint, so the project runs with zero API keys or
cost — ideal for an internship/portfolio project. If you want, this can be swapped
later for the official API (see "Optional upgrade" below).

## How to Run (VS Code) — Step by Step

1. **Install Python** (3.9–3.12 recommended) if you don't have it: https://www.python.org/downloads/
2. **Open the folder** `task1_translation` in VS Code.
3. **Open a terminal** in VS Code (`` Ctrl+` ``).
4. **(Recommended) Create a virtual environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # macOS/Linux
   ```
5. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
6. **Run the app:**
   ```bash
   python translator_app.py
   ```
7. A window will open. Type or paste text, choose the "From" and "To" languages,
   click **Translate**, and the result appears in the lower box. Use the copy
   button or the speaker buttons as needed.

> You need an active internet connection for translation to work (the app calls
> Google Translate's web service). If nothing translates, check your Wi-Fi/data
> first.

## Running in Jupyter Notebook instead?
Tkinter GUIs don't render well inside Jupyter. For this task, running it as a
plain `.py` script in VS Code (or `python translator_app.py` from any terminal)
is the recommended and simplest path — stick with that rather than Jupyter.

## Optional upgrade: official Google Cloud Translate API
If your internship wants you to explicitly use the **paid, official** API:
1. Create a Google Cloud project, enable "Cloud Translation API", generate an API key.
2. `pip install google-cloud-translate`
3. Replace the `GoogleTranslator(...).translate(text)` call with a call to the
   `google.cloud.translate_v2` client using your key.
This is optional — the current version already fully satisfies the task requirements.

## Troubleshooting
- **`ModuleNotFoundError: No module named 'deep_translator'`** → you forgot to run
  `pip install -r requirements.txt` (or your venv isn't activated).
- **pyttsx3 has no voice / errors on Linux** → run `sudo apt-get install espeak` first.
- **Translation error / "Request exception"** → almost always a network issue —
  check your internet connection, or that a firewall/VPN isn't blocking Google.
