import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailClient:
    def __init__(self, smtp_server, smtp_port, username, password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, to_email, subject, body):
        # Create a multipart message
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = to_email
        msg['Subject'] = subject

        # Add body to email
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Create SMTP session
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Enable TLS
                server.login(self.username, self.password)
                
                # Send email
                server.send_message(msg)
                print("Email sent successfully")
        except Exception as e:
            print(f"An error occurred: {e}")

# Usage example
if __name__ == "__main__":
    # Replace these with your actual email server details
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    username = "your_email@gmail.com"
    password = "your_password"

    client = EmailClient(smtp_server, smtp_port, username, password)

    to_email = "recipient@example.com"
    subject = "Test Email"
    body = "This is a test email sent from Python."

    client.send_email(to_email, subject, body)