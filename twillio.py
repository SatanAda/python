import datetime
import os

from dotenv import load_dotenv
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
from sociallinks.tests.registration.test_registration import test_registration


class SmsFromTwillio:
    def __init__(self, dotenv=load_dotenv()):
        self.account_sid = os.environ['TWILIO_ACCOUNT_SID']
        self.auth_token = os.environ['TWILIO_AUTH_TOKEN']
        self.client = Client(self.account_sid, self.auth_token)

    def read_sms(self, message_sent_after, data_sent=datetime.datetime.now(), ):
        messages = self.client.messages.list(
            to=os.environ['phone'],
            limit=1
        )
        for record in messages:
            if message_sent_after(test_registration) > data_sent:
                continue
        else:
            return record.body
