import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from matplotlib import pyplot as plt
import components as ui
import pandas as pd
import util as util
import services as sc

FILE = None
DF = None

def create_main_window():
    global DF
    
    root = tk.Tk()
    root.configure(padx=20, pady=20)
    root.title("Menu")

    ui.big_label(root, "Welcome to the Conversation Analyst!")
    ui.small_label(root, "Upload a conversation file to generate free analisys!")

    ui.button(root, "Upload file", create_file_window)
    ui.button(root, "Conversation Summary", lambda: sc.summary_of_conversations(DF))
    ui.button(root, "Sender History", create_filter_window)
    ui.button(root, "Sender History Histogram", lambda: sc.sender_history_histogram(DF))
    ui.button(root, "Sender Percentage Pizza Chart", lambda: sc.sender_percentage_pizzachart(DF))
    ui.button(root, "Message Counter Line Chart", lambda: sc.message_count_linechart(DF))
    ui.button(root, "Quit", lambda: quit(root))
    
    root.mainloop()

    return root

def create_file_window():
    root = tk.Toplevel()
    root.configure(padx=20, pady=20)

    label = ui.small_label(root, "No file selected.")
    ui.button(root, "Upload", lambda: select_file(label))
    
    btn_frame = ui.frame(root)
    ui.button(btn_frame, "Submit", lambda: exit(root), side='right')
    ui.button(btn_frame, "Quit", lambda: quit(root), side='left')

    root.mainloop()
    
def select_file(label):
    global FILE
    global DF

    FILE = ui.dialog("Select file")
    
    if FILE:
        label.config(
            text=F"File selected: {FILE}",
        )
        DF = util.get_messages(FILE)

    else:
        messagebox.showwarning("No file", "No file selected.")

def create_filter_window():
    global DF
    
    root = tk.Toplevel()
    root.configure(padx=20, pady=20)

    ui.small_label(root, "Select sender to generate an excel file with their message data.")
    dropdown = ui.dropdown(root, DF['Sender'].unique().tolist())
    ui.button(root, "Submit", lambda: when_sender_selected(dropdown))
    
    root.mainloop()
  
def when_sender_selected(dropdown):
    global DF
    
    selected_sender = dropdown.get()
    sc.sender_history(DF, selected_sender)
        
    messagebox.showinfo("Success", "Excel with message data generated successfully!")  

def exit(window):
    window.destroy()
    
def quit(window):
    global DF
    global FILE
    
    DF = None
    FILE = None
    window.destroy()