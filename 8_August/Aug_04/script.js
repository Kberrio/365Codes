const NEWS_API_KEY = 'YOUR_NEWSAPI_KEY';
const GUARDIAN_API_KEY = 'YOUR_GUARDIAN_API_KEY';

const searchInput = document.getElementById('search-input');
const searchButton = document.getElementById('search-button');
const categorySelect = document.getElementById('category-select');
const newsContainer = document.getElementById('news-container');

searchButton.addEventListener('click', searchNews);
categorySelect.addEventListener('change', getTopHeadlines);

async function searchNews() {
    const query = searchInput.value;
    if (!query) return;

    const newsApiResults = await fetchNewsAPI(query);
    const guardianResults = await fetchGuardianAPI(query);

    displayNews([...newsApiResults, ...guardianResults]);
}

async function getTopHeadlines() {
    const category = categorySelect.value;
    const newsApiResults = await fetchNewsAPI('', category);
    const guardianResults = await fetchGuardianAPI('', category);

    displayNews([...newsApiResults, ...guardianResults]);
}

async function fetchNewsAPI(query = '', category = '') {
    const url = `https://newsapi.org/v2/top-headlines?country=us&apiKey=${NEWS_API_KEY}&q=${query}&category=${category}`;
    try {
        const response = await fetch(url);
        const data = await response.json();
        return data.articles.map(article => ({
            title: article.title,
            description: article.description,
            url: article.url,
            imageUrl: article.urlToImage,
            source: 'NewsAPI'
        }));
    } catch (error) {
        console.error('Error fetching from NewsAPI:', error);
        return [];
    }
}

async function fetchGuardianAPI(query = '', category = '') {
    const section = category ? `&section=${category}` : '';
    const url = `https://content.guardianapis.com/search?api-key=${GUARDIAN_API_KEY}&q=${query}${section}&show-fields=thumbnail,trailText`;
    try {
        const response = await fetch(url);
        const data = await response.json();
        return data.response.results.map(article => ({
            title: article.webTitle,
            description: article.fields.trailText,
            url: article.webUrl,
            imageUrl: article.fields.thumbnail,
            source: 'The Guardian'
        }));
    } catch (error) {
        console.error('Error fetching from Guardian API:', error);
        return [];
    }
}

function displayNews(articles) {
    newsContainer.innerHTML = '';
    articles.forEach(article => {
        const articleElement = document.createElement('div');
        articleElement.classList.add('news-item');
        articleElement.innerHTML = `
            <h2><a href="${article.url}" target="_blank">${article.title}</a></h2>
            ${article.imageUrl ? `<img src="${article.imageUrl}" alt="${article.title}">` : ''}
            <p>${article.description}</p>
            <p class="news-source">Source: ${article.source}</p>
        `;
        newsContainer.appendChild(articleElement);
    });
}

// Load top headlines on page load
window.addEventListener('load', getTopHeadlines);