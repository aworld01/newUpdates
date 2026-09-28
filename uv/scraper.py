import requests
from bs4 import BeautifulSoup

# Fetch the webpage
response = requests.get("https://example.com")

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find and print all h1 tags
h1_tags = soup.find_all("h1")
for tag in h1_tags:
    print(tag.text)


'''
uv run scraper.py #to run the programe
'''