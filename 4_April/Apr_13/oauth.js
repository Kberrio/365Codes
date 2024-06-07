const express = require('express');
const passport = require('passport');
const OAuth2Strategy = require('passport-oauth2').Strategy;

// Replace these values with your OAuth provider's credentials
const CLIENT_ID = 'YOUR_CLIENT_ID';
const CLIENT_SECRET = 'YOUR_CLIENT_SECRET';
const CALLBACK_URL = 'http://localhost:3000/auth/callback'; // Replace with your callback URL

passport.use(new OAuth2Strategy({
    authorizationURL: 'YOUR_AUTHORIZATION_URL',
    tokenURL: 'YOUR_TOKEN_URL',
    clientID: CLIENT_ID,
    clientSecret: CLIENT_SECRET,
    callbackURL: CALLBACK_URL
  },
  function(accessToken, refreshToken, profile, cb) {
    // You can handle user data retrieval and saving here
    return cb(null, profile);
  }
));

passport.serializeUser(function(user, done) {
  done(null, user);
});

passport.deserializeUser(function(obj, done) {
  done(null, obj);
});

const app = express();

app.use(passport.initialize());
app.use(passport.session());

app.get('/auth/provider', passport.authenticate('oauth2'));

app.get('/auth/callback',
  passport.authenticate('oauth2', { failureRedirect: '/login' }),
  function(req, res) {
    // Successful authentication, redirect home.
    res.redirect('/');
  }
);

app.get('/', function(req, res) {
  res.send('You are authenticated!');
});

app.listen(3000, () => {
  console.log('Server is running on http://localhost:3000');
});
