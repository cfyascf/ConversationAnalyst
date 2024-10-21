import pandas as pd
import matplotlib.pyplot as plt

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