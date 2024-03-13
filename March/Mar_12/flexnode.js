// Import the Twilio module
const twilio = require('twilio');

// Your Twilio Account SID and Auth Token
const accountSid = 'your_account_sid';
const authToken = 'your_auth_token';

// Create a Twilio client
const client = new twilio(accountSid, authToken);

// Function to send an SMS message using Twilio Flex API
function sendSMS(to, message) {
    client.messages
        .create({
            body: message,
            from: 'your_twilio_phone_number', // This should be a Twilio phone number that you own
            to: to
        })
        .then(message => console.log(`Message sent successfully. SID: ${message.sid}`))
        .catch(error => console.error(`Error sending message: ${error.message}`));
}

// Example usage
sendSMS('+1234567890', 'Hello from Twilio Flex!');
