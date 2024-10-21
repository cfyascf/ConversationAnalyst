import re
import pandas as pd
import matplotlib.pyplot as plt
import sys
import io

# ..constants..

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
FILE = '_chat.txt'

# ..functions..

# ..creates a list with all the data from the file, 
# making each index a message..
def read_and_process_file():
    with open(FILE, 'r', encoding='utf-8') as f:
        raw_data = f.readlines()

    messages = []
    message_pattern = re.compile(r'^\[\d{2}/\d{2}/\d{4}, \d{2}:\d{2}:\d{2}\]') 
    current_message = None
    
    # ..for line in file, checks if the line is a message header, 
    # if it is, adds the line to the list, if it isn't, adds the line to 
    # the last message in list..
    for line in raw_data:
        if message_pattern.match(line):
            
            # ..takes off /n and this word that i don't know what it means..
            current_message = line.strip()
            current_message = current_message.replace("\u200e", "")
            
            if current_message:
                messages.append(current_message)
            
        else:
            if current_message:
                current_message += f"\n{line.strip()}"
    
    return messages 

# ..process the data and returns a dataframe
def process_messages(messages):
    processed_data = []
    
    for msg in messages:
        try:
            date_time, sender_message = msg.split('] ', 1)
            date_time = date_time[1:] 
            sender, message = sender_message.split(': ', 1)
            date, time = date_time.split(', ')
            
            processed_data.append([date, time, sender, message])
            
        except ValueError:
            continue
        
    df = pd.DataFrame(processed_data, columns=['Date', 'Time', 'Sender', 'Message'])
    df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
    
    return df

# ..returns a dataframe with a summary of the conversation..
def summary_of_conversations(df):
    summary = df['Sender'].value_counts().reset_index()
    summary.columns = ['Sender', 'Total Conversations']
    summary.sort_values(by='Total Conversations', ascending=False, inplace=True)
    
    return summary

# Função para filtrar histórico de mensagens por remetente
def history_of_sender(df, sender_name):
    sender_history = df[df['Sender'] == sender_name]
    return sender_history[['Date', 'Time', 'Message']]

# Função para gerar gráficos
def generate_graphs(df):
    # Gráfico de pizza: percentual de mensagens de cada remetente
    plt.figure(figsize=(8, 6))
    df['Sender'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, title='Percentual de Mensagens por Remetente')
    plt.ylabel('')
    plt.tight_layout()
    plt.show()

    # Gráfico de linhas: mensagens ao longo do tempo para cada remetente
    plt.figure(figsize=(12, 6))
    df.groupby(['Date', 'Sender']).size().unstack().plot(kind='line', marker='o')
    plt.title('Quantidade de Mensagens ao Longo do Tempo')
    plt.xlabel('Data')
    plt.ylabel('Número de Mensagens')
    plt.xticks(rotation=45)
    plt.legend(title='Remetente')
    plt.tight_layout()
    plt.show()

    # Gráfico de barras: histórico de mensagens por dia para cada remetente
    daily_counts = df.groupby(['Date', 'Sender']).size().unstack(fill_value=0)
    daily_counts.plot(kind='bar', stacked=True, figsize=(12, 6))
    plt.title('Histórico de Mensagens por Dia e Remetente')
    plt.xlabel('Data')
    plt.ylabel('Número de Mensagens')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    messages = read_and_process_file()
    df = process_messages(messages)
    print(df)
    
    # # Resumo das conversas
    summary_of_conversations(df)

    # # Exibir histórico de um remetente específico (por exemplo, "yago martins")
    # sender_name = "yago martins"
    # sender_history = history_of_sender(df, sender_name)
    # print(f"\nHistórico de Mensagens de {sender_name}:")
    # print(sender_history)

    # # Gerar os gráficos
    # generate_graphs(df)