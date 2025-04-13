import tkinter as tk
from tkinter import ttk
from deep_translator import GoogleTranslator

class TranslatorApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Translator App")
        self.root.geometry("600x400")

        # Create an instance of GoogleTranslator
        translator_instance = GoogleTranslator()
        self.langs = translator_instance.get_supported_languages()

        # Input Text
        self.input_text = tk.Text(self.root, height=8, width=60, font=("Arial", 12))
        self.input_text.pack(pady=10)

        # Language Dropdowns
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        self.src_lang = ttk.Combobox(frame, values=self.langs)
        self.src_lang.set("english")
        self.src_lang.pack(side="left", padx=10)

        self.dest_lang = ttk.Combobox(frame, values=self.langs)
        self.dest_lang.set("amharic")
        self.dest_lang.pack(side="left", padx=10)

        # Translate Button
        self.translate_btn = tk.Button(self.root, text="Translate", command=self.translate_text)
        self.translate_btn.pack(pady=10)

        # Output Text
        self.output_text = tk.Text(self.root, height=8, width=60, font=("Arial", 12), fg="blue")
        self.output_text.pack(pady=10)

        self.root.mainloop()

    def translate_text(self):
        # Get input text
        input_text = self.input_text.get("1.0", tk.END).strip()
        if not input_text:
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, "Please enter text to translate.")
            return

        # Get source and destination languages
        src_lang = self.src_lang.get()
        dest_lang = self.dest_lang.get()

        if not src_lang or not dest_lang:
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, "Please select both source and destination languages.")
            return

        try:
            # Perform translation
            translator = GoogleTranslator(source=src_lang, target=dest_lang)
            translated_text = translator.translate(input_text)

            # Display translated text
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, translated_text)
        except Exception as e:
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, f"Error: {str(e)}")

TranslatorApp()