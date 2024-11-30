from bs4 import BeautifulSoup
import requests

# Flipkart URL for searching PlayStation 4
URL = "https://www.flipkart.com/search?q=playstation+4"

# Headers for the request
HEADERS = ({
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    'Accept-Language': 'en-US, en;q=0.5'
})

# HTTP request
webpage = requests.get(URL, headers=HEADERS)

# Parse the page content with BeautifulSoup
soup = BeautifulSoup(webpage.content, "html.parser")

# Find all product links by inspecting Flipkart's product listing page
links = soup.find_all('a', class_='wjcEIp')  # This class is used for product links in grid views

# Check if any links were found
if links:
    # Get the first product link
    link = links[0].get('href')
    # Build the full URL to the product
    product_link = "https://www.flipkart.com" + link
    print(f"Full product link: {product_link}")
else:
    print("No products found.")
