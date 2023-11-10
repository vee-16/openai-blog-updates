# blog_scraper.py

import requests
from bs4 import BeautifulSoup

BLOG_URL = 'https://openai.com/blog/'

def get_blog_posts(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        blog_links = soup.find_all('a', class_='ui-link')
        blog_list = []
        for link in blog_links:
            title = link.find('h3')
            date_div = link.find('span', class_='sr-only')
            if title and date_div:
                title_text = title.get_text(strip=True)
                date_text = date_div.get_text(strip=True)
                href = link['href']
                if not href.startswith('http'):
                    href = BLOG_URL.rstrip('/') + href
                blog_list.append((title_text, href, date_text))
        return blog_list
    else:
        print("Failed to retrieve the blog.")
        return []

def get_top_blog_posts(url, number_of_posts=2):
    return get_blog_posts(url)[:number_of_posts]
