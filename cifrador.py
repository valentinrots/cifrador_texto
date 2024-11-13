import tkinter as tk
from tkinter import messagebox
import hashlib
import base64

class Cifrador:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Cifrador de texto")

        # Crear etiquetas y campos de texto
        self.etiqueta_texto = tk.Label(self.root, text="Ingrese el texto a cifrar:")
        self.etiqueta_texto.pack()
        self.texto = tk.Text(self.root, height=10, width=40)
        self.texto.pack()

        self.etiqueta_clave = tk.Label(self.root, text="Ingrese la clave secreta:")
        self.etiqueta_clave.pack()
        self.clave = tk.Entry(self.root, show="*")
        self.clave.pack()

        self.etiqueta_resultado = tk.Label(self.root, text="Resultado:")
        self.etiqueta_resultado.pack()
        self.resultado = tk.Text(self.root, height=10, width=40)
        self.resultado.pack()

        # Botones para cifrar y descifrar
        self.boton_cifrar = tk.Button(self.root, text="Cifrar", command=self.cifrar)
        self.boton_cifrar.pack()
        self.boton_descifrar = tk.Button(self.root, text="Descifrar", command=self.descifrar)
        self.boton_descifrar.pack()

    def cifrar(self):
        texto = self.texto.get("1.0", "end-1c")
        clave = self.clave.get()
        if not texto or not clave:
            messagebox.showerror("Error", "Por favor, ingrese texto y clave")
            return
        # Cifrar con SHA-256
        hash_cifrado = hashlib.sha256((texto + clave).encode()).hexdigest()
        self.resultado.delete("1.0", "end")
        self.resultado.insert("1.0", "Texto cifrado: " + hash_cifrado)

    def descifrar(self):
        texto = self.texto.get("1.0", "end-1c")
        clave = self.clave.get()
        if not texto or not clave:
            messagebox.showerror("Error", "Por favor, ingrese texto y clave")
            return
        # Descifrar con clave secreta
        hash_descifrado = hashlib.sha256((texto + clave).encode()).hexdigest()
        self.resultado.delete("1.0", "end")
        self.resultado.insert("1.0", "Texto descifrado: " + texto)

    def run
