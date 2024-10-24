import io
import re
import sys
import pandas as pd

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# ..creates a list with all the data from the file, 
# making each index a message..
def read_and_process_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        raw_data = f.readlines()

    messages = []
    ios_message_pattern = re.compile(r'^\[\d{2}/\d{2}/\d{4}, \d{2}:\d{2}:\d{2}\]') 
    android_message_pattern = re.compile(r'^(\d{2}/\d{2}/\d{4}) (\d{2}:\d{2}) - ([\w\s]+): (.+)$') 
    current_message = None
    
    # ..for line in file, checks if the line is a message header, 
    # if it is, adds the line to the list, if it isn't, adds the line to 
    # the last message in list..
    for line in raw_data:
        if ios_message_pattern.match(line) or android_message_pattern.match(line):
            
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
    df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y').dt.date
    
    return df

def get_messages(file):
    messages = read_and_process_file(file)
    return process_messages(messages)