import requests
from bs4 import BeautifulSoup

# Step 1: Fetch the page content using requests
url = "https://www.rentbyowner.com/all/usa/florida"
response = requests.get(url)
html_content = response.text

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Step 3: Find all anchor tags (<a>) and extract the href attribute
anchor_tags = soup.find_all('a', href=True)  # This finds all <a> tags with href attribute

# Step 4: Extract the URLs from the href attributes
urls = [anchor['href'] for anchor in anchor_tags]


print(len(urls))
# Step 5: Print the URLs
for url in urls:
    print(url)
