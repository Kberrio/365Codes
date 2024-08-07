const API_KEY = 'YOUR_ALPHA_VANTAGE_API_KEY';
const stockInput = document.getElementById('stock-input');
const searchBtn = document.getElementById('search-btn');
const stockInfo = document.getElementById('stock-info');
const priceChart = document.getElementById('price-chart');
const watchlistItems = document.getElementById('watchlist-items');

let chart;

searchBtn.addEventListener('click', searchStock);

async function searchStock() {
    const symbol = stockInput.value.toUpperCase();
    if (!symbol) return;

    try {
        const quoteData = await fetchStockQuote(symbol);
        const companyData = await fetchCompanyInfo(symbol);
        displayStockInfo(quoteData, companyData);
        
        const historicalData = await fetchHistoricalData(symbol);
        displayChart(historicalData);
        
        addToWatchlist(symbol, quoteData['05. price']);
    } catch (error) {
        console.error('Error fetching stock data:', error);
        stockInfo.innerHTML = '<p>Error fetching stock data. Please try again.</p>';
    }
}

async function fetchStockQuote(symbol) {
    const response = await fetch(`https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=${symbol}&apikey=${API_KEY}`);
    const data = await response.json();
    return data['Global Quote'];
}

async function fetchCompanyInfo(symbol) {
    const response = await fetch(`https://www.alphavantage.co/query?function=OVERVIEW&symbol=${symbol}&apikey=${API_KEY}`);
    const data = await response.json();
    return data;
}

async function fetchHistoricalData(symbol) {
    const response = await fetch(`https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=${symbol}&apikey=${API_KEY}`);
    const data = await response.json();
    return data['Time Series (Daily)'];
}

function displayStockInfo(quoteData, companyData) {
    stockInfo.innerHTML = `
        <h2>${companyData.Name} (${companyData.Symbol})</h2>
        <p>Price: $${parseFloat(quoteData['05. price']).toFixed(2)}</p>
        <p>Change: ${quoteData['09. change']} (${quoteData['10. change percent']})</p>
        <p>Industry: ${companyData.Industry}</p>
        <p>Market Cap: $${companyData.MarketCapitalization}</p>
        <p>52 Week High: $${companyData['52WeekHigh']}</p>
        <p>52 Week Low: $${companyData['52WeekLow']}</p>
    `;
}

function displayChart(historicalData) {
    const dates = Object.keys(historicalData).slice(0, 30).reverse();
    const prices = dates.map(date => parseFloat(historicalData[date]['4. close']));

    if (chart) {
        chart.destroy();
    }

    chart = new Chart(priceChart, {
        type: 'line',
        data: {
            labels: dates,
            datasets: [{
                label: 'Closing Price',
                data: prices,
                borderColor: 'rgb(75, 192, 192)',
                tension: 0.1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: false
                }
            }
        }
    });
}

function addToWatchlist(symbol, price) {
    const listItem = document.createElement('li');
    listItem.innerHTML = `
        ${symbol} - $${parseFloat(price).toFixed(2)}
        <button class="remove-btn">Remove</button>
    `;
    listItem.querySelector('.remove-btn').addEventListener('click', () => {
        watchlistItems.removeChild(listItem);
    });
    watchlistItems.appendChild(listItem);
}

// Initialize the app
stockInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        searchStock();
    }
});