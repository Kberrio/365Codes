const axios = require('axios');

async function getRandomData() {
  try {
    const response = await axios.get('https://api.example.com/random');
    return response.data; // Assuming the API returns JSON data
  } catch (error) {
    console.error('Error fetching random data:', error);
    return null;
  }
}

async function main() {
  try {
    const randomData = await getRandomData();
    if (randomData) {
      console.log('Random data:', randomData);
    } else {
      console.log('Failed to fetch random data.');
    }
  } catch (error) {
    console.error('Error in main function:', error);
  }
}

main();
