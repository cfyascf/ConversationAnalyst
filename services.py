import os
from tkinter import messagebox
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ..creates a bar chart with the data..
def summary_of_conversations(df):
    if(df is None):
        messagebox.showwarning("No", "No file selected.")
        
    summary = df['Sender'].value_counts().reset_index()
    summary.columns = ['Sender', 'Total Conversations']
    summary.sort_values(by='Total Conversations', ascending=False, inplace=True)
    
    plt.figure(figsize=(8, len(summary) * 0.5)) 
    plt.table(cellText=summary.values, colLabels=summary.columns, cellLoc='center', loc='center')
    plt.axis('off')

    plt.title('Messages by Sender', fontsize=14)
    plt.show()

# ..generate excel file with the all the messages of a sender..
def sender_history(df, selected_sender):
    if(df is None):
        messagebox.showwarning("No", "No file selected.")
        
    system_path = "C:\\Users\\Yasmim da Cunha\\Documents\\Codes\\Python\\wpp\\ConversationAnalyst\\"
    file_name = f"messages_from_{selected_sender}.xlsx"
    
    if(os.path.exists(system_path + file_name)):
        os.remove(system_path + file_name)
    
    messages = df.loc[df['Sender'] == selected_sender, ['Date', 'Time', 'Message']]
    messages_df = pd.DataFrame(messages).reset_index(drop=True)

    with pd.ExcelWriter(file_name) as writer:
        pd.DataFrame([['Messages from: ' + selected_sender]]).to_excel(writer, index=False, header=False, startrow=0, startcol=0)
        messages_df.to_excel(writer, index=False, startrow=2, startcol=0)
        
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