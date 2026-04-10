# PRACTICAL 23: Web Scraping with BeautifulSoup

import requests
from bs4 import BeautifulSoup

# URL to scrape (example: Python official website)
url = "https://www.python.org/"

# Send HTTP request
response = requests.get(url)

# Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Example 1: Get the title of the page
print("Page Title:", soup.title.string)

# Example 2: Extract all links
print("\nAll Links on the Page:")
for link in soup.find_all('a'):
    print(link.get('href'))

# Example 3: Extract specific section (Upcoming Events)
print("\nUpcoming Events:")
events = soup.find('div', {"class": "medium-widget event-widget last"})
for event in events.find_all('li'):
    print(event.text)