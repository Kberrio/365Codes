const axios = require('axios');

// Function to fetch Fortnite player stats
async function getPlayerStats(playerName) {
    try {
        const response = await axios.get(`https://api.fortnitetracker.com/v1/profile/pc/${playerName}`, {
            headers: {
                'TRN-Api-Key': 'YOUR_API_KEY' // Replace 'YOUR_API_KEY' with your actual Fortnite API key
            }
        });
        return response.data;
    } catch (error) {
        console.error('Error fetching player stats:', error.response.data);
        return null;
    }
}

// Example usage
const playerName = 'Ninja'; // Replace with the player name you want to search for
getPlayerStats(playerName)
    .then(data => {
        if (data) {
            console.log(`Stats for ${playerName}:`);
            console.log('Solo Wins:', data.stats.p2.top1.value);
            console.log('Duo Wins:', data.stats.p10.top1.value);
            console.log('Squad Wins:', data.stats.p9.top1.value);
            console.log('Total Wins:', data.lifeTimeStats.find(stat => stat.key === 'Wins').value);
        }
    });
