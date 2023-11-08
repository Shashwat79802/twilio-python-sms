# twilio-python-sms

Create a virtual environment using - ```python3 -m virtualenv venv```. <br>

Activate it- <br>1. Linux/MacOS: ```source venv/bin/activate``` <br>
                  2. Windows: ```source venv/scripts/activate```

Install the requirements - ```pip3 install -r requriements.txt```

Create your account and get the Account SID, Auth Token and Purchase a phone number from [Twilio](https://console.twilio.com) and then update the `.env` file with the credentials.

Finally, run the application using command - ```uvicorn main:app --reload```

And make a post request to the url - `http://127.0.0.1:8000/send-sms/` and send the following json: <br>
```
{
    "Body": "Test Test Tessstttt :)",
    "To": "YOUR_PHONE_NUMBER"
}
```
Replace the YOUR_PHONE_NUMBER placeholder above.
