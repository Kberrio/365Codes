import imaplib
import email
from twilio.rest import Client

EMAIL = 'your_email@example.com'
PASSWORD = 'your_email_password'
TWILIO_SID = 'your_twilio_sid'
TWILIO_TOKEN = 'your_twilio_token'
TWILIO_FROM = 'your_twilio_phone_number'
TWILIO_TO = 'recipient_phone_number'

mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(EMAIL, PASSWORD)
mail.select("inbox")

_, search_data = mail.search(None, 'UNSEEN SUBJECT "urgent"')

for num in search_data[0].split():
    _, data = mail.fetch(num, '(RFC822)')
    _, b = data[0]
    email_message = email.message_from_bytes(b)

    client = Client(TWILIO_SID, TWILIO_TOKEN)
    client.messages.create(
        body=f"Urgent email received: {email_message['subject']}",
        from_=TWILIO_FROM,
        to=TWILIO_TO
    )
