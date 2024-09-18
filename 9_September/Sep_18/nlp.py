import asyncio
import aiohttp
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from concurrent.futures import ThreadPoolExecutor
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import time

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

class WebCrawler:
    def __init__(self, start_url, max_depth=3, max_pages=50):
        self.start_url = start_url
        self.max_depth = max_depth
        self.max_pages = max_pages
        self.visited = set()
        self.queue = asyncio.Queue()
        self.session = None
        self.executor = ThreadPoolExecutor(max_workers=10)
        self.stop_words = set(stopwords.words('english'))

    async def crawl(self):
        self.session = aiohttp.ClientSession()
        await self.queue.put((self.start_url, 0))
        tasks = [asyncio.create_task(self.worker()) for _ in range(10)]
        await self.queue.join()
        for task in tasks:
            task.cancel()
        await asyncio.gather(*tasks, return_exceptions=True)
        await self.session.close()

    async def worker(self):
        while True:
            url, depth = await self.queue.get()
            try:
                await self.process_url(url, depth)
            finally:
                self.queue.task_done()

    async def process_url(self, url, depth):
        if url in self.visited or depth > self.max_depth or len(self.visited) >= self.max_pages:
            return

        self.visited.add(url)
        print(f"Crawling: {url} (Depth: {depth})")

        try:
            async with self.session.get(url, timeout=10) as response:
                if response.status == 200:
                    content = await response.text()
                    soup = BeautifulSoup(content, 'html.parser')
                    
                    # Extract and analyze text content
                    text = soup.get_text()
                    await self.analyze_content(text)

                    # Find and queue new URLs
                    if depth < self.max_depth:
                        for link in soup.find_all('a', href=True):
                            new_url = urljoin(url, link['href'])
                            if self.is_valid_url(new_url):
                                await self.queue.put((new_url, depth + 1))
        except Exception as e:
            print(f"Error processing {url}: {e}")

    def is_valid_url(self, url):
        parsed = urlparse(url)
        return bool(parsed.netloc) and bool(parsed.scheme)

    async def analyze_content(self, text):
        loop = asyncio.get_event_loop()
        words = await loop.run_in_executor(self.executor, self.process_text, text)
        print(f"Top 5 words: {words.most_common(5)}")

    def process_text(self, text):
        tokens = word_tokenize(text.lower())
        words = [word for word in tokens if word.isalnum() and word not in self.stop_words]
        return Counter(words)

if __name__ == "__main__":
    start_time = time.time()
    start_url = "https://example.com"  # Replace with your desired starting URL
    crawler = WebCrawler(start_url)
    asyncio.run(crawler.crawl())
    print(f"Crawling completed in {time.time() - start_time:.2f} seconds")
    print(f"Total pages crawled: {len(crawler.visited)}")