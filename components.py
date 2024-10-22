import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

def big_label(window, text):
    label = tk.Label(
        window, 
        text=text, 
        font=("Arial", 16),
        wraplength=300
    )
    label.pack(pady=20)
    
    return label
    
def small_label(window, text):
    label = tk.Label(
        window, 
        text=text, 
        font=("Arial", 12),
        wraplength=300
    )
    label.pack(pady=20)
    
    return label
    
def button(window, text, command, side='top'):
    button = tk.Button(window, text=text, font=("Arial", 12, "bold"), command=command)
    button.pack(pady=10, padx=5, side=side)
    
    return button
    
def frame(window):
    frame = tk.Frame(window)
    frame.pack(fill="both", expand=True, padx=10, pady=10)
    
    return frame

def dialog(text):
    dialog = filedialog.askopenfilename(
        title=text,
        filetypes=(("text files", "*.txt"), ("All files", "*.*"))
    )
    
    return dialog

def dropdown(window, values):
    dropdown = ttk.Combobox(
        window, 
        values
    )
    dropdown.pack(pady=10)
    
    return dropdown