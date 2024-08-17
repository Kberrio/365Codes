const nodemailer = require('nodemailer');

class EmailClient {
  constructor(smtpServer, smtpPort, username, password) {
    this.transporter = nodemailer.createTransport({
      host: smtpServer,
      port: smtpPort,
      secure: smtpPort === 465, // true for 465, false for other ports
      auth: {
        user: username,
        pass: password,
      },
    });
  }

  async sendEmail(toEmail, subject, body) {
    try {
      const info = await this.transporter.sendMail({
        from: this.transporter.options.auth.user,
        to: toEmail,
        subject: subject,
        text: body,
      });
      console.log('Email sent successfully');
      console.log('Message ID:', info.messageId);
    } catch (error) {
      console.error('An error occurred:', error);
    }
  }
}

// Usage example
async function main() {
  // Replace these with your actual email server details
  const smtpServer = 'smtp.gmail.com';
  const smtpPort = 587;
  const username = 'your_email@gmail.com';
  const password = 'your_password';

  const client = new EmailClient(smtpServer, smtpPort, username, password);

  const toEmail = 'recipient@example.com';
  const subject = 'Test Email';
  const body = 'This is a test email sent from Node.js.';

  await client.sendEmail(toEmail, subject, body);
}

main().catch(console.error);