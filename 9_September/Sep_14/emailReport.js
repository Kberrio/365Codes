const nodemailer = require('nodemailer');
const fs = require('fs');
const cron = require('node-cron');
const path = require('path');

// Email configuration
const transporter = nodemailer.createTransport({
    service: 'gmail', // Use your email provider, e.g., 'gmail'
    auth: {
        user: 'your_email@gmail.com',  // Your email address
        pass: 'your_password'          // Your email password or app-specific password for Gmail
    }
});

// Create report from CSV (optional)
function createReport() {
    const csvFilePath = path.join(__dirname, 'report.csv'); // Path to your CSV file
    const data = fs.readFileSync(csvFilePath, 'utf8');

    // Convert CSV to HTML table (you could use a library like 'csvtojson' for complex parsing)
    const rows = data.split('\n');
    let reportHtml = `<table border="1"><tr><th>${rows[0].split(',').join('</th><th>')}</th></tr>`;

    for (let i = 1; i < rows.length; i++) {
        const columns = rows[i].split(',');
        reportHtml += `<tr><td>${columns.join('</td><td>')}</td></tr>`;
    }
    reportHtml += `</table>`;

    return reportHtml;
}

// Function to send the email
function sendEmail() {
    const today = new Date().toISOString().split('T')[0]; // Format today's date

    const mailOptions = {
        from: 'your_email@gmail.com',
        to: 'recipient@example.com',  // Recipient's email
        subject: `Daily Report - ${today}`,
        html: `
        <h2>Daily Report - ${today}</h2>
        ${createReport()}
        `
    };

    transporter.sendMail(mailOptions, (error, info) => {
        if (error) {
            console.log('Error sending email:', error);
        } else {
            console.log('Email sent:', info.response);
        }
    });
}

// Schedule the email to be sent daily at 8 AM
cron.schedule('0 8 * * *', () => {
    console.log('Sending daily email report...');
    sendEmail();
}, {
    scheduled: true,
    timezone: "America/New_York"  // Set your timezone
});

// For testing, you can run sendEmail() manually here to test without scheduling
// sendEmail();
