from tkinter import *
from tkinter import ttk
from deep_translator import GoogleTranslator

root = Tk()
root.title("Language Translation Tool")
root.geometry("600x450")

Label(root, text="Enter Text", font=("Arial", 14)).pack()

text_input = Text(root, height=6, width=60)
text_input.pack()

languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "French": "fr",
    "Spanish": "es",
    "German": "de"
}

source = ttk.Combobox(root, values=list(languages.keys()))
source.set("English")
source.pack(pady=5)

target = ttk.Combobox(root, values=list(languages.keys()))
target.set("Hindi")
target.pack(pady=5)

output = Text(root, height=6, width=60)
output.pack()

def translate():
    text = text_input.get("1.0", END).strip()

    translated = GoogleTranslator(
        source=languages[source.get()],
        target=languages[target.get()]
    ).translate(text)

    output.delete("1.0", END)
    output.insert(END, translated)

Button(root, text="Translate", command=translate).pack(pady=10)

root.mainloop()