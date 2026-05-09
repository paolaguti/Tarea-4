import tkinter as tk
from tkinter import messagebox

class Principal:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Software FJ")
        self.root.geometry("400x300")
        self.label = tk.Label(self.root, text="Bienvenido al Software FJ", font=("Arial", 16))
        self.label.pack(pady=20)
        self.button = tk.Button(self.root, text="Mostrar mensaje", command=self.mostrar_mensaje)
        self.button.pack(pady=10)
        self.root.mainloop()