const express = require('express');
const request = require('request');
const querystring = require('querystring');

const app = express();
const port = 3000;

// Your Spotify API credentials
const clientId = 'YOUR_CLIENT_ID';
const clientSecret = 'YOUR_CLIENT_SECRET';

// Spotify API endpoints
const authUrl = 'https://accounts.spotify.com/api/token';
const apiUrl = 'https://api.spotify.com/v1/';

// Redirect URI for Spotify authorization
const redirectUri = 'http://localhost:3000/callback';

// Initialize the Express app
app.use(express.static(__dirname + '/public'))
   .use(express.urlencoded({ extended: true }));

// Route for initiating the Spotify authentication process
app.get('/login', (req, res) => {
    const queryParams = querystring.stringify({
        response_type: 'code',
        client_id: clientId,
        scope: 'user-read-private user-read-email', // Add scopes as needed
        redirect_uri: redirectUri
    });
    
    const authUrlWithParams = `https://accounts.spotify.com/authorize?${queryParams}`;
    res.redirect(authUrlWithParams);
});

// Route for handling the Spotify callback
app.get('/callback', (req, res) => {
    const code = req.query.code;

    // Exchange the code for an access token
    const authOptions = {
        url: authUrl,
        form: {
            code: code,
            redirect_uri: redirectUri,
            grant_type: 'authorization_code'
        },
        headers: {
            'Authorization': 'Basic ' + (new Buffer.from(clientId + ':' + clientSecret).toString('base64'))
        },
        json: true
    };

    request.post(authOptions, (error, response, body) => {
        if (!error && response.statusCode === 200) {
            const accessToken = body.access_token;
            const refreshToken = body.refresh_token;

            // Use the access token to make Spotify API requests
            const apiOptions = {
                url: apiUrl + 'me',
                headers: {
                    'Authorization': 'Bearer ' + accessToken
                },
                json: true
            };

            request.get(apiOptions, (error, response, user) => {
                // Now 'user' contains the user's information
                res.send(`Welcome, ${user.display_name}!`);
            });
        } else {
            res.send('Error: Unable to authenticate with Spotify.');
        }
    });
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
