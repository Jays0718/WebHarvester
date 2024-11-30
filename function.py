from bs4 import BeautifulSoup
import requests

URL = "https://www.amazon.in/s?k=PLAYSTATION+4&crid=3DTNCEP63NF5U&sprefix=playstation+4%2Caps%2C197&ref=nb_sb_noss_2"

# headers for request
HEADERS = ({
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36", 
    'Accept-Language': 'en-US, en;q=0.5'
})

# HTTP request
webpage = requests.get(URL, headers=HEADERS)

# Parse the page content with BeautifulSoup
soup = BeautifulSoup(webpage.content, "html.parser")

# Find all links for product titles on the page
links = soup.find_all('a', class_='a-link-normal s-no-outline')
link = links[4].get('href')
product_link = "https://www.amazon.in" + link
print(f"Full product link: {product_link}")

