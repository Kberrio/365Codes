const API_URL = 'https://libretranslate.de/';
const sourceLang = document.getElementById('source-lang');
const targetLang = document.getElementById('target-lang');
const sourceText = document.getElementById('source-text');
const targetText = document.getElementById('target-text');
const translateBtn = document.getElementById('translate-btn');
const swapLangBtn = document.getElementById('swap-lang');
const detectedLang = document.getElementById('detected-lang');

// Fetch supported languages and populate dropdowns
async function getLanguages() {
    try {
        const response = await fetch(`${API_URL}languages`);
        const languages = await response.json();
        
        languages.forEach(lang => {
            sourceLang.innerHTML += `<option value="${lang.code}">${lang.name}</option>`;
            targetLang.innerHTML += `<option value="${lang.code}">${lang.name}</option>`;
        });
        
        // Set default languages
        sourceLang.value = 'en';
        targetLang.value = 'es';
    } catch (error) {
        console.error('Error fetching languages:', error);
    }
}

// Translate text
async function translateText() {
    const text = sourceText.value;
    const source = sourceLang.value;
    const target = targetLang.value;

    if (!text) return;

    try {
        const response = await fetch(`${API_URL}translate`, {
            method: 'POST',
            body: JSON.stringify({
                q: text,
                source: source,
                target: target
            }),
            headers: { 'Content-Type': 'application/json' }
        });

        const data = await response.json();
        targetText.value = data.translatedText;
    } catch (error) {
        console.error('Error translating text:', error);
    }
}

// Detect language
async function detectLanguage() {
    const text = sourceText.value;
    if (!text) return;

    try {
        const response = await fetch(`${API_URL}detect`, {
            method: 'POST',
            body: JSON.stringify({ q: text }),
            headers: { 'Content-Type': 'application/json' }
        });

        const data = await response.json();
        const detectedCode = data[0].language;
        sourceLang.value = detectedCode;
        detectedLang.textContent = `Detected language: ${sourceLang.options[sourceLang.selectedIndex].text}`;
    } catch (error) {
        console.error('Error detecting language:', error);
    }
}

// Swap languages
function swapLanguages() {
    const temp = sourceLang.value;
    sourceLang.value = targetLang.value;
    targetLang.value = temp;

    const tempText = sourceText.value;
    sourceText.value = targetText.value;
    targetText.value = tempText;
}

// Event listeners
translateBtn.addEventListener('click', translateText);
swapLangBtn.addEventListener('click', swapLanguages);
sourceText.addEventListener('input', () => {
    if (sourceLang.value === 'auto') {
        detectLanguage();
    }
});

// Initialize app
getLanguages();