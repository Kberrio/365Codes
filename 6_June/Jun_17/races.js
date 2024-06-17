const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());

let races = [];

// Helper function to simulate race and determine the winner
const simulateRace = (participants) => {
  const results = participants.map(participant => ({
    name: participant,
    time: Math.random() * 100, // Random time between 0 and 100 seconds
  }));

  results.sort((a, b) => a.time - b.time); // Sort by time (ascending)
  return results;
};

// Endpoint to start a race
app.post('/start-race', (req, res) => {
  const { raceName, participants } = req.body;

  if (!raceName || !participants || participants.length < 2) {
    return res.status(400).json({ error: 'Invalid race details' });
  }

  const race = {
    id: races.length + 1,
    raceName,
    participants,
    results: simulateRace(participants),
  };

  races.push(race);
  res.status(201).json({ message: 'Race started', raceId: race.id });
});

// Endpoint to get race status
app.get('/race-status/:id', (req, res) => {
  const raceId = parseInt(req.params.id);
  const race = races.find(r => r.id === raceId);

  if (!race) {
    return res.status(404).json({ error: 'Race not found' });
  }

  res.json(race);
});

// Endpoint to get all races
app.get('/races', (req, res) => {
  res.json(races);
});

app.listen(port, () => {
  console.log(`Race API is running on http://localhost:${port}`);
});
