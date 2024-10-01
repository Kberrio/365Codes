import requests
from bs4 import BeautifulSoup
import csv

def scrape_books(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all('article', class_='product_pod')

    data = []
    for book in books:
        title = book.h3.a['title']
        price = book.select_one('p.price_color').text
        availability = book.select_one('p.availability').text.strip()
        rating = book.p['class'][1]  # Assumes rating is second class

        data.append([title, price, availability, rating])

    return data

def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Price', 'Availability', 'Rating'])
        writer.writerows(data)

def main():
    base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
    all_data = []

    for page in range(1, 51):  # Scrape 50 pages
        url = base_url.format(page)
        page_data = scrape_books(url)
        all_data.extend(page_data)
        print(f"Scraped page {page}")

    save_to_csv(all_data, 'books_data.csv')
    print("Scraping completed. Data saved to books_data.csv")

if __name__ == '__main__':
    main()