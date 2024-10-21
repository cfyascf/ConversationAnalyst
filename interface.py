import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import util as util

FILE = None
DF = None

def create_main_window():
    root = tk.Tk()
    root.title("Menu")
    root.geometry("300x300")  

    titulo = tk.Label(root, text="Choose an option", font=("Arial", 16))
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

    btn_quit = tk.Button(root, text="Quit", font=("Arial", 14), command=lambda: quit(root))
    btn_quit.pack(pady=10)

    root.mainloop()

    return root

def create_file_window():
    root = tk.Tk()

    label = tk.Label(root, text="No file selected.", font=("Arial", 14))
    label.pack(pady=10)

    btn_upload = tk.Button(root, text="Upload", command=lambda: select_file(label), font=("Arial", 14))
    btn_upload.pack(pady=20)

    btn_cancel = tk.Button(root, text="Submit", font=("Arial", 14), command=lambda: quit(root))
    btn_cancel.pack(pady=10)

    btn_cancel = tk.Button(root, text="Quit", font=("Arial", 14), command=lambda: quit(root))
    btn_cancel.pack(pady=10)

    root.mainloop()

    
def select_file(label):
    global FILE
    global DF

    FILE = filedialog.askopenfilename(
        title="Select a file",
        filetypes=(("text files", "*.txt"), ("All files", "*.*"))
    )
    
    if FILE:
        label.config(text=F"File selected: {FILE}")
        DF = util.get_messages(FILE)

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

def quit(window):
    window.destroy()