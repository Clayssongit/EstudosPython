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

# 4 - Adicionar o input text
frase_lab = tk.Label(frame, text="Frase")
frase_lab.pack(fill='x', expand=True)

frase_inp = tk.Entry(frame)
frase_inp.pack(fill='x', expand=True)

# 5 - Função para alterar o texto do label
def click():
    label.config(text=frase_inp.get())


# 6 - Adicionando botão
button = tk.Button(frame, text="Enviar", command=click)
button.pack()

window.mainloop()

"""
Para utilizar um tkinter mais bonito, utilize o customtkinter(Faça a instalação por pip).
Ele segue a mesma estrutura do tkinter que vem junto ao python, porém com visual mais moderno.
"""