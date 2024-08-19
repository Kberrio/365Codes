import tkinter as tk
from tkinter import ttk
from flask import Flask, request, jsonify
from googletrans import Translator
import threading

# Initialize the translator
translator = Translator()

# Create Flask app
app = Flask(__name__)

@app.route('/translate', methods=['POST'])
def translate_api():
    data = request.json
    text = data.get('text')
    dest = data.get('dest', 'en')
    src = data.get('src', 'auto')
    
    result = translator.translate(text, dest=dest, src=src)
    return jsonify({
        'translated': result.text,
        'src': result.src,
        'dest': result.dest
    })

# GUI
class TranslatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Translator")

        self.text_input = tk.Text(master, height=10, width=50)
        self.text_input.pack(pady=10)

        self.translate_button = ttk.Button(master, text="Translate", command=self.translate)
        self.translate_button.pack(pady=5)

        self.result_label = ttk.Label(master, text="Translation:")
        self.result_label.pack(pady=5)

        self.text_output = tk.Text(master, height=10, width=50)
        self.text_output.pack(pady=10)

    def translate(self):
        text = self.text_input.get("1.0", tk.END).strip()
        result = translator.translate(text, dest='en')
        self.text_output.delete("1.0", tk.END)
        self.text_output.insert(tk.END, result.text)

# Run Flask in a separate thread
def run_flask():
    app.run(debug=False, port=5000)

if __name__ == "__main__":
    # Start Flask in a separate thread
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    # Run the GUI
    root = tk.Tk()
    translator_app = TranslatorApp(root)
    root.mainloop()