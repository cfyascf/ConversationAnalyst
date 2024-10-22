import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk

from matplotlib import pyplot as plt
import pandas as pd
import util as util
import services as sc

FILE = None
DF = None

def create_main_window():
    global DF
    
    root = tk.Tk()
    root.title("Menu")
    root.geometry("300x300")  

    titulo = tk.Label(root, text="Choose an option", font=("Arial", 16))
    titulo.pack(pady=20)

    btn_upload_file = tk.Button(root, text="Upload file", font=("Arial", 14), command=create_file_window)
    btn_upload_file.pack(pady=10)

    btn_summary = tk.Button(root, text="Conversation Summary", font=("Arial", 14), command=lambda: sc.summary_of_conversations(DF))
    btn_summary.pack(pady=10)

    btn_history = tk.Button(root, text="Sender History", font=("Arial", 14), command=create_filter_window)
    btn_history.pack(pady=10)

    btn_histogram = tk.Button(root, text="Sender History Histogram", font=("Arial", 14), command=None)
    btn_histogram.pack(pady=10)

    btn_pizzachart = tk.Button(root, text="Sender Percentage Pizza Chart", font=("Arial", 14), command=None)
    btn_pizzachart.pack(pady=10)

    btn_linechart = tk.Button(root, text="Message Counter Line Chart", font=("Arial", 14), command=None)
    btn_linechart.pack(pady=10)

    btn_quit = tk.Button(root, text="Quit", font=("Arial", 14), command=lambda: quit(root))
    btn_quit.pack(pady=10)

    root.mainloop()

    return root

def create_file_window():
    root = tk.Toplevel()

    label = tk.Label(root, text="No file selected.", font=("Arial", 14))
    label.pack(pady=10)

    btn_upload = tk.Button(root, text="Upload", command=lambda: select_file(label), font=("Arial", 14))
    btn_upload.pack(pady=20)

    btn_cancel = tk.Button(root, text="Submit", font=("Arial", 14), command=lambda: exit(root))
    btn_cancel.pack(pady=10)

    btn_cancel = tk.Button(root, text="Quit", font=("Arial", 14), command=lambda: quit(root))
    btn_cancel.pack(pady=10)

    root.mainloop()

def create_filter_window():
    global DF
    
    root = tk.Toplevel()

    label = tk.Label(root, text="Select sender.", font=("Arial", 14))
    label.pack(pady=10)
    sender_dropdown = ttk.Combobox(root, values=DF['Sender'].unique().tolist())
    sender_dropdown.bind("<<ComboboxSelected>>", lambda event: when_sender_selected(event, sender_dropdown))
    sender_dropdown.pack(pady=10)
    
    root.mainloop()
    
def when_sender_selected(e, dropdown):
    global DF
    
    selected_sender = dropdown.get()
    messages = DF['Message'].loc[DF['Sender'] == selected_sender]
    
    messages_df = pd.DataFrame(messages).reset_index(drop=True)

    # Definir o nome do arquivo
    file_name = f"messages_from_{selected_sender}.xlsx"

    # Escrever o DataFrame em um arquivo Excel
    with pd.ExcelWriter(file_name) as writer:
        # Escrever o título na primeira linha
        pd.DataFrame([['Messages from: ' + selected_sender]]).to_excel(writer, index=False, header=False, startrow=0, startcol=0)
        # Escrever as mensagens abaixo
        messages_df.to_excel(writer, index=False, header=True, startrow=2, startcol=0)
    
    
def select_file(label):
    global FILE
    global DF

    print("selecting file")
    FILE = filedialog.askopenfilename(
        title="Select a file",
        filetypes=(("text files", "*.txt"), ("All files", "*.*"))
    )
    
    if FILE:
        label.config(text=F"File selected: {FILE}")
        DF = util.get_messages(FILE)
        print(FILE)
        print(f"aaaa, {DF}")

    else:
        messagebox.showwarning("Nenhum file", "Você não selecionou nenhum file.")

def exit(window):
    window.destroy()
    
def quit(window):
    global DF
    global FILE
    
    DF = None
    FILE = None
    window.destroy()