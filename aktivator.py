from smsactivateru import Sms, SmsTypes, SmsService, GetNumber, SetStatus, GetStatus



class SMSActivator:
    def __init__(self):
        self.wrapper = Sms('2871c8cd32A105A39f0cd98A361A5239')
        self.activation = None

    def get_number(self):
        self.activation = GetNumber(
            service=SmsService().AnyOther,
            country=SmsTypes.Country.RU,
        ).request(self.wrapper)

        SetStatus(
            id=self.activation.id,
            status=SmsTypes.Status.SmsSent,
        ).request(self.wrapper)

        return str(self.activation.phone_number)

    def wait_sms(self):
        while True:
            response = GetStatus(id=self.activation.id).request(self.wrapper)
            if response['code']:
                return response['code']
