const express = require('express');
const translate = require('@vitalets/google-translate-api');
const path = require('path');

const app = express();
const port = 3000;

app.use(express.json());
app.use(express.static('public'));

app.post('/translate', async (req, res) => {
    const { text, targetLang } = req.body;
    try {
        const result = await translate(text, { to: targetLang });
        res.json({ translatedText: result.text });
    } catch (error) {
        res.status(500).json({ error: 'Translation failed' });
    }
});

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});