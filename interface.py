import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def selecionar_arquivo():
    # Abre a janela para selecionar o arquivo
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

# Criação da janela principal
root = tk.Tk()
root.title("Upload de Arquivo com Tkinter")
root.geometry("400x200")

# Botão para selecionar o arquivo
btn_upload = tk.Button(root, text="Selecionar Arquivo", command=selecionar_arquivo)
btn_upload.pack(pady=20)

# Label para exibir o caminho do arquivo selecionado
label_arquivo = tk.Label(root, text="Nenhum arquivo selecionado")
label_arquivo.pack(pady=10)

# Inicia o loop da interface gráfica
root.mainloop()
