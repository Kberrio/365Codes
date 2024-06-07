const axios = require('axios');

// Function to fetch a random champion fact
async function getRandomChampionFact() {
  try {
    // Make a GET request to the Data Dragon API to get the list of champions
    const championsResponse = await axios.get(
      'https://ddragon.leagueoflegends.com/cdn/11.20.1/data/en_US/champion.json'
    );

    // Extract the list of champions from the response
    const champions = Object.values(championsResponse.data.data);

    // Select a random champion from the list
    const randomChampion = champions[Math.floor(Math.random() * champions.length)];

    // Get a random fact about the selected champion
    const randomFact = getRandomFact(randomChampion);

    return randomFact;
  } catch (error) {
    console.error('Error fetching random champion fact:', error);
    throw error;
  }
}

// Function to get a random fact about a champion
function getRandomFact(champion) {
  const facts = champion.blurb.split('. '); // Split the blurb into sentences
  const randomIndex = Math.floor(Math.random() * facts.length);
  return facts[randomIndex];
}

// Fetch and display a random champion fact
getRandomChampionFact()
  .then((fact) => {
    console.log('Random Champion Fact:');
    console.log(fact);
  })
  .catch((error) => {
    console.error('Error:', error);
  });
