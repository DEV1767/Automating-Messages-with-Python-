from twilio.rest import Client
from datetime import datetime, timedelta
import time


accountsid = '#YOUR-CODE'
authtoken = '#YOUR-TOKEN'

client = Client(accountsid, authtoken)

def send_message(reciver_number, message_s):
    try:
        message = client.messages.create(
            from_='whatsapp:+YOUR NUMBER FROM TWILIO',  
            body=message_s,
            to=f'whatsapp:{reciver_number}'
        )
        print("Message sent!!")
    except Exception as e:
        print(f'Error: {e}')  

name = input('Enter the name of the person you want to send the message to: ')
reciver_number = input("Enter the WhatsApp number of the recipient (include country code): ")
message_s = input(f'Enter the message you want to send to {name}: ')


date_str = input("Enter the date you want to send the message (YYYY-MM-DD): ")
time_str = input("Enter the time you want to send the message (HH:MM in 24-hour format): ")


try:
    schedule_date = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
    current_time = datetime.now()
    delay = (schedule_date - current_time).total_seconds()

    if delay <= 0:
        print("Time has already passed. Please enter a valid future time.")
    else:
        print(f'Message will be sent to {name} at {schedule_date}.')
        time.sleep(delay)
        send_message(reciver_number, message_s)
except ValueError as ve:
    print("Invalid date/time format. Please follow the correct format (YYYY-MM-DD and HH:MM).")
