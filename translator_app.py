"""
TASK 1: Language Translation Tool
----------------------------------
A desktop GUI application that translates text between languages.

Features:
- Text input box
- Source & target language selection (dropdowns)
- Translation using Google Translate (via deep-translator, no API key required)
- Copy-to-clipboard button
- Text-to-speech (TTS) for both input and translated text

Run with:  python translator_app.py
"""

import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator
import pyttsx3

# ---------------------------------------------------------
# Supported languages (display name -> language code)
# ---------------------------------------------------------
LANGUAGES = {
    "Auto Detect": "auto",
    "English": "en",
    "Urdu": "ur",
    "Arabic": "ar",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Chinese (Simplified)": "zh-CN",
    "Hindi": "hi",
    "Turkish": "tr",
    "Russian": "ru",
    "Japanese": "ja",
    "Korean": "ko",
    "Italian": "it",
    "Portuguese": "pt",
}

# Initialize the text-to-speech engine once (reused for every "speak" click)
engine = pyttsx3.init()


class TranslatorApp:
    def __init__(self, root):
        self.root = root
        root.title("Language Translation Tool")
        root.geometry("650x560")
        root.resizable(False, False)

        tk.Label(root, text="Language Translation Tool", font=("Arial", 16, "bold")).pack(pady=10)

        # --- Language selection row ---
        lang_frame = tk.Frame(root)
        lang_frame.pack(pady=5)

        tk.Label(lang_frame, text="From:").grid(row=0, column=0, padx=5)
        self.source_lang = ttk.Combobox(lang_frame, values=list(LANGUAGES.keys()), width=20, state="readonly")
        self.source_lang.set("Auto Detect")
        self.source_lang.grid(row=0, column=1, padx=5)

        tk.Label(lang_frame, text="To:").grid(row=0, column=2, padx=5)
        self.target_lang = ttk.Combobox(lang_frame, values=list(LANGUAGES.keys()), width=20, state="readonly")
        self.target_lang.set("English")
        self.target_lang.grid(row=0, column=3, padx=5)

        tk.Button(lang_frame, text="⇄ Swap", command=self.swap_languages, width=8).grid(row=0, column=4, padx=8)

        # --- Input box ---
        tk.Label(root, text="Enter Text:").pack(anchor="w", padx=20)
        self.input_text = tk.Text(root, height=8, width=75, wrap="word", font=("Arial", 11))
        self.input_text.pack(padx=20, pady=5)

        # --- Action buttons ---
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=8)

        tk.Button(btn_frame, text="Translate", command=self.translate_text,
                  bg="#4CAF50", fg="white", width=14, font=("Arial", 10, "bold")).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="🔊 Speak Input", command=lambda: self.speak(self.input_text.get("1.0", tk.END)),
                  width=14).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Clear All", command=self.clear_all, width=12).grid(row=0, column=2, padx=5)

        # --- Output box ---
        tk.Label(root, text="Translated Text:").pack(anchor="w", padx=20)
        self.output_text = tk.Text(root, height=8, width=75, wrap="word", bg="#f0f0f0", font=("Arial", 11))
        self.output_text.pack(padx=20, pady=5)

        # --- Output action buttons ---
        out_btn_frame = tk.Frame(root)
        out_btn_frame.pack(pady=5)
        tk.Button(out_btn_frame, text="📋 Copy Result", command=self.copy_result, width=14).grid(row=0, column=0, padx=5)
        tk.Button(out_btn_frame, text="🔊 Speak Result", command=lambda: self.speak(self.output_text.get("1.0", tk.END)),
                  width=14).grid(row=0, column=1, padx=5)

        self.status = tk.Label(root, text="Ready", fg="gray", font=("Arial", 9))
        self.status.pack(pady=5)

    # -------------------------------------------------------------
    def translate_text(self):
        text = self.input_text.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Empty Input", "Please enter text to translate.")
            return

        src = LANGUAGES[self.source_lang.get()]
        tgt = LANGUAGES[self.target_lang.get()]

        if src == tgt:
            messagebox.showwarning("Same Language", "Source and target languages must be different.")
            return

        try:
            self.status.config(text="Translating...", fg="blue")
            self.root.update_idletasks()

            translated = GoogleTranslator(source=src, target=tgt).translate(text)

            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, translated)
            self.status.config(text="Translation complete.", fg="green")
        except Exception as e:
            self.status.config(text="Error occurred.", fg="red")
            messagebox.showerror(
                "Translation Error",
                f"Could not translate text.\n\nMake sure you are connected to the internet.\n\nDetails: {e}"
            )

    def copy_result(self):
        result = self.output_text.get("1.0", tk.END).strip()
        if result:
            self.root.clipboard_clear()
            self.root.clipboard_append(result)
            self.status.config(text="Copied to clipboard!", fg="green")
        else:
            messagebox.showwarning("Nothing to Copy", "Translate some text first.")

    def speak(self, text):
        text = text.strip()
        if text:
            engine.say(text)
            engine.runAndWait()
        else:
            messagebox.showwarning("Nothing to Speak", "There is no text to read aloud.")

    def swap_languages(self):
        # Auto Detect can't be a target, so guard against that
        if self.source_lang.get() == "Auto Detect":
            messagebox.showinfo("Cannot Swap", "Pick a specific source language before swapping.")
            return
        src, tgt = self.source_lang.get(), self.target_lang.get()
        self.source_lang.set(tgt)
        self.target_lang.set(src)

    def clear_all(self):
        self.input_text.delete("1.0", tk.END)
        self.output_text.delete("1.0", tk.END)
        self.status.config(text="Ready", fg="gray")


if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()
