import tkinter as tk
from tkinter import messagebox

def upload_file():
    messagebox.showinfo("Opção 1", "Você escolheu a opção 1!")
    
def select_file():
    arquivo = filedialog.askopenfilename(
        title="Selecione um arquivo",
        filetypes=(("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*"))
    )
    
    if arquivo:
        label_arquivo.config(text=f"Arquivo selecionado: {arquivo}")
        # Aqui você pode processar o arquivo (ex: abrir e ler o conteúdo)
        with open(arquivo, 'r') as f:
            conteudo = f.read()
            print(conteudo)  # Apenas para exemplo

    else:
        messagebox.showwarning("Nenhum arquivo", "Você não selecionou nenhum arquivo.")

def conversation_summary():
    messagebox.showinfo("Opção 2", "Você escolheu a opção 2!")
    
def sender_history():
    raise NotImplementedError()

def sender_history_histogram():
    messagebox.showinfo("Opção 3", "Você escolheu a opção 3!")
    
def sender_history_pizzachart():
    messagebox.showinfo("Opção 3", "Você escolheu a opção 3!")

def sender_history_linechart():
    messagebox.showinfo("Opção 3", "Você escolheu a opção 3!")

def quit():
    root.destroy()

root = tk.Tk()
root.title("Menu de Opções")
root.geometry("300x300")  # Tamanho da janela

# Título do Menu
titulo = tk.Label(root, text="Escolha uma opção", font=("Arial", 16))
titulo.pack(pady=20)

# Botão para a Opção 1
btn_upload_file = tk.Button(root, text="Upload file", font=("Arial", 14), command=upload_file)
btn_upload_file.pack(pady=10)

btn_summary = tk.Button(root, text="Conversation Summary", font=("Arial", 14), command=conversation_summary)
btn_summary.pack(pady=10)

btn_history = tk.Button(root, text="Sender History", font=("Arial", 14), command=sender_history)
btn_history.pack(pady=10)

# Botão para a Opção 2
btn_histogram = tk.Button(root, text="Sender History Histogram", font=("Arial", 14), command=sender_history_histogram)
btn_histogram.pack(pady=10)

# Botão para a Opção 3
btn_pizzachart = tk.Button(root, text="Sender Percentage Pizza Chart", font=("Arial", 14), command=sender_history_pizzachart)
btn_pizzachart.pack(pady=10)

btn_linechart = tk.Button(root, text="Message Counter Line Chart", font=("Arial", 14), command=sender_history_linechart)
btn_linechart.pack(pady=10)

# Botão para quit
btn_quit = tk.Button(root, text="Quit", font=("Arial", 14), command=quit)
btn_quit.pack(pady=10)

# Inicia o loop da interface gráfica
root.mainloop()
