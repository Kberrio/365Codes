from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from reportlab.pdfgen import canvas
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SAMPLE_SPREADSHEET_ID = 'your_spreadsheet_id'
SAMPLE_RANGE_NAME = 'Sheet1!A1:E10'

creds = Credentials.from_authorized_user_file('token.json', SCOPES)
service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME).execute()
values = result.get('values', [])

pdf = canvas.Canvas("invoice.pdf")
y = 800
for row in values:
    pdf.drawString(100, y, ' '.join(row))
    y -= 20
pdf.save()

msg = MIMEMultipart()
msg['From'] = "your_email@example.com"
msg['To'] = "client_email@example.com"
msg['Subject'] = "Invoice"

body = "Please find the attached invoice."
msg.attach(MIMEText(body, 'plain'))

with open("invoice.pdf", "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

encoders.encode_base64(part)
part.add_header("Content-Disposition", f"attachment; filename= invoice.pdf")
msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("your_email@example.com", "your_password")
server.send_message(msg)
server.quit()