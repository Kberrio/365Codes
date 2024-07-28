const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function miniClaude(input) {
  const lowercaseInput = input.toLowerCase();
  
  if (lowercaseInput.includes('hello') || lowercaseInput.includes('hi')) {
    return "Hello! How can I assist you today?";
  } else if (lowercaseInput.includes('how are you')) {
    return "I'm functioning well, thank you. How may I help you?";
  } else if (lowercaseInput.includes('bye') || lowercaseInput.includes('goodbye')) {
    return "Goodbye! Have a great day!";
  } else if (lowercaseInput.includes('name')) {
    return "I'm Mini Claude, a simple chatbot.";
  } else if (lowercaseInput.includes('weather')) {
    return "I'm sorry, I don't have access to real-time weather information.";
  } else {
    return "I'm not sure how to respond to that. Can you please rephrase or ask something else?";
  }
}

console.log("Mini Claude: Hello! I'm Mini Claude. How can I help you?");

function chat() {
  rl.question('You: ', (input) => {
    if (input.toLowerCase() === 'exit') {
      console.log("Mini Claude: Goodbye!");
      rl.close();
      return;
    }
    
    const response = miniClaude(input);
    console.log(`Mini Claude: ${response}`);
    chat();
  });
}

chat();