import os 
from twilio.rest import Client

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

try:
    message = client.messages.create(
        body="Hello there! I'm from Keploy :)",
        from_='+16413324066',
        to='+91700004379'
    )
    print(1)
    print(message.sid)
    print(message.status)

except Exception as e: 
    print(e)
