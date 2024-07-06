import tkinter as tk

class AddizioneApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calcolatrice di Addizione")
        self.root.geometry("300x200")

        # Creazione dei campi di input
        self.label1 = tk.Label(root, text="Numero 1:")
        self.label1.pack(pady=5)

        self.entry1 = tk.Entry(root)
        self.entry1.pack(pady=5)

        self.label2 = tk.Label(root, text="Numero 2:")
        self.label2.pack(pady=5)

        self.entry2 = tk.Entry(root)
        self.entry2.pack(pady=5)

        # Creazione del pulsante
        self.button = tk.Button(root, text="Calcola", command=self.add_numbers)
        self.button.pack(pady=10)

        # Creazione dell'etichetta per mostrare il risultato
        self.label_result = tk.Label(root, text="Risultato:")
        self.label_result.pack(pady=20)

    def add_numbers(self):
        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
            result = num1 + num2
            self.label_result.config(text=f"Risultato: {result}")
        except ValueError:
            self.label_result.config(text="Errore: Inserisci numeri validi")

# Creazione della finestra principale
root = tk.Tk()
app = AddizioneApp(root)

# Avvio del loop principale dell'applicazione
root.mainloop()




