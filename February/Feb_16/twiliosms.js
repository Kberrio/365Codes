const accountSid = 'YOUR_TWILIO_ACCOUNT_SID';
const authToken = 'YOUR_TWILIO_AUTH_TOKEN';
const twilioNumber = 'YOUR_TWILIO_PHONE_NUMBER';
const recipientNumber = 'RECIPIENT_PHONE_NUMBER';

const client = require('twilio')(accountSid, authToken);

client.messages
  .create({
     body: 'This is a test message from your Twilio account',
     from: twilioNumber,
     to: recipientNumber
   })
  .then(message => console.log(`Message sent with SID: ${message.sid}`))
  .catch(err => console.error(`Error: ${err.message}`));
