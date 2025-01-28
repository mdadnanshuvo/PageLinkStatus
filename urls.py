import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# Step 1: Fetch the page content using requests
base_url = "https://www.rentbyowner.com/all/usa/florida"
response = requests.get(base_url)
html_content = response.text

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Step 3: Helper function to validate URLs
def is_valid_url(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

# Step 4: Extract and validate anchor hrefs
anchor_tags = soup.find_all('a', href=True)
urls = [
    urljoin(base_url, anchor['href'])  # Normalize relative URLs
    for anchor in anchor_tags
    if is_valid_url(urljoin(base_url, anchor['href']))  # Ensure URLs are valid
]

print(f"Valid anchor URLs found: {len(urls)}")

# Step 5: Extract and validate image srcs
image_tags = soup.find_all('img', src=True)
image_srcs = [
    urljoin(base_url, img['src'])  # Normalize relative URLs
    for img in image_tags
    if is_valid_url(urljoin(base_url, img['src']))  # Ensure URLs are valid
]

print(f"Valid image src URLs found: {len(image_srcs)}")

# Step 6: Test each URL and log the status
def check_urls(urls, url_type):
    for url in urls:
        try:
            response = requests.get(url, timeout=5)
            print(f"{url_type} URL: {url}, Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"{url_type} URL: {url}, Error: {e}")

# Check anchor URLs
print("\nTesting anchor URLs:")
check_urls(urls, "Anchor")

# Check image src URLs
print("\nTesting image src URLs:")
check_urls(image_srcs, "Image")
