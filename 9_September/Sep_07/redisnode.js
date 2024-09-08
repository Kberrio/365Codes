const redis = require('redis');

// Create a Redis client
const client = redis.createClient({
  host: 'localhost',
  port: 6379
});

// Connect to Redis
client.connect()
  .then(() => {
    console.log('Connected to Redis');

    // Set a key-value pair
    return client.set('myKey', 'Hello, Redis!');
  })
  .then(() => {
    console.log('Value set successfully');

    // Get the value for the key
    return client.get('myKey');
  })
  .then((value) => {
    console.log('Retrieved value:', value);

    // Close the connection
    return client.quit();
  })
  .then(() => {
    console.log('Redis connection closed');
  })
  .catch((err) => {
    console.error('Error:', err);
  });