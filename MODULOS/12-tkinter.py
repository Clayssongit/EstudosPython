import tkinter as tk
 
 # 1 - Criando a janela
window = tk.Tk()
window.geometry("300x150")
window.title("Gerenciador de Frases")

# 2 - Adicionar o frame
frame = tk.Frame(window)
frame.pack(padx=10, pady=10, fill= 'x', expand= True)

# 3 - Adicionando o label
label = tk.Label(frame, text="Hello, World")
label.pack(fill='x', expand=True)

window.mainloop()