import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
from datetime import datetime

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_USER = 'your_email@gmail.com'
EMAIL_PASS = 'your_password'

# Create email content from data
def create_report():
    # Example of using a CSV for report
    df = pd.read_csv('report.csv')  # Replace with your data source
    report_html = df.to_html()

    # Optional: Add today's date
    today = datetime.now().strftime('%Y-%m-%d')
    
    # Email message
    email_content = f"""
    <html>
    <body>
        <h2>Daily Report - {today}</h2>
        {report_html}
    </body>
    </html>
    """
    return email_content

def send_email(subject, body):
    try:
        # Set up the MIME message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_USER
        msg['To'] = 'recipient@example.com'  # Add recipient's email address
        msg['Subject'] = subject
        
        # Attach the HTML body
        msg.attach(MIMEText(body, 'html'))

        # Connect to the server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Start TLS encryption
        server.login(EMAIL_USER, EMAIL_PASS)  # Login to the email server
        
        # Send the email
        server.sendmail(EMAIL_USER, msg['To'], msg.as_string())
        
        # Disconnect from the server
        server.quit()
        print(f"Email sent to {msg['To']}")

    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == "__main__":
    # Prepare the email
    subject = "Daily Report"
    email_body = create_report()

    # Send the email
    send_email(subject, email_body)
