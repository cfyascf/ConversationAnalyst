import tkinter as tk
from tkinter import messagebox

def create_main_window():
    root = tk.Tk()
    root.title("Menu de Opções")
    root.geometry("300x300")  

    titulo = tk.Label(root, text="Escolha uma opção", font=("Arial", 16))
    titulo.pack(pady=20)

    btn_upload_file = tk.Button(root, text="Upload file", font=("Arial", 14), command=create_file_window)
    btn_upload_file.pack(pady=10)

    btn_summary = tk.Button(root, text="Conversation Summary", font=("Arial", 14), command=conversation_summary)
    btn_summary.pack(pady=10)

    btn_history = tk.Button(root, text="Sender History", font=("Arial", 14), command=sender_history)
    btn_history.pack(pady=10)

    btn_histogram = tk.Button(root, text="Sender History Histogram", font=("Arial", 14), command=sender_history_histogram)
    btn_histogram.pack(pady=10)

    btn_pizzachart = tk.Button(root, text="Sender Percentage Pizza Chart", font=("Arial", 14), command=sender_history_pizzachart)
    btn_pizzachart.pack(pady=10)

    btn_linechart = tk.Button(root, text="Message Counter Line Chart", font=("Arial", 14), command=sender_history_linechart)
    btn_linechart.pack(pady=10)

    btn_quit = tk.Button(root, text="Quit", font=("Arial", 14), command=quit)
    btn_quit.pack(pady=10)

    root.mainloop()

    return root

def create_file_window():
    root = tk.Tk()

    btn_upload = tk.Button(root, text="Upload", command=upload_file)
    btn_upload.pack(pady=20)

    label_arquivo = tk.Label(root, text="No file selected.")
    label_arquivo.pack(pady=10)

    btn_cancel = tk.Button(root, text="Cancel", font=("Arial", 14))
    btn_cancel.pack(pady=10)

    btn_submit = tk.Button(root, text="Submit", font=("Arial", 14))
    btn_submit.pack(pady=10)

    root.mainloop()

    return root

def upload_file():
    messagebox.showinfo("Opção 1", "Você escolheu a opção 1!")
    
def select_file():
    file = filedialog.askopenfilename(
        title="Select a file",
        filetypes=(("text files", "*.txt"), ("All files", "*.*"))
    )
    
    if file:
        label_file.config(text=f"Selected file: {file}")
        
        with open(file, 'r') as f:
            conteudo = f.read()
            print(conteudo)  # Apenas para exemplo

    else:
        messagebox.showwarning("Nenhum file", "Você não selecionou nenhum file.")

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


