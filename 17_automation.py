import schedule
import requests
import time

my_phone_number = '+569xxxxxxxx'

def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone': my_phone_number,
        'message': 'Hey. Good Morning',
        'key': 'textbelt'
    })

    print(resp.json())

# schedule.every().day.at('08:00').do(send_message)

schedule.every(10).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)