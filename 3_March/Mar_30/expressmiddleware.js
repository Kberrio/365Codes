// Import the express module
const express = require('express');
const bodyParser = require('body-parser'); // Import body-parser module

// Create an Express application
const app = express();

// Middleware to parse JSON bodies
app.use(express.json());

// Define a route for the root URL ("/")
app.get('/', (req, res) => {
    res.send('Welcome to the homepage!');
});

// Define a route for the "/user" URL with a dynamic segment for userID
app.get('/user/:userID', (req, res) => {
    const userID = req.params.userID;
    res.send(`Welcome to the profile of user ${userID}`);
});

// Define a route to demonstrate handling POST requests at "/login"
app.post('/login', (req, res) => {
    const username = req.body.username;
    const password = req.body.password;
    
    // In a real application, you'd check these credentials against a database
    if(username === 'admin' && password === 'password') {
        res.send('Login successful!');
    } else {
        res.status(401).send('Login failed: Invalid username or password.');
    }
});

// Catch-all route for any other requests (404 Not Found)
app.use((req, res) => {
    res.status(404).send('Page not found!');
});

// Start the server on port 3000
app.listen(3000, () => {
    console.log('Server running on http://localhost:3000');
});
