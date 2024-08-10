require('dotenv').config();
const express = require('express');
const axios = require('axios');
const { google } = require('googleapis');

const app = express();
const port = 3000;

const oauth2Client = new google.auth.OAuth2(
  process.env.GOOGLE_CLIENT_ID,
  process.env.GOOGLE_CLIENT_SECRET,
  'http://localhost:3000/auth/google/callback'
);

app.use(express.static('public'));

app.get('/auth/google', (req, res) => {
  const url = oauth2Client.generateAuthUrl({
    access_type: 'offline',
    scope: ['https://www.googleapis.com/auth/fitness.activity.read']
  });
  res.redirect(url);
});

app.get('/auth/google/callback', async (req, res) => {
  const { code } = req.query;
  const { tokens } = await oauth2Client.getToken(code);
  oauth2Client.setCredentials(tokens);
  res.redirect('/');
});

app.get('/api/fitness-data', async (req, res) => {
  try {
    const fitness = google.fitness({ version: 'v1', auth: oauth2Client });
    const now = Date.now();
    const oneDayAgo = now - 24 * 60 * 60 * 1000;

    const response = await fitness.users.dataset.aggregate({
      userId: 'me',
      requestBody: {
        aggregateBy: [
          { dataTypeName: 'com.google.step_count.delta' },
          { dataTypeName: 'com.google.calories.expended' },
          { dataTypeName: 'com.google.active_minutes' }
        ],
        bucketByTime: { durationMillis: 86400000 },
        startTimeMillis: oneDayAgo,
        endTimeMillis: now
      }
    });

    res.json(response.data);
  } catch (error) {
    console.error('Error fetching fitness data:', error);
    res.status(500).json({ error: 'Error fetching fitness data' });
  }
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});