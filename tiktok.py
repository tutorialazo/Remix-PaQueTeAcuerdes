import tkinter as tk
from tkinter import messagebox

frases = [
    "Que yo soy tu gatito y vos sos mi bebé",
    "Yo soy tu gatita, miau, kitty, ¡uy!",
    "Dulcecita como un daiquiri",
    "Quiero que fumemo' y quedemo' chillin'",
    "Solo con vos se me prende el feelin'",
    "Arranca el toque, sé que te re da"
]
indice = 0
def siguiente_frase():
    global indice
    if indice < len(frases) - 1:
        indice += 1
        etiqueta_frase.config(text=frases[indice])
    else:
        messagebox.showinfo(
            "Final",
            "Tiagon PZK, Feid, BM, La Joaqui - Pa' Que Te Acuerdes (Remix)\n\nBy Chigne"
        )
        indice = 0
        etiqueta_frase.config(text=frases[indice])

ventana = tk.Tk()
ventana.title("Frases de la Canción")
ventana.geometry("400x200")

etiqueta_frase = tk.Label(ventana, text=frases[indice], font=("Arial", 14), wraplength=400)
etiqueta_frase.pack(pady=60)

boton_ok = tk.Button(ventana, text="OK", command=siguiente_frase, font=("Arial", 14))
boton_ok.pack()

ventana.mainloop()
