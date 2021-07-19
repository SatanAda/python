import email
import imaplib

import bs4 as bs4


class imap:

    def __init__(self):
        self.mail = imaplib.IMAP4_SSL('imap.gmail.com')

    def auth(self):
        self.mail.login('mail', 'password')
        self.mail.list()
        self.mail.select("inbox")

        result, data = self.mail.search(None, "ALL")

        ids = data[0]
        id_list = ids.split()
        latest_email_id = id_list[-1]

        result, data = self.mail.fetch(latest_email_id, "(RFC822)")
        raw_email = data[0][1]
        raw_email_string = raw_email.decode('utf-8')
        print(raw_email_string)

        email_message = email.message_from_string(raw_email_string)

        if email_message.is_multipart():
            for payload in email_message.get_payload():
                body = payload.get_payload(decode=True).decode('utf-8')
                print(body)
        else:
            body = email_message.get_payload(decode=True).decode('utf-8')
            print(body)

        soup = bs4.BeautifulSoup(body, 'html.parser')
        link = soup.find('a', text='Verify email')['href']
        return link

