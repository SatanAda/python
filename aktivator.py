import os
from smsactivateru import Sms, SmsTypes, SmsService, GetNumber, SetStatus, GetStatus


class SMSActivator:
    def __init__(self):
        self.wrapper = Sms (os.environ.get('sms_key'))
        self.activation = None

    def get_number(self):
        self.activation = GetNumber (
            service=SmsService ().AnyOther,
            country=SmsTypes.Country.RU,
        ).request (self.wrapper)

        SetStatus (
            id=self.activation.id,
            status=SmsTypes.Status.SmsSent,
        ).request (self.wrapper)

        return str (self.activation.phone_number)

    def wait_sms(self):
        while True:
            response = GetStatus (id=self.activation.id).request (self.wrapper)
            if response['code']:
                return response['code']
