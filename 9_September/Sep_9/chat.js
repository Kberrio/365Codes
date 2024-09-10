const natural = require('natural');
const axios = require('axios');
const readline = require('readline');
const fs = require('fs').promises;

class AdvancedChatbot {
  constructor() {
    this.classifier = new natural.BayesClassifier();
    this.tokenizer = new natural.WordTokenizer();
    this.stemmer = natural.PorterStemmer;
    this.learningData = {};
    this.weatherApiKey = 'YOUR_OPENWEATHERMAP_API_KEY';
  }

  async initialize() {
    await this.loadLearningData();
    await this.trainClassifier();
    console.log("Chatbot initialized and ready!");
  }

  async loadLearningData() {
    try {
      const data = await fs.readFile('learning_data.json', 'utf8');
      this.learningData = JSON.parse(data);
    } catch (error) {
      console.log("No existing learning data found. Starting fresh.");
    }
  }

  async saveLearningData() {
    await fs.writeFile('learning_data.json', JSON.stringify(this.learningData));
  }

  async trainClassifier() {
    for (const [intent, phrases] of Object.entries(this.learningData)) {
      phrases.forEach(phrase => this.classifier.addDocument(this.processText(phrase), intent));
    }
    this.classifier.train();
  }

  processText(text) {
    return this.tokenizer.tokenize(text).map(token => this.stemmer.stem(token)).join(' ');
  }

  async classifyIntent(text) {
    const processedText = this.processText(text);
    return this.classifier.classify(processedText);
  }

  async getWeather(city) {
    try {
      const response = await axios.get(`http://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${this.weatherApiKey}&units=metric`);
      const { main, weather } = response.data;
      return `The weather in ${city} is ${weather[0].description} with a temperature of ${main.temp}°C.`;
    } catch (error) {
      return "Sorry, I couldn't fetch the weather information at the moment.";
    }
  }

  async respondTo(input) {
    const intent = await this.classifyIntent(input);

    switch (intent) {
      case 'greeting':
        return "Hello! How can I assist you today?";
      case 'farewell':
        return "Goodbye! Have a great day!";
      case 'weather':
        const city = input.match(/weather in (.+)/i)?.[1] || "London";
        return await this.getWeather(city);
      case 'learn':
        const [newIntent, ...phraseParts] = input.split(':');
        const phrase = phraseParts.join(':').trim();
        if (newIntent && phrase) {
          if (!this.learningData[newIntent]) this.learningData[newIntent] = [];
          this.learningData[newIntent].push(phrase);
          await this.saveLearningData();
          await this.trainClassifier();
          return `Thank you! I've learned that "${phrase}" is associated with the intent "${newIntent}".`;
        }
        return "I'm sorry, I couldn't understand the learning format. Please use 'learn: intent: phrase'.";
      default:
        return "I'm not sure how to respond to that. Can you try rephrasing or asking something else?";
    }
  }
}

async function main() {
  const chatbot = new AdvancedChatbot();
  await chatbot.initialize();

  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });

  console.log("Chatbot: Hello! How can I help you today? (Type 'exit' to quit)");

  rl.on('line', async (input) => {
    if (input.toLowerCase() === 'exit') {
      console.log("Chatbot: Goodbye!");
      rl.close();
      return;
    }

    const response = await chatbot.respondTo(input);
    console.log("Chatbot:", response);
  });
}

main();