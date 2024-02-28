const axios = require('axios');

async function getRandomUserData() {
  try {
    const response = await axios.get('https://randomuser.me/api/');
    return response.data.results[0]; // Assuming the API returns results as an array
  } catch (error) {
    console.error('Error fetching random user data:', error);
    return null;
  }
}

async function main() {
  try {
    const randomUserData = await getRandomUserData();
    if (randomUserData) {
      console.log('Random user data:', randomUserData);
    } else {
      console.log('Failed to fetch random user data.');
    }
  } catch (error) {
    console.error('Error in main function:', error);
  }
}

main();
