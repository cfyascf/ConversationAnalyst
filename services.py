import os
from tkinter import messagebox
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import load_workbook

def summary_of_conversations(df):
    if(df is None):
        messagebox.showwarning("No", "No file selected.")
        
    print(df.head(5))
        
    summary = df['Sender'].value_counts().reset_index()
    summary.columns = ['Sender', 'Total Conversations']
    
    if summary.empty:
        messagebox.showwarning("Warning", "No conversations found.")
        return
    
    summary.sort_values(by='Total Conversations', ascending=False, inplace=True)
    
    plt.figure(figsize=(8, len(summary) * 0.5)) 
    plt.table(cellText=summary.values, colLabels=summary.columns, cellLoc='center', loc='center')
    plt.axis('off')

    plt.title('Messages by Sender', fontsize=14)
    plt.show()

def sender_history(df, selected_sender):
    if df is None:
        messagebox.showwarning("No", "No file selected.")
        return
    
    system_path = "C:\\Users\\Yasmim da Cunha\\Documents\\Codes\\Python\\wpp\\ConversationAnalyst\\"
    file_name = f"messages_from_{selected_sender}.xlsx"
    
    if os.path.exists(system_path + file_name):
        os.remove(system_path + file_name)
    
    messages = df.loc[df['Sender'] == selected_sender, ['Date', 'Time', 'Message']]
    messages_df = pd.DataFrame(messages).reset_index(drop=True)

    full_file_path = system_path + file_name
    
    with pd.ExcelWriter(full_file_path, engine='openpyxl') as writer:
        pd.DataFrame([['Messages from: ' + selected_sender]]).to_excel(writer, index=False, header=False, startrow=0, startcol=0)
        messages_df.to_excel(writer, index=False, startrow=2, startcol=0)
    
    wb = load_workbook(full_file_path)
    ws = wb.active

    for column_cells in ws.columns:
        max_length = 0
        column = column_cells[0].column_letter 
        for cell in column_cells:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        adjusted_width = (max_length + 2)
        ws.column_dimensions[column].width = adjusted_width

    wb.save(full_file_path)
        
def sender_history_histogram(df):
    if(df is None):
        messagebox.showwarning("No", "No file selected.")
        
    grouped = df.groupby(['Date', 'Sender']).size().reset_index(name='Count')

    plt.figure(figsize=(12, 6))

    for sender in grouped['Sender'].unique():
        sender_data = grouped[grouped['Sender'] == sender]
        plt.bar(sender_data['Date'], sender_data['Count'], width=0.4, label=sender)

    plt.xlabel('Date')
    plt.ylabel('Number of Messages')
    plt.title('Number of Conversations per Day by Sender')
    plt.xticks(rotation=45)
    plt.legend(title='Sender')
    plt.tight_layout()
    plt.show()
    
def sender_percentage_pizzachart(df):
    if(df is None):
        messagebox.showwarning("No", "No file selected.")
        
    message_counts = df['Sender'].value_counts().reset_index()
    message_counts.columns = ['Sender', 'Count']

    total_messages = message_counts['Count'].sum()
    message_counts['Percentage'] = (message_counts['Count'] / total_messages) * 100

    colors = plt.cm.tab10(np.linspace(0, 1, len(message_counts)))

    plt.figure(figsize=(8, 8))
    plt.pie(message_counts['Count'], labels=message_counts['Sender'], autopct='%1.1f%%', startangle=90, colors=colors)
    plt.title('Percentage of Messages by Sender')
    plt.axis('equal') 
    plt.tight_layout()
    plt.show()
    
def message_count_linechart(df):
    if(df is None):
        messagebox.showwarning("No", "No file selected.")
        
    message_counts = df.groupby(['Date', 'Sender']).size().unstack(fill_value=0)

    plt.figure(figsize=(12, 6))
    colors = plt.cm.tab10(np.linspace(0, 1, message_counts.shape[1]))

    for i, sender in enumerate(message_counts.columns):
        plt.plot(message_counts.index, message_counts[sender], marker='o', label=sender, color=colors[i])

    plt.title('Message Count by Time and Sender')
    plt.xlabel('Date')
    plt.ylabel('Message Count')
    plt.xticks(rotation=45)
    plt.legend(title='Sender')
    plt.grid()
    plt.tight_layout()
    plt.show()