const API_KEY = 'YOUR_API_KEY';
const API_URL = 'https://free.currconv.com/api/v7';

const amountInput = document.getElementById('amount');
const fromCurrency = document.getElementById('from-currency');
const toCurrency = document.getElementById('to-currency');
const convertBtn = document.getElementById('convert');
const resultDiv = document.getElementById('result');

// Fetch available currencies and populate dropdowns
async function fetchCurrencies() {
    try {
        const response = await fetch(`${API_URL}/currencies?apiKey=${API_KEY}`);
        const data = await response.json();
        const currencies = Object.keys(data.results);

        currencies.forEach(currency => {
            fromCurrency.innerHTML += `<option value="${currency}">${currency}</option>`;
            toCurrency.innerHTML += `<option value="${currency}">${currency}</option>`;
        });
    } catch (error) {
        console.error('Error fetching currencies:', error);
    }
}

// Convert currency
async function convertCurrency() {
    const amount = amountInput.value;
    const from = fromCurrency.value;
    const to = toCurrency.value;

    if (!amount || !from || !to) {
        alert('Please fill in all fields');
        return;
    }

    try {
        const response = await fetch(`${API_URL}/convert?apiKey=${API_KEY}&q=${from}_${to}&compact=ultra`);
        const data = await response.json();
        const rate = data[`${from}_${to}`];
        const result = (amount * rate).toFixed(2);

        resultDiv.innerHTML = `${amount} ${from} = ${result} ${to}`;
    } catch (error) {
        console.error('Error converting currency:', error);
        resultDiv.innerHTML = 'Error converting currency. Please try again.';
    }
}

// Event listeners
convertBtn.addEventListener('click', convertCurrency);
window.addEventListener('load', fetchCurrencies);