// Import the express module
const express = require('express');

// Create an Express application
const app = express();

// Define a route for the root URL ("/")
app.get('/', (req, res) => {
    res.send('Welcome to the homepage!');
});

// Define a route for the "/user" URL
app.get('/user', (req, res) => {
    res.send('Welcome to your profile!');
});

// Catch-all route for any other requests (404 Not Found)
app.use((req, res) => {
    res.status(404).send('Page not found!');
});

// Start the server on port 3000
app.listen(3000, () => {
    console.log('Server running on http://localhost:3000');
});
