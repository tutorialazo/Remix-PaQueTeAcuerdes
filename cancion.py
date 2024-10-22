import tkinter as tk
from tkinter import messagebox

# Lista con las frases de la canción
frases = [
    "Vos eras mi re amor",
    "Siempre nos veíamos",
    "Después te perdí el rastro",
    "Aún te sigo buscando a ver si te cruzo",

    "Y todavía no se dio",
    "Sé que entre nosotros do'",
    "Algo te estás guardando",
    "Vos decime la posta, la bala la aguanto (¿pa' qué me miras así, bebé?)",

    "Pa' que te acuerdes que yo no te olvidé, volvámono' a ver",
    "Que te quiero cobrar los beso' que debes",
    "Si vos ya sabés que me re podés",
    "Que yo soy tu gatito y vos sos mi bebé",

    "Yo soy tu gatita, miau, kitty, ¡uy!",
    "Dulcecita como un daiquiri",
    "Quiero que fumemo' y quedemo' chillin'",
    "Solo con vos se me prende el feelin'",

    "Arranca el toque, sé que te re da",
    "Nos conocemo' de menor de edad",
    "Besos que viene', besos que van",
    "Guachito rico, no tenga' piedad, ay",

    "Qué bien se te ve, aeh, aeh",
    "Pegada a la pared, aeh, aeh",
    "Si te vuelvo a ver, aeh, aeh",
    "Te vuelvo a romper",

    "Que bien se me ve, aeh, aeh",
    "Me pongo al revé', aeh, aeh",
    "Si te vuelvo a ver, aeh, aeh",
    "Te vuelvo a romper",

    "Pa' que te acuerdes que yo no te olvidé, volvámono' a ver",
    "Que te quiero cobrar los beso' que debes",
    "Si vos ya sabés que me re podés",
    "Vos sos mi gatito y yo soy tu bebé",

    "Esto ya estaba escrito, ya sabes pa' qué te cito",
    "Pa' comernos, para verno', que te necesito",
    "El único problema es que si te como, repito",
    "Mmm, qué rico bizcochito",

    "Qué bien se te ve, aeh, aeh",
    "Pegada a la pared, aeh, aeh",
    "Si te vuelvo a ver, aeh, aeh",
    "Te vuelvo a romper",

    "Pa' que te acuerdes que yo no te olvidé, volvámono' a ver",
    "Que te quiero cobrar los beso' que debes",
    "Si vos ya sabés que me re podés",
    "Que yo soy tu gatito y vos sos mi bebé",

    "This is the Big One, baby",
    "Qué junte, mi amor",
    "¿Te gustó un poquito o te gustó mucho?",

    "No soy tan mala como parece",
    "Cada quien tiene lo que merece",
    "Te estuve llorando un par de vece'",
    "Desde que no estás",

    "Ma, yo sigo esperando que regrese'",
    "Mientras tu fantasma se aparece",
    "To' los días son un martes 13",
    "Desde que no estás"
]

# Índice para recorrer las frases
indice = 0

# Función para avanzar a la siguiente frase
def siguiente_frase():
    global indice
    if indice < len(frases) - 1:
        indice += 1
        etiqueta_frase.config(text=frases[indice])
    else:
        # Mostrar mensaje al finalizar las frases
        messagebox.showinfo(
            "Final",
            "Tiagon PZK, Feid, BM, La Joaqui - Pa' Que Te Acuerdes (Remix)\n\nBy Chigne"
        )
        indice = 0  # Reinicia el índice al inicio
        etiqueta_frase.config(text=frases[indice])

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Frases de la Canción")
ventana.geometry("400x200")

# Etiqueta para mostrar las frases
etiqueta_frase = tk.Label(ventana, text=frases[indice], font=("Arial", 14), wraplength=400)
etiqueta_frase.pack(pady=60)

# Botón para avanzar a la siguiente frase
boton_ok = tk.Button(ventana, text="OK", command=siguiente_frase, font=("Arial", 14))
boton_ok.pack()

# Ejecutar la ventana
ventana.mainloop()
