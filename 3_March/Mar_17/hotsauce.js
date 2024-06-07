// Import necessary modules
const readline = require('readline');
const fs = require('fs');

// Create interface for user input
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Define file path for storing hot sauce data
const filePath = 'hot_sauces.json';

// Function to load hot sauce data from file
function loadHotSauces() {
  try {
    const data = fs.readFileSync(filePath, 'utf8');
    return JSON.parse(data);
  } catch (err) {
    return [];
  }
}

// Function to save hot sauce data to file
function saveHotSauces(hotSauces) {
  const data = JSON.stringify(hotSauces, null, 2);
  fs.writeFileSync(filePath, data);
}

// Function to add a new hot sauce
function addHotSauce() {
  rl.question('Enter the name of the hot sauce: ', (name) => {
    rl.question('Enter the heat level (mild, medium, hot, extra hot): ', (heatLevel) => {
      const hotSauce = { name, heatLevel };
      const hotSauces = loadHotSauces();
      hotSauces.push(hotSauce);
      saveHotSauces(hotSauces);
      console.log('Hot sauce added successfully!');
      rl.close();
    });
  });
}

// Function to list all hot sauces
function listHotSauces() {
  const hotSauces = loadHotSauces();
  if (hotSauces.length === 0) {
    console.log('No hot sauces found.');
  } else {
    console.log('Hot Sauces:');
    hotSauces.forEach((hotSauce, index) => {
      console.log(`${index + 1}. ${hotSauce.name} - Heat Level: ${hotSauce.heatLevel}`);
    });
  }
  rl.close();
}

// Main function to display menu options
function main() {
  console.log('Welcome to the Hot Sauce Management System!');
  console.log('1. Add a new hot sauce');
  console.log('2. List all hot sauces');
  console.log('3. Exit');
  rl.question('Please select an option: ', (option) => {
    switch (option) {
      case '1':
        addHotSauce();
        break;
      case '2':
        listHotSauces();
        break;
      case '3':
        console.log('Exiting...');
        rl.close();
        break;
      default:
        console.log('Invalid option. Please try again.');
        main();
    }
  });
}

// Run the main function
main();
