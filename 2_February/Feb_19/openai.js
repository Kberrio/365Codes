const fetch = require('node-fetch');

// Function to interact with the OpenAI API
async function generateText(prompt) {
    try {
        const response = await fetch('https://api.openai.com/v1/engines/davinci/completions', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer YOUR_API_KEY', // Replace YOUR_API_KEY with your actual OpenAI API key
            },
            body: JSON.stringify({
                prompt: prompt,
                max_tokens: 150,
            }),
        });
        
        const data = await response.json();
        return data.choices[0].text.trim();
    } catch (error) {
        console.error('Error:', error);
        return null;
    }
}

// Example usage
async function main() {
    const prompt = "Once upon a time";
    const generatedText = await generateText(prompt);
    if (generatedText) {
        console.log("Generated Text:");
        console.log(generatedText);
    } else {
        console.log("Failed to generate text.");
    }
}

main();
